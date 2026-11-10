"""Unit tests for RetrievalEngine and VectorDatabaseManager."""
import pytest
from src.vector_database import VectorDatabaseManager
from src.retrieval import RetrievalEngine


def test_vector_db_stats():
    vdb = VectorDatabaseManager()
    stats = vdb.get_stats()
    assert stats["total_chunks"] > 0
    assert stats["unique_documents_count"] >= 8
    assert stats["embedding_dimension"] == 384


def test_semantic_retrieval_relevance():
    retrieval = RetrievalEngine()
    query = "Hallasan mountain hiking trails Seongpanak and Gwaneumsa"
    result = retrieval.retrieve(query=query, top_k=3)

    assert "chunks" in result
    assert len(result["chunks"]) <= 3
    assert result["is_sufficient"] is True

    # The top retrieved chunk should be from Hallasan or the official guide
    top_chunk = result["chunks"][0]
    assert top_chunk["filename"] in ["01_hallasan_national_park.txt", "jeju_official_travel_guide_sample.pdf"]
    assert top_chunk["similarity_score"] > 0.40
