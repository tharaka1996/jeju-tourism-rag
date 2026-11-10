"""
Document Loader module for Jeju Tourism RAG system.
Loads TXT and PDF documents, extracts text and metadata, and prepares LangChain Document objects.
"""
import os
import io
import logging
from pathlib import Path
from typing import List, Dict, Any, Union, BinaryIO
from langchain_core.documents import Document
from pypdf import PdfReader
from src.preprocessing import TextPreprocessor

logger = logging.getLogger(__name__)


class DocumentLoader:
    """Loads and extracts text and metadata from PDF and TXT files."""

    def __init__(self):
        self.preprocessor = TextPreprocessor()

    def load_txt(self, file_path_or_buffer: Union[str, Path, BinaryIO], filename: str = "") -> List[Document]:
        """Load text from a TXT file or binary buffer."""
        content = ""
        source_name = filename

        if isinstance(file_path_or_buffer, (str, Path)):
            path = Path(file_path_or_buffer)
            source_name = source_name or path.name
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(path, "r", encoding="latin-1") as f:
                    content = f.read()
        else:
            # File-like object (e.g. from Streamlit)
            raw_bytes = file_path_or_buffer.read()
            try:
                content = raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                content = raw_bytes.decode("latin-1", errors="ignore")

        cleaned = self.preprocessor.clean_text(content)
        if not cleaned:
            logger.warning(f"TXT document '{source_name}' contains no readable text.")
            return []

        doc = Document(
            page_content=cleaned,
            metadata={
                "source": source_name,
                "filename": source_name,
                "file_type": "txt",
                "page": 1,
                "total_pages": 1,
                "char_count": len(cleaned),
            },
        )
        return [doc]

    def load_pdf(self, file_path_or_buffer: Union[str, Path, BinaryIO], filename: str = "") -> List[Document]:
        """Load text from a PDF file, extracting page-by-page with metadata."""
        documents = []
        source_name = filename

        if isinstance(file_path_or_buffer, (str, Path)):
            path = Path(file_path_or_buffer)
            source_name = source_name or path.name
            reader = PdfReader(str(path))
        else:
            source_name = source_name or "uploaded_document.pdf"
            reader = PdfReader(file_path_or_buffer)

        total_pages = len(reader.pages)
        for page_num, page in enumerate(reader.pages, start=1):
            raw_text = page.extract_text() or ""
            cleaned = self.preprocessor.clean_text(raw_text)

            if cleaned:
                doc = Document(
                    page_content=cleaned,
                    metadata={
                        "source": source_name,
                        "filename": source_name,
                        "file_type": "pdf",
                        "page": page_num,
                        "total_pages": total_pages,
                        "char_count": len(cleaned),
                    },
                )
                documents.append(doc)

        if not documents:
            logger.warning(f"PDF document '{source_name}' yielded no extractable text.")
        return documents

    def load_file(self, file_path_or_buffer: Union[str, Path, BinaryIO], filename: str = "") -> List[Document]:
        """Load a file based on its extension."""
        name = filename
        if isinstance(file_path_or_buffer, (str, Path)):
            name = Path(file_path_or_buffer).name
        name_lower = name.lower()

        if name_lower.endswith(".pdf"):
            return self.load_pdf(file_path_or_buffer, filename=name)
        elif name_lower.endswith(".txt"):
            return self.load_txt(file_path_or_buffer, filename=name)
        else:
            raise ValueError(f"Unsupported file format: {name}. Only .pdf and .txt are supported.")

    def load_directory(self, dir_path: Union[str, Path]) -> List[Document]:
        """Load all supported documents from a directory."""
        directory = Path(dir_path)
        all_docs = []
        if not directory.exists():
            logger.error(f"Directory {directory} does not exist.")
            return all_docs

        for file_path in sorted(directory.iterdir()):
            if file_path.suffix.lower() in [".txt", ".pdf"]:
                try:
                    docs = self.load_file(file_path)
                    all_docs.extend(docs)
                    logger.info(f"Loaded {len(docs)} section(s) from {file_path.name}")
                except Exception as e:
                    logger.error(f"Error loading {file_path.name}: {e}")

        return all_docs
