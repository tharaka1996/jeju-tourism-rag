"""
ChromaDB Inspection Utility for Jeju Tourism RAG Assistant.
Run this script anytime to inspect collections, chunks, metadata, and embeddings.
Usage:
    python scripts/view_chromadb.py
"""

import sys
from pathlib import Path
from collections import Counter

# Set UTF-8 encoding for Windows console (cp949 support)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import chromadb
from chromadb.config import Settings as ChromaSettings
from config.settings import settings


def inspect_chroma():
    persist_dir = str(settings.VECTORSTORE_DIR)
    print("=" * 70)
    print("🏝️  CHROMA VECTOR DATABASE INSPECTION REPORT")
    print("=" * 70)
    print(f"📁 Storage Path: {persist_dir}")

    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=ChromaSettings(anonymized_telemetry=False, is_persistent=True),
    )

    collections = client.list_collections()
    print(f"📦 Total Collections: {len(collections)}")

    for col in collections:
        count = col.count()
        print(f"\n📂 Collection Name: '{col.name}'")
        print(f"   ├─ Distance Metric: {col.metadata.get('hnsw:space', 'l2')}")
        print(f"   └─ Total Stored Chunks: {count}")

        if count == 0:
            print("   ⚠️  Collection is currently empty.")
            continue

        # Fetch all metadata to compute document breakdown
        data = col.get(include=["metadatas", "documents"])
        filenames = [m.get("filename", "unknown") for m in data["metadatas"]]
        file_counts = Counter(filenames)

        print("\n📊 Chunks Distribution Across Ingested Documents:")
        for fname, chunk_cnt in sorted(file_counts.items()):
            print(f"   • {fname:<45} : {chunk_cnt:>2} chunks")

        # Peek at 3 sample chunks
        print("\n🔎 Sample Indexed Chunks (First 3):")
        peek = col.peek(limit=3)
        for i, (cid, doc, meta) in enumerate(zip(peek["ids"], peek["documents"], peek["metadatas"]), 1):
            print(f"\n   [Chunk #{i}]")
            print(f"   ├─ ID: {cid}")
            print(f"   ├─ Source: {meta.get('filename')} (Page {meta.get('page')})")
            print(f"   ├─ Length: {len(doc)} chars")
            print("   ├─ Content Preview:")
            preview = "\n".join("   │   " + line for line in doc[:250].splitlines())
            print(preview + " ...")

    print("\n" + "=" * 70)
    print("💡 To interactively inspect, search, and view similarity scores in your browser:")
    print("   1. Run: streamlit run app.py")
    print("   2. Open: http://localhost:8501")
    print("   3. Go to Tab 4: '🔍 Retrieval Inspector' or Tab 1: '🏠 Dashboard & Architecture'")
    print("=" * 70)


if __name__ == "__main__":
    inspect_chroma()
