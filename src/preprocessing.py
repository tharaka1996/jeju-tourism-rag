"""
Text Preprocessing module for Jeju Tourism RAG system.
Cleans and normalizes extracted text from PDF and TXT files.
"""
import re
import unicodedata
from typing import List


class TextPreprocessor:
    """Preprocesses raw text extracted from documents."""

    @staticmethod
    def normalize_unicode(text: str) -> str:
        """Normalize Unicode characters to standard NFKC representation."""
        if not text:
            return ""
        return unicodedata.normalize("NFKC", text)

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean text by removing excessive whitespace, trailing dashes from line wraps,
        and standardizing line endings while preserving paragraph boundaries.
        """
        if not text:
            return ""

        # Normalize unicode
        text = unicodedata.normalize("NFKC", text)

        # Standardize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Replace non-breaking spaces and unusual whitespace
        text = text.replace("\u00a0", " ").replace("\u200b", "").replace("\ufeff", "")

        # Fix hyphenated words broken across line breaks (e.g., "infor-\nmation" -> "information")
        text = re.sub(r"(\b[A-Za-z]+)-\n([A-Za-z]+\b)", r"\1\2", text)

        # Replace horizontal tabs and multiple consecutive spaces with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Collapse 3 or more consecutive newlines into 2 (preserving clean paragraphs)
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    @staticmethod
    def filter_short_lines(text: str, min_chars: int = 5) -> str:
        """Filter out stray short lines or page artifacts."""
        lines = text.split("\n")
        cleaned_lines = [line.strip() for line in lines if len(line.strip()) >= min_chars or line.strip() == ""]
        return "\n".join(cleaned_lines)
