"""
Embedding Manager module for Jeju Tourism RAG system.
Wraps Sentence Transformers (all-MiniLM-L6-v2) for local, fast, 384-dimensional dense embeddings.
Compatible with LangChain Embeddings interface.
"""
import logging
from typing import List
from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer
from config.settings import settings

logger = logging.getLogger(__name__)


class EmbeddingManager(Embeddings):
    """Manages local Sentence-Transformers embeddings for chunks and queries."""

    _instance = None
    _model = None

    def __new__(cls, *args, **kwargs):
        """Singleton pattern to avoid re-loading the embedding model multiple times in memory."""
        if cls._instance is None:
            cls._instance = super(EmbeddingManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, model_name: str = None):
        if self._model is None:
            self.model_name = model_name or settings.EMBEDDING_MODEL_NAME
            logger.info(f"Loading embedding model: '{self.model_name}' on local device...")
            try:
                self._model = SentenceTransformer(self.model_name)
                logger.info(f"Embedding model '{self.model_name}' loaded successfully. Dimension: {self.get_embedding_dimension()}")
            except Exception as e:
                logger.error(f"Failed to load SentenceTransformer model '{self.model_name}': {e}")
                raise RuntimeError(f"Could not initialize embedding model: {e}")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of document chunk texts into 384-dimensional vectors."""
        if not texts:
            return []
        embeddings = self._model.encode(
            texts,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """Embed a single query text into a normalized vector."""
        if not text.strip():
            return [0.0] * self.get_embedding_dimension()
        embedding = self._model.encode(
            text,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return embedding.tolist()

    def get_embedding_dimension(self) -> int:
        """Return embedding vector length (384 for all-MiniLM-L6-v2)."""
        if self._model is not None:
            return self._model.get_sentence_embedding_dimension()
        return settings.EMBEDDING_DIMENSION
