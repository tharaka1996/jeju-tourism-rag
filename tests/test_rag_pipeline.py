"""Integration tests for the complete RAGGenerationPipeline."""
import pytest
from src.generation import RAGGenerationPipeline


def test_rag_in_domain_answer():
    pipeline = RAGGenerationPipeline()
    res = pipeline.query("What are the admission fees for Seongsan Ilchulbong?", top_k=3)

    assert "answer" in res
    assert len(res["answer"]) > 20
    assert "retrieved_chunks" in res
    assert len(res["retrieved_chunks"]) > 0

    # Answer should contain 5,000 KRW
    assert "5,000" in res["answer"]
    assert "Sources Consulted:" in res["answer"]


def test_rag_out_of_domain_refusal():
    pipeline = RAGGenerationPipeline()
    res = pipeline.query("How to apply for a mortgage loan in Canada?", top_k=3)

    assert "answer" in res
    # Should contain explicit refusal
    refusal_phrases = ["sufficient information is unavailable", "do not contain", "cannot be found"]
    assert any(p in res["answer"].lower() for p in refusal_phrases)
