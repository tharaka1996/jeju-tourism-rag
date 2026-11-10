"""
Answer Generation module for Jeju Tourism RAG system.
Implements LangChain-based prompt templates, LCEL chain orchestration,
multi-provider LLM support (Ollama, OpenAI, Local Fallback),
strict context grounding, and source citation.
"""
import os
import re
import time
import logging
from typing import Dict, Any, List, Optional
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from config.settings import settings
from src.retrieval import RetrievalEngine

logger = logging.getLogger(__name__)

# Strict System Prompt as specified in the lecture slides & assignment
SYSTEM_PROMPT = """You are the 'Jeju Tourism AI Assistant', an expert academic tourism guide for Jeju Island.
You must adhere strictly to the following grounding rules:
1. Answer the question using ONLY the factual information provided in the RETRIEVED CONTEXT below.
2. If the answer cannot be found in the RETRIEVED CONTEXT, or if the context does not contain sufficient facts to answer the question, you MUST explicitly state:
   "I am sorry, but sufficient information is unavailable in the retrieved tourism documents to answer this question."
3. Do NOT invent, assume, extrapolate, or use outside training knowledge.
4. At the end of your answer, explicitly list the source documents and page numbers you cited.
5. Keep your tone informative, polite, professional, and clear.
"""

USER_PROMPT_TEMPLATE = """RETRIEVED CONTEXT:
{context}

USER QUESTION:
{question}

HELPFUL GROUNDED ANSWER:"""


class LocalGroundedGenerator:
    """
    An offline, deterministic grounded generator that synthesizes answers
    directly from retrieved passages without requiring external API keys or Ollama.
    Enforces strict grounding, source citation, and explicit rejection of unanswerable queries.
    """

    def __init__(self, score_threshold: float = 0.30):
        self.score_threshold = score_threshold

    def generate(self, question: str, retrieved_data: Dict[str, Any]) -> str:
        chunks = retrieved_data.get("chunks", [])
        is_sufficient = retrieved_data.get("is_sufficient", False)

        # Check if chunks are empty or top similarity score is below threshold
        if not chunks or (chunks and chunks[0]["similarity_score"] < self.score_threshold):
            return (
                "I am sorry, but sufficient information is unavailable in the retrieved "
                "tourism documents to answer this question. The current knowledge base contains "
                "official guides for Jeju Island tourism (Hallasan, Seongsan Ilchulbong, Manjanggul, "
                "Olle trails, beaches, transportation, culinary culture, and traveler safety)."
            )

        # Filter sentences in retrieved chunks that are semantically relevant to question keywords
        q_words = set(re.findall(r"\w+", question.lower()))
        # Remove common stop words
        stopwords = {
            "what", "is", "the", "of", "and", "in", "to", "for", "are", "do", "how", "many", "does",
            "which", "when", "where", "why", "who", "a", "an", "on", "with", "at", "by", "from",
            "about", "or", "as", "if", "that", "this", "can", "should", "you", "their", "its"
        }
        content_words = {w for w in q_words if w not in stopwords and len(w) > 2}

        # Check keyword overlap across all retrieved chunks
        all_text = " ".join([c["content"] for c in chunks]).lower()
        matching_words = [w for w in content_words if w in all_text]

        # If keyword match ratio is very low, treat as insufficient/out-of-domain
        if len(content_words) >= 2 and len(matching_words) == 0:
            return (
                "I am sorry, but sufficient information is unavailable in the retrieved "
                "tourism documents to answer this question. The provided documents do not contain "
                "information relevant to your query."
            )

        # Score paragraphs and sections within retrieved chunks
        scored_sections = []
        cited_sources = set()

        for chunk in chunks:
            chunk_content = chunk["content"]
            filename = chunk["filename"]
            page = chunk["page"]

            # Clean out the prepended title tag for readable answer presentation
            clean_chunk = re.sub(r"^\[.*?\]\n?", "", chunk_content).strip()

            # Split into semantic blocks (paragraphs or subsections)
            sections = [s.strip() for s in re.split(r"\n{2,}", clean_chunk) if s.strip()]
            if not sections:
                sections = [clean_chunk]

            for s in sections:
                s_words = set(re.findall(r"\w+", s.lower()))
                overlap = len(content_words.intersection(s_words))
                if overlap > 0:
                    scored_sections.append((overlap, s, filename, page))

        # Sort sections by keyword relevance
        scored_sections.sort(key=lambda x: x[0], reverse=True)

        if not scored_sections:
            # Fallback to the top chunk's cleaned text
            top_chunk = chunks[0]
            clean_text = re.sub(r"^\[.*?\]\n?", "", top_chunk["content"]).strip()
            answer_text = clean_text
            cited_sources.add(f"{top_chunk['filename']} (Page {top_chunk['page']})")
        else:
            # Select top non-redundant sections
            selected_sections = []
            seen_texts = set()
            for score, sec, fname, page in scored_sections:
                if sec not in seen_texts:
                    selected_sections.append(sec)
                    seen_texts.add(sec)
                    cited_sources.add(f"{fname} (Page {page})")
                if len(selected_sections) >= 2:
                    break
            answer_text = "\n\n".join(selected_sections)

        # Build final cited response
        citations = ", ".join(sorted(list(cited_sources)))
        formatted_answer = (
            f"{answer_text}\n\n"
            f"**Sources Consulted:** {citations}"
        )
        return formatted_answer


class RAGGenerationPipeline:
    """Orchestrates retrieval and generation using LangChain LCEL workflows."""

    def __init__(
        self,
        retrieval_engine: Optional[RetrievalEngine] = None,
        llm_provider: Optional[str] = None,
    ):
        self.retrieval_engine = retrieval_engine or RetrievalEngine()
        self.llm_provider = llm_provider or settings.DEFAULT_LLM_PROVIDER
        self.local_generator = LocalGroundedGenerator(score_threshold=settings.SIMILARITY_SCORE_THRESHOLD)

        # Build LangChain prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", USER_PROMPT_TEMPLATE),
        ])

        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        """Initialize the configured LLM backend."""
        provider = self.llm_provider.lower()

        if provider == "openai" and settings.OPENAI_API_KEY:
            try:
                from langchain_openai import ChatOpenAI
                logger.info(f"Using OpenAI LLM: {settings.OPENAI_MODEL}")
                return ChatOpenAI(
                    model=settings.OPENAI_MODEL,
                    api_key=settings.OPENAI_API_KEY,
                    temperature=0.1,
                )
            except Exception as e:
                logger.warning(f"Failed to load ChatOpenAI ({e}). Falling back to local generator.")
                return None

        elif provider == "ollama":
            try:
                from langchain_community.chat_models import ChatOllama
                logger.info(f"Using Ollama LLM: {settings.OLLAMA_MODEL} at {settings.OLLAMA_BASE_URL}")
                return ChatOllama(
                    base_url=settings.OLLAMA_BASE_URL,
                    model=settings.OLLAMA_MODEL,
                    temperature=0.1,
                )
            except Exception as e:
                logger.warning(f"Failed to load ChatOllama ({e}). Falling back to local generator.")
                return None

        logger.info("Using local grounded generation engine (100% offline, free).")
        return None

    def query(
        self,
        question: str,
        top_k: int = None,
        threshold: float = None,
    ) -> Dict[str, Any]:
        """
        Execute the end-to-end RAG pipeline:
        Query -> Retrieval -> Context Construction -> LLM Generation -> Output with Sources
        """
        start_total = time.perf_counter()

        # Step 1: Retrieval
        retrieval_result = self.retrieval_engine.retrieve(
            query=question,
            top_k=top_k,
            threshold=threshold,
        )

        # Step 2: Generation
        start_gen = time.perf_counter()
        answer = ""

        if self.llm is not None:
            try:
                # Modern LangChain LCEL chain
                chain = self.prompt | self.llm | StrOutputParser()
                answer = chain.invoke({
                    "context": retrieval_result["context_text"],
                    "question": question,
                })
            except Exception as e:
                logger.error(f"Error during LLM invocation ({e}). Using local grounded generator fallback.")
                answer = self.local_generator.generate(question, retrieval_result)
        else:
            answer = self.local_generator.generate(question, retrieval_result)

        gen_time = time.perf_counter() - start_gen
        total_time = time.perf_counter() - start_total

        return {
            "question": question,
            "answer": answer,
            "retrieved_chunks": retrieval_result["chunks"],
            "raw_chunks": retrieval_result["raw_chunks"],
            "context_text": retrieval_result["context_text"],
            "is_sufficient": retrieval_result["is_sufficient"],
            "llm_provider": self.llm_provider,
            "latency": {
                "retrieval_seconds": retrieval_result["latency_seconds"],
                "generation_seconds": round(gen_time, 4),
                "total_seconds": round(total_time, 4),
            },
        }
