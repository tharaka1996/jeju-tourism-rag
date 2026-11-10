"""Configuration package for Jeju Tourism RAG system."""
try:
    from config.settings import settings
except ImportError:
    from .settings import settings

__all__ = ["settings"]
