"""
Vector Database Manager module for Jeju Tourism RAG system.
Integrates persistent ChromaDB vector store, handles deduplication,
batch indexing, metadata preservation, and similarity querying.
"""
import logging
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"
try:
    import posthog
    posthog.capture = lambda *args, **kwargs: None
except Exception:
    pass
import chromadb
from chromadb.config import Settings as ChromaSettings
from langchain_core.documents import Document

from config.settings import settings
from src.embeddings import EmbeddingManager
from src.chunking import DocumentChunker

logger = logging.getLogger(__name__)


class VectorDatabaseManager:
    """Manages persistent ChromaDB vector store operations."""

    def __init__(
        self,
        persist_directory: Optional[str] = None,
        collection_name: Optional[str] = None,
        embedding_manager: Optional[EmbeddingManager] = None,
    ):
        self.persist_directory = persist_directory or settings.CHROMA_PERSIST_DIR
        self.collection_name = collection_name or settings.COLLECTION_NAME
        self.embedding_manager = embedding_manager or EmbeddingManager()

        # Ensure persist directory exists
        Path(self.persist_directory).mkdir(parents=True, exist_ok=True)

        logger.info(f"Connecting to persistent ChromaDB at '{self.persist_directory}'...")
        self.client = chromadb.PersistentClient(
            path=self.persist_directory,
            settings=ChromaSettings(anonymized_telemetry=False, is_persistent=True),
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={
                "hnsw:space": "cosine",
                "hnsw:batch_size": 10000,
                "hnsw:sync_threshold": 10000,
            },
        )

    def add_chunks(self, chunks: List[Document]) -> Dict[str, Any]:
        """
        Add document chunks to ChromaDB with automatic deduplication by chunk_id.
        """
        if not chunks:
            return {"added": 0, "skipped_duplicates": 0, "total_in_db": self.collection.count()}

        # Query existing IDs in collection to avoid duplicate re-indexing
        existing_result = self.collection.get()
        existing_ids = set(existing_result["ids"]) if existing_result and "ids" in existing_result else set()

        new_chunks = [c for c in chunks if c.metadata.get("chunk_id") not in existing_ids]
        skipped_count = len(chunks) - len(new_chunks)

        if not new_chunks:
            logger.info(f"All {len(chunks)} chunks already exist in ChromaDB collection. Skipped indexing.")
            return {
                "added": 0,
                "skipped_duplicates": skipped_count,
                "total_in_db": self.collection.count(),
            }

        texts = [c.page_content for c in new_chunks]
        ids = [c.metadata["chunk_id"] for c in new_chunks]

        # Chroma metadata must have primitive values (str, int, float, bool)
        metadatas = []
        for c in new_chunks:
            clean_meta = {}
            for k, v in c.metadata.items():
                if isinstance(v, (str, int, float, bool)):
                    clean_meta[k] = v
                else:
                    clean_meta[k] = str(v)
            metadatas.append(clean_meta)

        # Generate embeddings
        logger.info(f"Generating embeddings for {len(new_chunks)} new chunks...")
        embeddings = self.embedding_manager.embed_documents(texts)

        # Batch insert into ChromaDB
        batch_size = 100
        for i in range(0, len(new_chunks), batch_size):
            end_idx = min(i + batch_size, len(new_chunks))
            self.collection.add(
                ids=ids[i:end_idx],
                embeddings=embeddings[i:end_idx],
                metadatas=metadatas[i:end_idx],
                documents=texts[i:end_idx],
            )

        logger.info(f"Successfully added {len(new_chunks)} chunks to collection '{self.collection_name}'. Total: {self.collection.count()}")
        return {
            "added": len(new_chunks),
            "skipped_duplicates": skipped_count,
            "total_in_db": self.collection.count(),
        }

    def index_documents(
        self,
        documents: List[Document],
        chunk_size: int = None,
        chunk_overlap: int = None,
    ) -> Dict[str, Any]:
        """
        Full ingestion pipeline: takes Document objects, splits into chunks, and saves to ChromaDB.
        """
        chunker = DocumentChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = chunker.split_documents(documents)
        result = self.add_chunks(chunks)
        result["chunk_stats"] = chunker.get_chunk_statistics(chunks)
        return result

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Perform semantic similarity search for a query string.
        Returns retrieved chunks with metadata and cosine similarity score.
        """
        if self.collection.count() == 0:
            logger.warning("Vector database is empty. Please index documents first.")
            return []

        query_vector = self.embedding_manager.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=min(top_k, self.collection.count()),
            include=["documents", "metadatas", "distances"],
        )

        retrieved_items = []
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0]
            distances = results["distances"][0]

            for doc_text, meta, dist in zip(docs, metas, distances):
                # For cosine distance: distance is 1 - cosine_similarity
                # Cosine similarity is in [-1, 1], but for normalized positive vectors it is in [0, 1]
                # Similarity score = 1.0 - distance
                similarity_score = max(0.0, min(1.0, 1.0 - float(dist)))
                retrieved_items.append({
                    "content": doc_text,
                    "metadata": meta,
                    "distance": float(dist),
                    "similarity_score": round(similarity_score, 4),
                    "source": meta.get("source", "unknown"),
                    "filename": meta.get("filename", "unknown"),
                    "page": meta.get("page", 1),
                    "chunk_id": meta.get("chunk_id", ""),
                })

        return retrieved_items

    def get_stats(self) -> Dict[str, Any]:
        """Get collection health, chunk count, unique documents, and storage path."""
        count = self.collection.count()
        unique_sources = set()

        if count > 0:
            all_records = self.collection.get(include=["metadatas"])
            if all_records and "metadatas" in all_records:
                for m in all_records["metadatas"]:
                    if m and "filename" in m:
                        unique_sources.add(m["filename"])

        return {
            "collection_name": self.collection_name,
            "total_chunks": count,
            "unique_documents_count": len(unique_sources),
            "indexed_documents": sorted(list(unique_sources)),
            "persist_directory": self.persist_directory,
            "embedding_model": self.embedding_manager.model_name,
            "embedding_dimension": self.embedding_manager.get_embedding_dimension(),
        }

    def clear_collection(self) -> None:
        """Reset and wipe the current ChromaDB collection."""
        logger.warning(f"Resetting collection '{self.collection_name}'...")
        self.client.delete_collection(self.collection_name)
        self.collection = self.client.get_or_create_collection(
            metadata={
                "hnsw:space": "cosine",
                "hnsw:batch_size": 10000,
                "hnsw:sync_threshold": 10000,
            },
        )
        logger.info(f"Collection '{self.collection_name}' has been cleared.")
