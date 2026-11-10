"""
Configuration settings for the Jeju Tourism AI Assistant RAG Application.
Loads environment variables from .env if present, otherwise provides reliable defaults.
"""
import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

# Base Directory of the Project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file if it exists
load_dotenv(BASE_DIR / ".env")


@dataclass
class Settings:
    # Project Identity
    PROJECT_NAME: str = "Jeju Tourism AI Assistant"
    PROJECT_SUBTITLE: str = "A Retrieval-Augmented Generation System for Jeju Island Tourism"
    UNIVERSITY: str = "Jeju National University"
    DEPARTMENT: str = "Department of Management Information Systems (MIS)"
    COURSE: str = "Project for Implementing RAG Applications System"
    VERSION: str = "1.0.0"

    # Directory Paths
    BASE_DIR: Path = BASE_DIR
    DATA_DIR: Path = BASE_DIR / "data"
    DOCS_DIR: Path = BASE_DIR / "data" / "documents"
    EVAL_DIR: Path = BASE_DIR / "data" / "evaluation"
    VECTORSTORE_DIR: Path = BASE_DIR / "vectorstore"
    REPORTS_DIR: Path = BASE_DIR / "reports"
    FIGURES_DIR: Path = BASE_DIR / "reports" / "figures"
    RESULTS_DIR: Path = BASE_DIR / "reports" / "results"

    # ChromaDB Configuration
    CHROMA_PERSIST_DIR: str = os.getenv("CHROMA_PERSIST_DIRECTORY", str(BASE_DIR / "vectorstore"))
    COLLECTION_NAME: str = os.getenv("CHROMA_COLLECTION_NAME", "jeju_tourism_knowledge")

    # Embedding Model Settings
    # Sentence-Transformers all-MiniLM-L6-v2 (384-dimensional dense vectors)
    EMBEDDING_MODEL_NAME: str = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")
    EMBEDDING_DIMENSION: int = 384

    # Chunking Hyperparameters
    DEFAULT_CHUNK_SIZE: int = int(os.getenv("DEFAULT_CHUNK_SIZE", 750))
    DEFAULT_CHUNK_OVERLAP: int = int(os.getenv("DEFAULT_CHUNK_OVERLAP", 75))

    # Retrieval Hyperparameters
    DEFAULT_TOP_K: int = int(os.getenv("TOP_K_RETRIEVAL", 3))
    SIMILARITY_SCORE_THRESHOLD: float = float(os.getenv("SIMILARITY_SCORE_THRESHOLD", 0.35))

    # LLM Provider Configuration
    DEFAULT_LLM_PROVIDER: str = os.getenv("DEFAULT_LLM_PROVIDER", "local_fallback")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3:8b")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def ensure_directories(self) -> None:
        """Ensure all required directories exist."""
        for path in [
            self.DOCS_DIR,
            self.EVAL_DIR,
            self.VECTORSTORE_DIR,
            self.FIGURES_DIR,
            self.RESULTS_DIR,
        ]:
            path.mkdir(parents=True, exist_ok=True)


settings = Settings()
settings.ensure_directories()
