"""Unit tests for DocumentChunker module."""
import pytest
from langchain_core.documents import Document
from src.chunking import DocumentChunker


def test_chunking_preserves_metadata():
    chunker = DocumentChunker(chunk_size=100, chunk_overlap=20)
    sample_text = (
        "Hallasan Mountain is a shield volcano on Jeju Island. "
        "It is the highest mountain in South Korea with an elevation of 1947 meters. "
        "The Seongpanak and Gwaneumsa trails reach the crater lake summit of Baeknokdam. "
        "Trekking during the winter season requires crampons and poles."
    )
    doc = Document(
        page_content=sample_text,
        metadata={"filename": "test_guide.txt", "page": 1, "source": "test_guide.txt"},
    )

    chunks = chunker.split_documents([doc])
    assert len(chunks) > 1

    for idx, c in enumerate(chunks):
        assert c.metadata["filename"] == "test_guide.txt"
        assert c.metadata["page"] == 1
        assert "chunk_id" in c.metadata
        assert c.metadata["chunk_index"] == idx
        assert len(c.page_content) <= 120


def test_chunking_statistics():
    chunker = DocumentChunker(chunk_size=150, chunk_overlap=30)
    docs = [
        Document(page_content="Sentence one is about Jeju beaches. " * 5, metadata={"filename": "d1.txt"}),
        Document(page_content="Sentence two is about Hallasan hiking. " * 5, metadata={"filename": "d2.txt"}),
    ]
    chunks = chunker.split_documents(docs)
    stats = chunker.get_chunk_statistics(chunks)

    assert stats["total_chunks"] == len(chunks)
    assert stats["avg_char_length"] > 0
    assert stats["min_char_length"] > 0
