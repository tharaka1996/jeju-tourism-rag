# System Architecture & Technical Specification: Jeju Tourism AI Assistant

**Author:** Master's Student in MIS, Jeju National University  
**Course:** Project for Implementing RAG Applications System (Assignment 01)  
**Academic Reference:** Week 10 Lecture Framework (`RAG-Framework(Week10).pptx`)

---

## 1. Architectural Philosophy and Framework Overview

Retrieval-Augmented Generation (RAG) combines dense semantic retrieval with prompt-driven language generation. As formulated in the course curriculum, general Large Language Models (LLMs) suffer from three critical shortcomings in domain-specific tasks:
1. **Knowledge Cutoffs**: Parametric weights cannot capture recent developments or proprietary regional schedules.
2. **Hallucination Risk**: When uncertain, generative decoders produce plausible but factually erroneous claims.
3. **Lack of Source Grounding**: Standard generative outputs lack deterministic document and page citations.

The **Jeju Tourism AI Assistant** resolves these limitations through a dual-pipeline architecture:
- **Pipeline A: Document Ingestion & Indexing Pipeline (Offline/Batch Processing)**
- **Pipeline B: Query Answering & Verification Pipeline (Real-Time Online Processing)**

```
+----------------------------------------------------------------------------------------------------+
|                                 1. DOCUMENT INGESTION PIPELINE (Offline)                           |
|                                                                                                    |
|  [PDF / TXT Documents]                                                                             |
|          |                                                                                         |
|          v                                                                                         |
|  [DocumentLoader] -------> [TextPreprocessor] --------> [Context-Enriched Chunker]                |
|  (Extract text & metadata) (Normalize Unicode & spaces) (chunk_size=750, overlap=75)               |
|                                                                    |                               |
|                                                                    v                               |
|                                                    [Sentence-Transformers (384-d)]                 |
|                                                                    |                               |
|                                                                    v                               |
|                                                    [(Persistent ChromaDB Collection)]              |
+----------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------+
|                                  2. QUERY ANSWERING PIPELINE (Online)                              |
|                                                                                                    |
|  [User Question (Natural Language)]                                                                |
|          |                                                                                         |
|          v                                                                                         |
|  [Query Embedding (all-MiniLM-L6-v2)]                                                              |
|          |                                                                                         |
|          v                                                                                         |
|  [ChromaDB Cosine Metric Search (Top-K=3)] <--- [Persistent ChromaDB Collection]                   |
|          |                                                                                         |
|          v                                                                                         |
|  [Context Formatting & Similarity Scoring]                                                         |
|          |                                                                                         |
|          v                                                                                         |
|  [LangChain LCEL Prompt Orchestration]                                                             |
|  (ChatPromptTemplate with Strict Grounding Rules)                                                  |
|          |                                                                                         |
|          v                                                                                         |
|  [LLM Generation Engine (Ollama / OpenAI / Local Grounded Generator)]                              |
|          |                                                                                         |
|          v                                                                                         |
|  [Verified Grounded Answer with Source Citations]                                                  |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Mathematical Formulations

### 2.1 Dense Embedding & Cosine Similarity
Given a document chunk $c_i \in C$ and a user query $q$, the embedding function $f_\theta: \mathcal{T} \to \mathbb{R}^d$ maps text to a $d=384$ dimensional hypersphere where $\|f_\theta(x)\|_2 = 1$.

The semantic similarity score $S(q, c_i)$ is computed via the inner product of normalized vectors:
$$\text{Sim}(q, c_i) = \frac{f_\theta(q) \cdot f_\theta(c_i)}{\|f_\theta(q)\|_2 \|f_\theta(c_i)\|_2} = \sum_{j=1}^{384} q_j \cdot c_{i,j}$$

ChromaDB internal cosine distance is defined as:
$$D_{\text{cosine}}(q, c_i) = 1 - \text{Sim}(q, c_i)$$

Our retrieval engine converts distance back to similarity score bounded in $[0.0, 1.0]$:
$$S(q, c_i) = \max\left(0.0, \min\left(1.0, 1.0 - D_{\text{cosine}}(q, c_i)\right)\right)$$

### 2.2 Top-$k$ Ranking & Thresholding
For a query $q$ and collection of $N$ indexed chunks, the retrieval set $\mathcal{R}_k(q)$ is defined as:
$$\mathcal{R}_k(q) = \text{argtop}_{c_i \in C}^{(k)} S(q, c_i)$$

Subject to the confidence threshold $\tau = 0.35$:
$$\mathcal{R}_{k, \tau}(q) = \{ c_i \in \mathcal{R}_k(q) \mid S(q, c_i) \ge \tau \}$$

If $\mathcal{R}_{k, \tau}(q) = \emptyset$, the query is classified as **out-of-domain / unanswerable**, triggering the deterministic refusal handler.

---

## 3. Detailed Component Architecture

### 3.1 Document Loader (`src/document_loader.py`)
- **PyPDF Engine**: Ingests multi-page official tourism documents, extracting text page-by-page.
- **TXT Ingestion**: Handles UTF-8 and Latin-1 text files.
- **Metadata Encapsulation**: Retains `filename`, `source`, `file_type`, `page`, `total_pages`, and character count.

### 3.2 Preprocessor (`src/preprocessing.py`)
- Normalizes Unicode to standard NFKC representation.
- Merges hyphenated words broken across line wraps.
- Collapses redundant whitespace and formatting noise while maintaining structural paragraph boundaries.

### 3.3 Context-Enriched Chunker (`src/chunking.py`)
- **Recursive Splitting**: Uses LangChain's `RecursiveCharacterTextSplitter` with hierarchical separators `["\n\n", "\n", ". ", " "]`.
- **Optimal Hyperparameters**: `chunk_size = 750` characters, `chunk_overlap = 75` characters.
- **Context-Aware Title Enrichment**: Prepends `[Document Title - Page N]` to each chunk to retain topical grounding for dense embeddings across isolated list items.
- **Deduplication Hashing**: Computes deterministic SHA-256 chunk hash for duplicate detection.

### 3.4 Vector Database (`src/vector_database.py`)
- **ChromaDB Integration**: Persistent disk storage at `./vectorstore` using SQLite and HNSW indexing.
- **Deduplication Engine**: Queries existing IDs before insertion; skips redundant chunks.
- **Collection Introspection**: Exposes real-time collection metrics (total chunks, unique sources, dimensionality).

### 3.5 Retrieval Engine (`src/retrieval.py`)
- Embeds user query and computes cosine similarity against candidate chunks.
- Formats context block with explicit citation tags `[Source i | Document: ... | Page: ... | Score: ...]`.
- Records retrieval latency in milliseconds.

### 3.6 LangChain Generation Pipeline (`src/generation.py`)
- Employs **LangChain Expression Language (LCEL)**:
  $$\text{Pipeline} = \text{RunnableLambda}(\text{retrieve}) \mid \text{Prompt} \mid \text{LLM} \mid \text{StrOutputParser}$$
- **Strict Grounding System Prompt**: Mandates answering solely from retrieved passages and explicitly refusing queries lacking supporting documentation.
- **Multi-Provider Architecture**:
  1. *Local Grounded Generator*: 100% offline, free, deterministic synthesis engine.
  2. *Local Ollama*: Invokes locally hosted models (`llama3:8b`, `mistral`).
  3. *OpenAI API*: Configurable via `.env` (`gpt-4o-mini`).

### 3.7 Evaluation Suite (`src/evaluation.py`)
- Automated benchmark against 22 academic test queries.
- Computes:
  - $\text{Precision@}k = \frac{|\mathcal{R}_k \cap \mathcal{T}|}{k}$
  - $\text{Recall@}k = \frac{|\text{Unique Target Docs in } \mathcal{R}_k|}{|\text{Total Target Docs}|}$
  - $\text{Context Faithfulness} = \frac{|\text{Answer Claim Words in Context}|}{|\text{Answer Words}|}$
  - $\text{Answer Relevance} = \frac{|\text{Key Ground Truth Entities in Answer}|}{|\text{Key Entities}|}$
- Exports CSV results and Matplotlib figures.

### 3.8 Streamlit Dashboard (`app.py`)
- Clean, multi-tab interface:
  1. Home / Dashboard
  2. Document Management (Upload & Indexing)
  3. AI Chat Assistant (Natural Language Q&A with Citations)
  4. Retrieval Inspector (Raw Vector Search Debugger)
  5. Evaluation & Analytics (Live Benchmarking & Visualizations)
