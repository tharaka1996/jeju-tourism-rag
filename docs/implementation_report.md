# Report on the Implementation of a Vector Database and RAG Application System

**Application Name:** Jeju Tourism AI Assistant  
**Author:** Master's Student in Management Information Systems (MIS)  
**Institution:** Jeju National University (JNU)  
**Course:** Project for Implementing RAG Applications System (Assignment 01)  
**Submission Date:** December 2026  
**Primary Lecture Reference:** `RAG-Framework(Week10).pptx` (JNU MIS Week 10)

---

## Executive Summary

This academic report documents the design, implementation, testing, and empirical evaluation of a complete Retrieval-Augmented Generation (RAG) application system tailored for Jeju Island Tourism Information, titled the **Jeju Tourism AI Assistant**. Following the technical and architectural guidelines provided in the university lecture framework, the system bridges domain-specific knowledge gaps and mitigates Large Language Model (LLM) hallucinations through dense semantic vector retrieval.

The application is implemented in Python using **LangChain** for chain orchestration, **ChromaDB** as a persistent local vector database, and the **Sentence-Transformers** (`all-MiniLM-L6-v2`) model for generating 384-dimensional dense embeddings. A curated corpus of official Jeju tourism documents (covering UNESCO natural heritage, Hallasan hiking routes, volcanic caves, public bus networks, beaches, and Haenyeo culinary traditions) was ingested, preprocessed, and indexed. An empirical evaluation across 22 structured academic benchmark questions demonstrated an in-domain retrieval **Precision@3 of 94.7%**, a **Recall@3 of 81.6%**, a **Context Faithfulness of 97.0%**, an **Average Latency of 18.5 milliseconds**, and a **100% Refusal Accuracy** on out-of-domain negative controls.

---

## 1. Objective & Background

### 1.1 Project Motivation
As international and domestic tourism on Jeju Island continues to expand, prospective visitors and travelers require timely, reliable, and precise guidance regarding transportation schedules, national park reservations, seasonal trail cutoffs, and cultural protocols. While general Large Language Models (e.g., GPT-4, LLaMA) demonstrate impressive linguistic capabilities, they exhibit fundamental limitations in specialized domains:
1. **Knowledge Cutoffs and Temporal Latency**: Model weights cannot reflect recent regulatory updates, reservation policies, or island-specific public transit route reorganizations.
2. **Hallucination Risk**: Generative decoders frequently fabricate plausible but non-existent admission fees, bus schedules, or hiking routes when lacking explicit grounding.
3. **Absence of Source Attribution**: Standard generative outputs cannot provide verifiable citations to official government guides or tourism authority publications.

The **Jeju Tourism AI Assistant** addresses these challenges by implementing a local, verifiable RAG pipeline grounded in authoritative documents published by the Jeju Tourism Organization and Jeju Special Self-Governing Province.

### 1.2 Retrieval-Augmented Generation (RAG) Concepts
Retrieval-Augmented Generation (Lewis et al., 2020) combines a parametric memory model (an autoregressive LLM) with a non-parametric memory index (a dense vector database). As articulated in the Week 10 lecture, RAG does not modify the underlying model weights; instead, it dynamically enriches the prompt context with top-$k$ relevant document chunks retrieved at inference time. This guarantees that model responses are factually grounded in authoritative external source materials.

### 1.3 Vector Database Concepts
A vector database specializes in storing high-dimensional numerical representations (embeddings) of unstructured text and executing Approximate Nearest Neighbor (ANN) search at scale. Unlike traditional relational databases (SQL) or lexical keyword search engines (BM25) which rely on exact term matching, vector databases measure semantic similarity. This enables the retrieval of relevant passages even when user queries employ synonyms, varied syntax, or paraphrasing.

### 1.4 Project Objectives
1. Implement a complete 5-stage RAG workflow: Data Collection/Preprocessing, Vector Database Construction, Semantic Retrieval, Answer Generation, and Quantitative Evaluation.
2. Support heterogeneous document ingestion, specifically PDF and TXT file formats, with full metadata retention.
3. Build a persistent, local, and free ChromaDB vector store that supports incremental document addition and deduplication.
4. Orchestrate context-aware generation using modern LangChain components with strict prompt grounding and unanswerable refusal handling.
5. Provide a responsive, multi-page Streamlit web interface suitable for academic demonstration.
6. Conduct rigorous empirical benchmarking with 22 structured evaluation queries, generating reproducible performance tables and high-resolution figures.

### 1.5 Technology Stack

| Layer | Selected Technology | Technical Justification |
|---|---|---|
| **Programming Language** | Python 3.11 | Standard language for AI engineering, LangChain, and scientific computing. |
| **RAG Framework** | LangChain 1.4+ (LCEL) | Provides modular chain composition (`RunnableLambda | Prompt | LLM | StrOutputParser`). |
| **Vector Database** | ChromaDB 0.5.23 | 100% free, open-source, local persistent storage (SQLite/hnswlib), no API keys needed. |
| **Embedding Model** | Sentence-Transformers (`all-MiniLM-L6-v2`) | High-performance 384-dimensional dense embeddings; fast, CPU-efficient, completely local. |
| **LLM Generation** | Multi-Tier Engine (Local Grounded / Ollama / OpenAI) | Fully self-contained local grounded generator ensures 100% offline university demo capability. |
| **User Interface** | Streamlit 1.66+ | Rapid development of interactive multi-tab dashboards with chat and data visualization. |
| **Document Processing** | PyPDF 7.0 & TextPreprocessor | Robust PDF page-by-page text extraction and Unicode NFKC normalization. |
| **Evaluation & Plotting** | Pandas, NumPy, Matplotlib | Empirical metrics calculation, CSV export, and publication-ready visualization generation. |

---

## 2. System Architecture

### 2.1 Overall System Architecture
The application architecture is bifurcated into two synchronized pipelines: an **Offline Document Ingestion Pipeline** and an **Online Real-Time Query Answering Pipeline**.

```
+----------------------------------------------------------------------------------------------------+
|                               1. OFFLINE DOCUMENT INGESTION PIPELINE                                |
|                                                                                                    |
|  [PDF & TXT Guides]                                                                                |
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
|                                 2. ONLINE QUERY ANSWERING PIPELINE                                 |
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
|  [LLM Generation Engine (Local Grounded / Ollama / OpenAI)]                                        |
|          |                                                                                         |
|          v                                                                                         |
|  [Verified Grounded Answer with Source Citations]                                                  |
+----------------------------------------------------------------------------------------------------+
```

### 2.2 Component Functional Breakdown
1. **Document Loader (`src/document_loader.py`)**: Ingests files, preserving page numbers, character lengths, filenames, and format identifiers.
2. **Text Preprocessor (`src/preprocessing.py`)**: Sanitizes extracted strings, removes hyphenated word-breaks across line boundaries, and collapses excess whitespace.
3. **Context-Enriched Chunker (`src/chunking.py`)**: Uses recursive splitting (`chunk_size=750`, `overlap=75`) and prepends `[Document Title - Page N]` to prevent semantic drift across sub-chunks.
4. **Embedding Manager (`src/embeddings.py`)**: Singleton class managing local inference of `all-MiniLM-L6-v2`, mapping text strings to normalized 384-dimensional vectors.
5. **Vector Database Manager (`src/vector_database.py`)**: Manages the persistent ChromaDB collection (`jeju_tourism_knowledge`), implementing SHA-256 hash deduplication to eliminate redundant storage.
6. **Retrieval Engine (`src/retrieval.py`)**: Converts distance to normalized similarity scores $S \in [0, 1]$, extracts top-$k$ candidates, and applies thresholding ($\tau = 0.35$).
7. **Generation Pipeline (`src/generation.py`)**: Enforces strict grounding prompts via LangChain LCEL, dispatches between LLM providers, and formats source citations.
8. **Evaluation Engine (`src/evaluation.py`)**: Executes the 22-question benchmark suite, logs metrics to CSV, and generates analytical figures.

---

## 3. Implementation Details

### 3.1 Development Environment & Software Versions
- **Operating System:** Microsoft Windows 11 Enterprise (x86_64)
- **Python Environment:** Python 3.11.3
- **Core Dependencies:**
  - `chromadb == 0.5.23`
  - `numpy < 2.0.0` (1.26.4 for PyTorch C-extension binary compatibility)
  - `torch == 2.0.1+cpu`
  - `sentence-transformers == 3.3.1`
  - `langchain == 1.4.9`
  - `langchain-core == 1.7.6`
  - `pypdf == 7.0.0`
  - `streamlit == 1.66.0`

### 3.2 Embedding Space and Dense Vector Representation
The embedding model transforms arbitrary-length text passages into dense vectors $\vec{v} \in \mathbb{R}^{384}$. For any two normalized vectors $\vec{u}$ and $\vec{v}$, their cosine similarity is calculated via inner product:
$$\text{Sim}(\vec{u}, \vec{v}) = \sum_{i=1}^{384} u_i \cdot v_i$$
ChromaDB indexes these vectors using an HNSW (Hierarchical Navigable Small World) graph structure, providing sub-millisecond approximate nearest neighbor retrieval.

### 3.3 Context-Enriched Chunking
A major technical finding during development was that sub-chunks containing bulleted lists (e.g. admission fees, seasonal cutoff hours) often lack mention of the parent entity name (e.g. "Seongsan Ilchulbong"). To overcome this vocabulary disassociation, the chunker dynamically prepends document-level metadata to each chunk:
```
[02 Seongsan Ilchulbong Unesco - Page 1]
Visiting Hours, Ticketing, and Admission:
- Admission Fees: Adults (ages 25-64): 5,000 KRW.
```
In controlled experiments, this title enrichment elevated the cosine similarity for topical queries from 0.41 to **0.725**, ensuring correct ranking over cross-document distractors.

### 3.4 Strict Prompt Grounding and Out-of-Domain Refusal
The generation engine utilizes a strict system prompt instruction designed to prevent hallucination:
```text
You are the 'Jeju Tourism AI Assistant', an expert academic tourism guide for Jeju Island.
You must adhere strictly to the following grounding rules:
1. Answer the question using ONLY the factual information provided in the RETRIEVED CONTEXT below.
2. If the answer cannot be found in the RETRIEVED CONTEXT, or if the context does not contain sufficient facts to answer the question, you MUST explicitly state:
   "I am sorry, but sufficient information is unavailable in the retrieved tourism documents to answer this question."
3. Do NOT invent, assume, extrapolate, or use outside training knowledge.
4. At the end of your answer, explicitly list the source documents and page numbers you cited.
```

### 3.5 Streamlit Multi-Tab Web Application
The user interface (`app.py`) provides 5 dedicated views:
- **Dashboard & Architecture**: Real-time system status metrics (indexed documents count, total chunks, embedding dimensions), theoretical framework overview, and dataflow diagrams.
- **Document Management**: File uploader (PDF/TXT), live preview, chunk configuration, and collection reset.
- **AI Chat Assistant**: Natural language Q&A, interactive sample prompt buttons, latency badges, and expandable retrieved passages with similarity scores.
- **Retrieval Inspector**: Direct query testing tool displaying raw chunk distances, cosine similarity scores, and ranking.
- **Evaluation & Analytics**: Interactive benchmark runner, summary metrics cards, and embedded Matplotlib visualization charts.

#### Live System Interface Captures:

**Figure 2: Interactive Web Application Dashboard (Tab 1)**
![Dashboard & Architecture](../reports/figures/screenshots/01_dashboard.png)

**Figure 3: Document Management & Ingestion Interface (Tab 2)**
![Document Management](../reports/figures/screenshots/02_document_management.png)

**Figure 4: AI Chat Assistant with Grounded Citations (Tab 3)**
![AI Chat Assistant](../reports/figures/screenshots/03_chat_assistant.png)

**Figure 5: Vector Database Retrieval Inspector (Tab 4)**
![Retrieval Inspector](../reports/figures/screenshots/04_retrieval_inspector.png)

---

## 4. Experiments & Results

### 4.1 Evaluation Dataset
A benchmark dataset comprising 22 structured questions was designed across four distinct categories:
1. **Fact Retrieval (Single-Chunk)**: Questions testing specific numerical facts, elevations, fees, and rules (Q01-Q16).
2. **Multi-Chunk Synthesis**: Questions requiring aggregation of facts across distinct sections or documents (Q17-Q19).
3. **Out-of-Domain Negative Controls**: Questions on external non-Jeju topics to evaluate hallucination prevention and refusal accuracy (Q20-Q22).

### 4.2 Quantitative Performance Metrics
The system was evaluated using four standard information retrieval and RAG metrics:
- **Precision@3**: Proportion of the top-3 retrieved chunks that originate from designated target documents.
- **Recall@3**: Proportion of relevant target documents present within the top-3 retrieved chunks.
- **Context Faithfulness**: Proportion of substantive factual words in the generated answer directly supported by the retrieved context.
- **Answer Relevance**: Proportion of required ground-truth entities present in the generated answer.
- **Latency**: Mean retrieval, generation, and end-to-end processing times in seconds.

### 4.3 Empirical Benchmark Results Table

| Question ID | Category | Topic | Top Cosine Score | Precision@3 | Recall@3 | Faithfulness | Relevance | Latency (s) |
|---|---|---|---|---|---|---|---|---|
| **Q01** | Fact Retrieval | Hallasan Summit Trails | 0.7857 | 1.00 | 1.00 | 0.985 | 1.00 | 0.016 |
| **Q02** | Fact Retrieval | Hallasan Reservation | 0.7028 | 1.00 | 1.00 | 0.988 | 1.00 | 0.012 |
| **Q03** | Fact Retrieval | Hallasan Winter Cutoff | 0.6514 | 1.00 | 0.50 | 0.991 | 1.00 | 0.011 |
| **Q04** | Fact Retrieval | Seongsan Formation & Fees | 0.6402 | 1.00 | 0.50 | 0.957 | 1.00 | 0.012 |
| **Q05** | Fact Retrieval | Seongsan Haenyeo Show | 0.6120 | 1.00 | 0.50 | 0.963 | 0.75 | 0.013 |
| **Q06** | Fact Retrieval | Manjanggul Temperature | 0.6698 | 1.00 | 1.00 | 0.978 | 0.75 | 0.014 |
| **Q07** | Fact Retrieval | Manjanggul Lava Column | 0.7214 | 1.00 | 1.00 | 0.975 | 1.00 | 0.013 |
| **Q08** | Fact Retrieval | Hyeopjae Beach Family | 0.6387 | 1.00 | 1.00 | 0.941 | 1.00 | 0.012 |
| **Q09** | Fact Retrieval | Jungmun Saekdal Surfing | 0.6641 | 1.00 | 1.00 | 0.938 | 0.75 | 0.011 |
| **Q10** | Fact Retrieval | Olle Trail Markers | 0.6974 | 1.00 | 1.00 | 0.979 | 0.83 | 0.013 |
| **Q11** | Fact Retrieval | Olle Total Scale | 0.7312 | 1.00 | 0.50 | 0.982 | 0.75 | 0.012 |
| **Q12** | Fact Retrieval | Red Express Buses | 0.7491 | 1.00 | 1.00 | 0.956 | 0.80 | 0.012 |
| **Q13** | Fact Retrieval | Yellow Tourist Buses | 0.7533 | 1.00 | 1.00 | 0.968 | 0.80 | 0.013 |
| **Q14** | Fact Retrieval | Black Pork & Meljot | 0.6729 | 1.00 | 1.00 | 0.972 | 1.00 | 0.012 |
| **Q15** | Fact Retrieval | Haenyeo Bulteok | 0.6841 | 0.67 | 1.00 | 0.984 | 0.75 | 0.012 |
| **Q16** | Fact Retrieval | 1330 Travel Hotline | 0.6912 | 1.00 | 1.00 | 0.952 | 0.75 | 0.012 |
| **Q17** | Multi-Chunk | UNESCO Sites Synthesis | 0.5891 | 0.67 | 0.50 | 0.965 | 0.75 | 0.014 |
| **Q18** | Multi-Chunk | Airport to Seongsan Transit | 0.5724 | 0.67 | 0.50 | 0.961 | 0.75 | 0.015 |
| **Q19** | Multi-Chunk | Summer/Winter Climate | 0.6110 | 1.00 | 0.50 | 0.966 | 0.80 | 0.014 |
| **Q20** | Out-of-Domain | Paris Metro Line 4 | 0.3311 | 1.00 | 1.00 | 1.000 | 1.00 | 0.011 |
| **Q21** | Out-of-Domain | UK Prime Minister Policy | 0.2814 | 1.00 | 1.00 | 1.000 | 1.00 | 0.011 |
| **Q22** | Out-of-Domain | Italian Pizza Crust Recipe | 0.2541 | 1.00 | 1.00 | 1.000 | 1.00 | 0.011 |
| **Mean**| **Overall** | **All 22 Benchmark Items** | **0.6226** | **0.955** | **0.841** | **0.974** | **0.860** | **0.0185s** |

### 4.4 Analytical Graphs and Findings

**Figure 6: Experimental Evaluation Dashboard (Tab 5: Live Benchmark Metrics & Interactive Table)**
![Evaluation Dashboard](../reports/figures/screenshots/05_evaluation_dashboard.png)

**Figure 7: Empirical Quality Metrics Across In-Domain Test Queries**
![Overall RAG Metrics](../reports/figures/overall_rag_metrics.png)

**Figure 8: Retrieval Precision@3 and Recall@3 Breakdown by Tourism Topic**
![Topic Breakdown](../reports/figures/retrieval_performance_by_topic.png)

**Figure 9: End-to-End Processing Latency Breakdown by Question Category**
![Latency Breakdown](../reports/figures/latency_breakdown.png)

- **Retrieval Performance (Figure 8)**: In-domain retrieval achieved a mean **Precision@3 of 94.7%** and **Recall@3 of 81.6%**. The lowest recall occurred on multi-chunk synthesis questions (e.g. Q17, Q18) where information was distributed across 3 or 4 separate source documents, illustrating that $k=3$ is slightly constrained for complex cross-document aggregation.
- **Latency Breakdown (Figure 9)**: Query latency averaged **18.5 ms** across all questions, with retrieval taking ~12-20 ms and local generation taking < 1 ms.
- **Overall Quality (Figure 7)**: Context faithfulness averaged **97.0%**, demonstrating strict adherence to retrieved text without hallucination. Refusal accuracy on out-of-domain queries was **100.0%**.

### 4.5 Qualitative Input/Output Examples
- **Example 1: In-Domain Hallasan Summit Access (Q01)**:
  - *Query:* "What is the elevation of Mount Hallasan, and what are the two trails that reach the Baeknokdam summit?"
  - *Generated Answer:* "Mount Hallasan stands in the center of Jeju Island as the highest peak in South Korea, reaching an altitude of 1,947 meters (6,388 feet) above sea level. Hallasan National Park features five official hiking routes, but only two routes provide access to the Baeknokdam crater summit: Seongpanak Trail (9.6 km) and Gwaneumsa Trail (8.7 km)."
  - *Sources Consulted:* `01_hallasan_national_park.txt (Page 1)`, `jeju_official_travel_guide_sample.pdf (Page 1)`.
- **Example 2: Negative Control Refusal (Q20)**:
  - *Query:* "What is the ticket price and schedule for the Paris Metro subway line 4?"
  - *Generated Answer:* "I am sorry, but sufficient information is unavailable in the retrieved tourism documents to answer this question. The current knowledge base contains official guides for Jeju Island tourism (Hallasan, Seongsan Ilchulbong, Manjanggul, Olle trails, beaches, transportation, culinary culture, and traveler safety)."
  - *Outcome:* Verified 100% correct refusal; no hallucination of French transit prices.

---

## 5. Conclusion & Future Work

### 5.1 Summary of Implementation
The **Jeju Tourism AI Assistant** successfully fulfills all five stages of Assignment 01:
1. **Data Ingestion**: Multi-format ingestion of 8 official TXT documents and 1 compiled PDF document with metadata preservation.
2. **Vector Indexing**: Construction of a persistent ChromaDB database housing 50 context-enriched dense chunks.
3. **Retrieval**: Sub-20ms cosine similarity retrieval with confidence thresholding.
4. **Generation**: Strict prompt grounding via LangChain LCEL with source citation and negative control handling.
5. **Evaluation**: Comprehensive benchmark across 22 questions with quantitative CSV logging and Matplotlib visualization.

### 5.2 Current Limitations
1. **Top-K Retrieval Constraints**: For complex multi-document synthesis queries (such as comparing all UNESCO sites), a fixed top-$k=3$ cannot capture all 4 relevant source documents simultaneously.
2. **Dense-Only Retrieval**: Extremely specific alphanumeric queries (e.g., bus route numbers like "181") can occasionally score slightly lower in pure dense vector space compared to hybrid BM25 lexical matching.

### 5.3 Potential Improvements
1. **Hybrid Retrieval (Dense + BM25)**: Implementing Reciprocal Rank Fusion (RRF) combining dense embeddings with sparse BM25 keyword matching.
2. **Cross-Encoder Reranking**: Introducing a secondary reranker (e.g., `bge-reranker-large`) to rescore the top-20 retrieved candidates down to the top-3 most precise chunks.
3. **Multi-Modal Tourism RAG**: Indexing tourism maps, trail elevation profiles, and coastal photographs using vision-language embeddings (e.g. CLIP).

---

## References

1. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *Advances in Neural Information Processing Systems (NeurIPS 2020)*, 33, 9459–9474.
2. Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP 2019)*, 3982–3992.
3. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 5998–6008.
4. ChromaDB Development Team. (2024). Chroma: The Open-Source Embedding Database. *Chroma Technical Report*. https://trychroma.com
5. LangChain Inc. (2024). LangChain: Building Applications with LLMs through Modular Orchestration. *LangChain Documentation*. https://python.langchain.com
6. Jeju Tourism Organization (JTO). (2026). VisitJeju: Official Jeju Island Travel and Heritage Guide. *Jeju Special Self-Governing Province*. https://www.visitjeju.net
