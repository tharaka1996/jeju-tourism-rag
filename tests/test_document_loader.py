"""Unit tests for DocumentLoader module."""
import pytest
from pathlib import Path
from src.document_loader import DocumentLoader
from config.settings import settings


def test_load_txt_file():
    loader = DocumentLoader()
    txt_path = settings.DOCS_DIR / "01_hallasan_national_park.txt"
    assert txt_path.exists(), "Sample TXT document must exist"

    docs = loader.load_file(txt_path)
    assert len(docs) == 1
    doc = docs[0]
    assert doc.metadata["filename"] == "01_hallasan_national_park.txt"
    assert doc.metadata["file_type"] == "txt"
    assert doc.metadata["page"] == 1
    assert "Hallasan" in doc.page_content
    assert doc.metadata["char_count"] > 100


def test_load_pdf_file():
    loader = DocumentLoader()
    pdf_path = settings.DOCS_DIR / "jeju_official_travel_guide_sample.pdf"
    assert pdf_path.exists(), "Sample PDF document must exist"

    docs = loader.load_file(pdf_path)
    assert len(docs) >= 1
    for d in docs:
        assert d.metadata["file_type"] == "pdf"
        assert d.metadata["page"] >= 1
        assert len(d.page_content) > 0


def test_unsupported_file_extension():
    loader = DocumentLoader()
    with pytest.raises(ValueError, match="Unsupported file format"):
        loader.load_file("test_document.docx")
