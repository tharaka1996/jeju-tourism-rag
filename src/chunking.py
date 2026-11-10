"""
Document Chunking module for Jeju Tourism RAG system.
Splits documents into meaningful chunks using LangChain text splitters,
preserving all document metadata, page numbers, and generating unique chunk IDs.
"""
import hashlib
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import settings

logger = logging.getLogger(__name__)


class DocumentChunker:
    """Splits documents into overlapping chunks with rich metadata."""

    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        self.chunk_size = chunk_size or settings.DEFAULT_CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or settings.DEFAULT_CHUNK_OVERLAP

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " "],
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split a list of documents into chunks, assigning unique IDs and chunk indices.
        """
        chunked_docs = []
        chunk_counters: Dict[str, int] = {}

        for doc in documents:
            filename = doc.metadata.get("filename", "unknown_doc")
            page = doc.metadata.get("page", 1)
            raw_chunks = self.splitter.split_text(doc.page_content)

            # Generate clean document title for context grounding
            doc_title = Path(filename).stem.replace("_", " ").title()

            for chunk_text in raw_chunks:
                chunk_text = chunk_text.strip()
                if not chunk_text:
                    continue

                if filename not in chunk_counters:
                    chunk_counters[filename] = 0
                chunk_index = chunk_counters[filename]
                chunk_counters[filename] += 1

                # Context-aware chunking: Prepend document title if not already at the start
                if not chunk_text.lower().startswith("title:"):
                    enriched_chunk_text = f"[{doc_title} - Page {page}]\n{chunk_text}"
                else:
                    enriched_chunk_text = chunk_text

                # Generate deterministic hash for deduplication
                content_hash = hashlib.sha256(enriched_chunk_text.encode("utf-8")).hexdigest()[:12]
                chunk_id = f"{filename}_p{page}_c{chunk_index}_{content_hash}"

                meta = dict(doc.metadata)
                meta.update({
                    "chunk_id": chunk_id,
                    "chunk_index": chunk_index,
                    "chunk_char_count": len(enriched_chunk_text),
                    "chunk_size_config": self.chunk_size,
                    "chunk_overlap_config": self.chunk_overlap,
                })

                chunked_doc = Document(page_content=enriched_chunk_text, metadata=meta)
                chunked_docs.append(chunked_doc)

        logger.info(f"Split {len(documents)} document section(s) into {len(chunked_docs)} chunks.")
        return chunked_docs

    @staticmethod
    def get_chunk_statistics(chunks: List[Document]) -> Dict[str, Any]:
        """Calculate summary statistics for a collection of chunks."""
        if not chunks:
            return {"total_chunks": 0, "avg_char_length": 0, "min_char_length": 0, "max_char_length": 0}

        lengths = [len(c.page_content) for c in chunks]
        return {
            "total_chunks": len(chunks),
            "avg_char_length": round(sum(lengths) / len(lengths), 1),
            "min_char_length": min(lengths),
            "max_char_length": max(lengths),
        }
