"""
Batch index all documents into ChromaDB with explicit progress printing and exception handling.
"""

import sys
import os
import time
from pathlib import Path

# Set UTF-8 encoding for Windows console (cp949 support)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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


def run_batch_indexing():
    print("=" * 70, flush=True)
    print("🚀 BATCH INDEXING EXPANDED JEJU TOURISM CORPUS (61 DOCUMENTS)", flush=True)
    print("=" * 70, flush=True)

    loader = DocumentLoader()
    docs = loader.load_directory(settings.DOCS_DIR)
    print(f"Loaded {len(docs)} document objects across {len(set(d.metadata['source'] for d in docs))} unique files.", flush=True)

    chunker = DocumentChunker(
        chunk_size=settings.DEFAULT_CHUNK_SIZE,
        chunk_overlap=settings.DEFAULT_CHUNK_OVERLAP,
    )
    chunks = chunker.split_documents(docs)
    print(f"Total chunks in corpus: {len(chunks)}", flush=True)

    # Connect to ChromaDB
    client = chromadb.PersistentClient(
        path=str(settings.VECTORSTORE_DIR),
        settings=ChromaSettings(anonymized_telemetry=False, is_persistent=True),
    )
    col = client.get_or_create_collection(
        name=settings.COLLECTION_NAME,
        metadata={
            "hnsw:space": "cosine",
            "hnsw:batch_size": 10000,
            "hnsw:sync_threshold": 10000,
        },
    )
    print(f"Current chunks in ChromaDB collection: {col.count()}", flush=True)

    em = EmbeddingManager()
    existing_ids = set(col.get()["ids"]) if col.count() > 0 else set()
    new_chunks = [c for c in chunks if c.metadata["chunk_id"] not in existing_ids]
    print(f"Remaining chunks to index: {len(new_chunks)}", flush=True)

    if not new_chunks:
        print("All chunks are already indexed!", flush=True)
        return

    batch_size = 20
    total_batches = (len(new_chunks) + batch_size - 1) // batch_size

    for b in range(total_batches):
        start_idx = b * batch_size
        end_idx = min(start_idx + batch_size, len(new_chunks))
        batch = new_chunks[start_idx:end_idx]

        b_texts = [c.page_content for c in batch]
        b_ids = [c.metadata["chunk_id"] for c in batch]
        b_metas = []
        for c in batch:
            clean_m = {k: v for k, v in c.metadata.items() if isinstance(v, (str, int, float, bool))}
            b_metas.append(clean_m)

        try:
            print(f"[{b+1}/{total_batches}] Generating embeddings for {len(batch)} chunks...", end="", flush=True)
            b_vecs = em.embed_documents(b_texts)
            col.add(ids=b_ids, embeddings=b_vecs, metadatas=b_metas, documents=b_texts)
            print(f" Done! DB Total: {col.count()}", flush=True)
            time.sleep(0.2)
        except Exception as e:
            print(f"\n❌ Error in batch {b+1}: {e}", flush=True)

    print("\n" + "=" * 70, flush=True)
    print(f"🎉 INDEXING PROCESS FINISHED! Final Total Chunks in ChromaDB: {col.count()}", flush=True)
    print("=" * 70, flush=True)


if __name__ == "__main__":
    import traceback
    try:
        run_batch_indexing()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
