"""
Retrieval Engine module for Jeju Tourism RAG system.
Performs semantic similarity searches in ChromaDB, applies threshold filtering,
formats retrieved passages with clear citation tags, and measures retrieval latency.
"""
import time
import logging
from typing import List, Dict, Any, Tuple
from config.settings import settings
from src.vector_database import VectorDatabaseManager

logger = logging.getLogger(__name__)


class RetrievalEngine:
    """Handles semantic retrieval of document chunks for incoming queries."""

    def __init__(self, vector_db: VectorDatabaseManager = None):
        self.vector_db = vector_db or VectorDatabaseManager()

    def retrieve(
        self,
        query: str,
        top_k: int = None,
        threshold: float = None,
    ) -> Dict[str, Any]:
        """
        Execute semantic retrieval for a user question.

        Returns:
            Dict containing:
                - chunks: List of retrieved chunk dictionaries
                - context_text: Formatted context string for prompt injection
                - latency_seconds: Time taken to retrieve
                - top_k: Requested top_k
                - is_sufficient: Boolean indicating if any chunk met the threshold
        """
        k = top_k if top_k is not None else settings.DEFAULT_TOP_K
        thresh = threshold if threshold is not None else settings.SIMILARITY_SCORE_THRESHOLD

        start_time = time.perf_counter()
        raw_results = self.vector_db.search(query=query, top_k=k)
        retrieval_time = time.perf_counter() - start_time

        # Filter by threshold if specified
        valid_chunks = [item for item in raw_results if item["similarity_score"] >= thresh]

        # If no chunks met the strict threshold, keep raw_results as fallback but flag is_sufficient as False
        is_sufficient = len(valid_chunks) > 0
        chunks_to_use = valid_chunks if is_sufficient else raw_results

        # Format clean context string with citations
        context_blocks = []
        for idx, chunk in enumerate(chunks_to_use, start=1):
            source_tag = f"[Source {idx} | Document: {chunk['filename']} | Page: {chunk['page']} | Score: {chunk['similarity_score']:.4f}]"
            context_blocks.append(f"{source_tag}\n{chunk['content']}\n")

        context_text = "\n".join(context_blocks) if context_blocks else "No relevant documents found."

        return {
            "query": query,
            "chunks": chunks_to_use,
            "raw_chunks": raw_results,
            "context_text": context_text,
            "latency_seconds": round(retrieval_time, 4),
            "top_k": k,
            "threshold": thresh,
            "is_sufficient": is_sufficient,
        }

    def format_sources_summary(self, chunks: List[Dict[str, Any]]) -> str:
        """Generate human-readable summary of retrieved sources."""
        if not chunks:
            return "No sources retrieved."

        lines = ["### Retrieved Source Passages:"]
        for i, c in enumerate(chunks, 1):
            lines.append(
                f"- **Source {i}**: `{c['filename']}` (Page {c['page']}) "
                f"— Similarity Score: `{c['similarity_score']:.4f}`"
            )
        return "\n".join(lines)
