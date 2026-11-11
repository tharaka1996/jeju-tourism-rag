"""
Re-index all documents into ChromaDB with hnsw:batch_size=10000 setting to bypass Windows pybind11 bug.
Loads 61 documents (60 TXT + 1 PDF), splits into 267 chunks,
generates 384-dimensional embeddings, and commits cleanly to vectorstore/.
"""

import os
import sys
import time
from pathlib import Path

# Configure UTF-8 for console output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Safe telemetry suppression
os.environ["ANONYMIZED_TELEMETRY"] = "False"
try:
    import posthog
    posthog.capture = lambda *args, **kwargs: None
except Exception:
    pass

import chromadb
from chromadb.config import Settings as ChromaSettings
from config.settings import settings
from src.document_loader import DocumentLoader
from src.chunking import DocumentChunker
from src.embeddings import EmbeddingManager


def reindex_all():
    print("=" * 70, flush=True)
    print("🚀 RE-INDEXING JEJU TOURISM RAG KNOWLEDGE BASE (61 DOCUMENTS)", flush=True)
    print("=" * 70, flush=True)

    vectorstore_path = settings.VECTORSTORE_DIR
    vectorstore_path.mkdir(parents=True, exist_ok=True)

    # 1. Connect to ChromaDB client
    client = chromadb.PersistentClient(
        path=str(vectorstore_path),
        settings=ChromaSettings(anonymized_telemetry=False, is_persistent=True),
    )

    # Safely clear old collection if it exists
    existing_cols = [c.name for c in client.list_collections()]
    if settings.COLLECTION_NAME in existing_cols:
        print(f"🧹 Resetting collection '{settings.COLLECTION_NAME}'...", flush=True)
        client.delete_collection(settings.COLLECTION_NAME)

    col = client.create_collection(
        name=settings.COLLECTION_NAME,
        metadata={
            "hnsw:space": "cosine",
            "hnsw:batch_size": 10000,
            "hnsw:sync_threshold": 10000,
        },
    )

    # 2. Load all documents from data/documents/
    print(f"\n📂 Loading documents from '{settings.DOCS_DIR}'...", flush=True)
    loader = DocumentLoader()
    raw_docs = loader.load_directory(settings.DOCS_DIR)
    unique_files = set(d.metadata["source"] for d in raw_docs)
    print(f"✅ Successfully loaded {len(raw_docs)} document sections across {len(unique_files)} unique files.", flush=True)

    # 3. Chunk documents
    print("\n✂️  Chunking documents (chunk_size=750, overlap=75)...", flush=True)
    chunker = DocumentChunker(
        chunk_size=settings.DEFAULT_CHUNK_SIZE,
        chunk_overlap=settings.DEFAULT_CHUNK_OVERLAP,
    )
    chunks = chunker.split_documents(raw_docs)
    stats = chunker.get_chunk_statistics(chunks)
    print(f"✅ Generated {len(chunks)} chunks total.", flush=True)
    print(f"   Avg chunk length: {stats['avg_char_length']:.1f} characters", flush=True)
    print(f"   Min length: {stats['min_char_length']}, Max length: {stats['max_char_length']}", flush=True)

    # 4. Generate Embeddings
    print("\n🧠 Generating 384-dimensional dense embeddings with all-MiniLM-L6-v2...", flush=True)
    texts = [c.page_content for c in chunks]
    ids = [c.metadata["chunk_id"] for c in chunks]
    metadatas = []
    for c in chunks:
        clean_meta = {}
        for k, v in c.metadata.items():
            if isinstance(v, (str, int, float, bool)):
                clean_meta[k] = v
            else:
                clean_meta[k] = str(v)
        metadatas.append(clean_meta)

    t0 = time.time()
    em = EmbeddingManager()
    embeddings = em.embed_documents(texts)
    embed_time = time.time() - t0
    print(f"✅ Generated {len(embeddings)} embeddings in {embed_time:.2f}s ({len(embeddings)/embed_time:.1f} chunks/sec).", flush=True)

    # 5. Populate ChromaDB collection in one clean pass
    print(f"\n💾 Writing {len(chunks)} chunks to collection '{settings.COLLECTION_NAME}'...", flush=True)
    col.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=texts,
    )

    final_count = col.count()
    print(f"\n🎉 ALL CHUNKS COMMITTED! Final ChromaDB Total: {final_count} chunks.", flush=True)

    # 6. Sanity check search
    print("\n🔍 Running sanity check query: 'Hallasan summit reservation requirements'...", flush=True)
    query_vec = em.embed_query("Hallasan summit reservation requirements")
    res = col.query(query_embeddings=[query_vec], n_results=3)
    for idx, (doc, dist, meta) in enumerate(zip(res["documents"][0], res["distances"][0], res["metadatas"][0])):
        sim = 1.0 - dist
        print(f"   [Result #{idx+1}] Sim: {sim:.4f} | Source: {meta.get('source')} (P.{meta.get('page')})")
        print(f"      {doc[:120].strip()}...")

    print("\n" + "=" * 70, flush=True)
    print("✅ RE-INDEXING COMPLETED SUCCESSFULLY!", flush=True)
    print("=" * 70, flush=True)
    return final_count


if __name__ == "__main__":
    reindex_all()
