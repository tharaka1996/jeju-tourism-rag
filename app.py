"""
Jeju Tourism AI Assistant - Streamlit Web Application
A comprehensive Retrieval-Augmented Generation (RAG) system for Jeju Island Tourism.
Assignment 01 - Master of Management Information Systems (MIS), Jeju National University.
"""
# Linux SQLite override for ChromaDB on Streamlit Cloud
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

import os
import sys
import time
from pathlib import Path

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import streamlit as st
import pandas as pd

from config.settings import settings
from src.document_loader import DocumentLoader
from src.chunking import DocumentChunker
from src.vector_database import VectorDatabaseManager
from src.retrieval import RetrievalEngine
from src.generation import RAGGenerationPipeline
from src.evaluation import RAGEvaluator

# Page Configuration
st.set_page_config(
    page_title="Jeju Tourism AI Assistant (RAG)",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0F4C81;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #555555;
        margin-bottom: 1.2rem;
    }
    .metric-card {
        background-color: #F8F9FA;
        border-left: 4px solid #0F4C81;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .citation-box {
        background-color: #EEF4FA;
        border-left: 3px solid #2E5B88;
        padding: 10px 14px;
        border-radius: 4px;
        font-size: 0.9rem;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_vector_db():
    """Cache vector database connection and auto-index default corpus if empty."""
    vdb = VectorDatabaseManager()
    if vdb.collection.count() == 0:
        loader = DocumentLoader()
        docs = loader.load_directory(settings.DOCS_DIR)
        if docs:
            vdb.index_documents(docs, chunk_size=500, chunk_overlap=50)
    return vdb


@st.cache_resource
def get_rag_pipeline(llm_provider: str):
    """Cache RAG pipeline instance."""
    vdb = get_vector_db()
    retrieval = RetrievalEngine(vector_db=vdb)
    return RAGGenerationPipeline(retrieval_engine=retrieval, llm_provider=llm_provider)


# Sidebar Configuration
st.sidebar.image("https://images.unsplash.com/photo-1578637387939-43c525550085?auto=format&fit=crop&w=600&q=80", caption="Jeju Island - UNESCO World Heritage")
st.sidebar.title("🏝️ System Controls")

llm_choice = st.sidebar.selectbox(
    "Active LLM Engine",
    options=["local_fallback", "ollama", "openai"],
    index=0,
    help="Select the generation engine. 'local_fallback' is 100% offline and requires no setup or API keys.",
)

st.sidebar.divider()
st.sidebar.subheader("Retrieval Hyperparameters")
top_k_slider = st.sidebar.slider("Top-K Passages", min_value=1, max_value=8, value=3, step=1)
threshold_slider = st.sidebar.slider("Similarity Threshold", min_value=0.10, max_value=0.80, value=0.35, step=0.05)

st.sidebar.divider()
st.sidebar.markdown("""
**Academic Information:**
- **Institution:** Jeju National University (JNU)
- **Program:** Master of Science in MIS
- **Course:** Project for Implementing RAG Systems
- **Assignment:** Assignment 01
""")

# Initialize Pipeline
with st.spinner("🏝️ Initializing Jeju Tourism AI Assistant & Loading Vector Database..."):
    rag_pipeline = get_rag_pipeline(llm_choice)
    vdb_manager = get_vector_db()

# Navigation Tabs
tabs = st.tabs([
    "🏠 Dashboard & Architecture",
    "📚 Document Management",
    "💬 AI Chat Assistant",
    "🔍 Retrieval Inspector",
    "📊 Evaluation & Analytics",
])

# ==============================================================================
# TAB 1: DASHBOARD & ARCHITECTURE
# ==============================================================================
with tabs[0]:
    st.markdown('<div class="main-header">🏝️ Jeju Tourism AI Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Design and Implementation of a Retrieval-Augmented Generation (RAG) System for Jeju Island Tourism Information</div>', unsafe_allow_html=True)

    # Real-time System Status Metrics
    stats = vdb_manager.get_stats()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Indexed Documents", stats["unique_documents_count"])
    with col2:
        st.metric("Vector Chunks in DB", stats["total_chunks"])
    with col3:
        st.metric("Embedding Dimension", f"{stats['embedding_dimension']} dims")
    with col4:
        st.metric("Vector DB Status", "🟢 Connected (Persistent)")

    st.divider()

    st.subheader("📖 Theoretical Framework (Aligned with Lecture Week 10)")
    st.markdown("""
    As covered in the **JNU MIS Week 10 Lecture (`RAG-Framework(Week10).pptx`)**, Retrieval-Augmented Generation (RAG) 
    overcomes the core limitations of standard Large Language Models (knowledge cutoffs, domain gaps, and hallucinations) 
    by retrieving external, authoritative domain documents before prompting the LLM.
    """)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        #### 1. Document Indexing Pipeline (Offline/Batch)
        1. **Document Loading**: Ingest raw TXT and multi-page PDF documents.
        2. **Text Normalization**: Strip noise, normalize Unicode, preserve semantic paragraphs.
        3. **Recursive Chunking**: Split text into segments (`chunk_size=500`, `overlap=50`) with metadata.
        4. **Dense Embeddings**: Encode chunks using `all-MiniLM-L6-v2` into 384-dimensional space.
        5. **ChromaDB Storage**: Store embeddings, text, and metadata with deduplication.
        """)

    with col_b:
        st.markdown("""
        #### 2. Query Answering Pipeline (Real-Time)
        1. **Query Embedding**: Encode the user question with the exact same embedding model.
        2. **Similarity Search**: Perform cosine distance search in ChromaDB for top-$k$ matches.
        3. **Context Construction**: Format retrieved passages with document and page citations.
        4. **Strict Grounding Prompt**: Instruct LLM to answer *only* from retrieved context.
        5. **Refusal Handling**: Explicitly refuse queries when relevant context is unavailable.
        """)

    st.info("💡 **Tip**: Switch to the **'AI Chat Assistant'** tab to start asking questions about Hallasan, Seongsan Ilchulbong, Olle trails, buses, and beaches!")

# ==============================================================================
# TAB 2: DOCUMENT MANAGEMENT
# ==============================================================================
with tabs[1]:
    st.subheader("📚 Corpus & Vector Database Management")
    st.markdown("Upload new tourism brochures or inspection documents (PDF/TXT), configure chunking, and index vectors.")

    col_up1, col_up2 = st.columns([1, 1])

    with col_up1:
        st.markdown("#### Upload Documents")
        uploaded_files = st.file_uploader(
            "Upload Tourism Documents (PDF or TXT)",
            type=["pdf", "txt"],
            accept_multiple_files=True,
            help="Upload PDF or TXT documents to index into the persistent ChromaDB collection.",
        )

        chunk_size_in = st.slider("Chunk Size (characters)", min_value=200, max_value=1000, value=500, step=50)
        chunk_overlap_in = st.slider("Chunk Overlap (characters)", min_value=0, max_value=200, value=50, step=10)

        if st.button("🚀 Process & Index Uploaded Documents", type="primary"):
            if not uploaded_files:
                st.warning("Please select at least one PDF or TXT file to upload.")
            else:
                loader = DocumentLoader()
                all_new_docs = []
                with st.spinner("Extracting text and metadata..."):
                    for up_file in uploaded_files:
                        try:
                            docs = loader.load_file(up_file, filename=up_file.name)
                            all_new_docs.extend(docs)
                            st.success(f"Loaded '{up_file.name}': {len(docs)} section(s).")
                        except Exception as e:
                            st.error(f"Error loading {up_file.name}: {e}")

                if all_new_docs:
                    with st.spinner("Chunking and updating ChromaDB..."):
                        res = vdb_manager.index_documents(
                            all_new_docs,
                            chunk_size=chunk_size_in,
                            chunk_overlap=chunk_overlap_in,
                        )
                        st.success(f"Indexing Complete! Added: **{res['added']}** chunks | Skipped duplicates: **{res['skipped_duplicates']}** | Total in DB: **{res['total_in_db']}**")
                        st.rerun()

    with col_up2:
        st.markdown("#### Currently Indexed Documents")
        current_stats = vdb_manager.get_stats()
        doc_list = current_stats["indexed_documents"]

        if doc_list:
            doc_df = pd.DataFrame({
                "Document Name": doc_list,
                "Format": [Path(d).suffix.upper() for d in doc_list],
            })
            st.dataframe(doc_df, use_container_width=True, hide_index=True)
        else:
            st.info("No documents currently indexed.")

        st.divider()
        st.markdown("#### Vector Store Maintenance")
        if st.button("⚠️ Wipe / Re-Index Default Corpus"):
            with st.spinner("Re-indexing default 8 TXT guides and 1 PDF guide..."):
                loader = DocumentLoader()
                docs = loader.load_directory(settings.DOCS_DIR)
                vdb_manager.clear_collection()
                res = vdb_manager.index_documents(docs, chunk_size=500, chunk_overlap=50)
                st.success(f"Vector Database reset and reloaded with {res['added']} chunks!")
                st.rerun()

# ==============================================================================
# TAB 3: AI CHAT ASSISTANT
# ==============================================================================
with tabs[2]:
    st.subheader("💬 Jeju Tourism AI Assistant")
    st.markdown("Ask natural language questions about Jeju Island attractions, hiking trails, buses, and travel safety.")

    # Quick Example Question Pills
    st.markdown("**Sample University Class Demonstration Queries:**")
    example_cols = st.columns(4)
    sample_q = ""
    if example_cols[0].button("🏔️ Hallasan Summit Trails"):
        sample_q = "What are the two trails that reach the Baeknokdam summit of Hallasan, and is reservation required?"
    if example_cols[1].button("🌅 Seongsan Ilchulbong"):
        sample_q = "How was Seongsan Ilchulbong formed, and what are its admission fees for adults?"
    if example_cols[2].button("🚌 Airport Bus Transit"):
        sample_q = "What is the function of the Red Express Buses in Jeju, and what are routes 101 and 102?"
    if example_cols[3].button("🚫 Unanswerable (Refusal)"):
        sample_q = "What is the ticket price and schedule for the Paris Metro subway line 4?"

    # Initialize Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "sources" in msg and msg["sources"]:
                with st.expander("🔍 View Retrieved Sources & Similarity Scores"):
                    for i, s in enumerate(msg["sources"], 1):
                        st.markdown(f"**Source {i}:** `{s['filename']}` (Page {s['page']}) | Similarity: `{s['similarity_score']:.4f}`")
                        st.text(s["content"][:300] + ("..." if len(s["content"]) > 300 else ""))

    # Input Box
    user_input = st.chat_input("Enter your question about Jeju Island...")
    active_prompt = sample_q or user_input

    if active_prompt:
        # Display User Message
        st.session_state.messages.append({"role": "user", "content": active_prompt})
        with st.chat_message("user"):
            st.markdown(active_prompt)

        # Generate RAG Response
        with st.chat_message("assistant"):
            with st.spinner("Retrieving relevant passages and synthesizing answer..."):
                response = rag_pipeline.query(
                    question=active_prompt,
                    top_k=top_k_slider,
                    threshold=threshold_slider,
                )

                st.markdown(response["answer"])

                # Display latency badge
                lat = response["latency"]
                st.caption(f"⚡ Latency: Retrieval {lat['retrieval_seconds']}s | Generation {lat['generation_seconds']}s | Total {lat['total_seconds']}s")

                if response["retrieved_chunks"]:
                    with st.expander("🔍 View Retrieved Passages & Similarity Scores"):
                        for i, s in enumerate(response["retrieved_chunks"], 1):
                            st.markdown(f"**Source {i}:** `{s['filename']}` (Page {s['page']}) | Cosine Similarity: `{s['similarity_score']:.4f}`")
                            st.info(s["content"])

        # Save to History
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["answer"],
            "sources": response["retrieved_chunks"],
        })

# ==============================================================================
# TAB 4: RETRIEVAL INSPECTOR
# ==============================================================================
with tabs[3]:
    st.subheader("🔍 Vector Database Retrieval Inspector")
    st.markdown("Inspect raw cosine similarity search rankings, chunk text, and metadata vectors directly.")

    inspect_query = st.text_input("Test Retrieval Query", value="Hallasan mountain hiking trails and reservation rules")
    inspect_k = st.slider("Inspect Top-K Results", min_value=1, max_value=10, value=5, key="inspect_k")

    if st.button("🔎 Execute Similarity Search"):
        retrieval_eng = RetrievalEngine(vector_db=vdb_manager)
        res = retrieval_eng.retrieve(query=inspect_query, top_k=inspect_k, threshold=0.0)

        st.write(f"**Retrieval Latency:** `{res['latency_seconds']:.4f} seconds` | **Retrieved Chunks:** `{len(res['chunks'])}`")

        for idx, chunk in enumerate(res["chunks"], 1):
            with st.container():
                st.markdown(f"### Rank #{idx} — Score: `{chunk['similarity_score']:.4f}` (Distance: `{chunk['distance']:.4f}`)")
                meta_cols = st.columns(3)
                meta_cols[0].write(f"**Document:** `{chunk['filename']}`")
                meta_cols[1].write(f"**Page:** `{chunk['page']}`")
                meta_cols[2].write(f"**Chunk ID:** `{chunk['chunk_id'][:20]}...`")
                st.code(chunk["content"], language="text")
                st.divider()

# ==============================================================================
# TAB 5: EVALUATION & ANALYTICS
# ==============================================================================
with tabs[4]:
    st.subheader("📊 Experimental Evaluation Dashboard")
    st.markdown("""
    Evaluate retrieval precision, recall, answer faithfulness, and latency using the 
    **22 academic benchmark questions** (`data/evaluation/benchmark_questions.json`).
    """)

    evaluator = RAGEvaluator(pipeline=rag_pipeline)

    col_btn1, col_btn2 = st.columns([1, 3])
    with col_btn1:
        run_eval_btn = st.button("🧪 Run Full 22-Question Benchmark", type="primary")

    results_csv_path = settings.RESULTS_DIR / "evaluation_results.csv"

    if run_eval_btn or results_csv_path.exists():
        if run_eval_btn:
            with st.spinner("Executing 22 test questions through ChromaDB and generation pipeline..."):
                df_results = evaluator.run_evaluation(top_k=3)
                evaluator.generate_visualizations(df_results)
                st.success("Benchmark completed and analytical charts generated!")
        else:
            df_results = pd.read_csv(results_csv_path)

        # Overview Metrics Cards
        in_domain_df = df_results[df_results["Category"] != "out_of_domain"]
        out_domain_df = df_results[df_results["Category"] == "out_of_domain"]

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Precision@3 (In-Domain)", f"{in_domain_df['Precision@K'].mean():.1%}")
        c2.metric("Recall@3 (In-Domain)", f"{in_domain_df['Recall@K'].mean():.1%}")
        c3.metric("Context Faithfulness", f"{in_domain_df['Faithfulness'].mean():.1%}")
        c4.metric("Avg Latency", f"{df_results['Total_Time_sec'].mean():.3f}s")
        refusal_rate = out_domain_df['Correct_Handling'].mean() if len(out_domain_df) > 0 else 1.0
        c5.metric("Refusal Accuracy", f"{refusal_rate:.1%}")

        st.divider()

        # Visualizations
        st.markdown("#### Evaluation Charts (Matplotlib High-Resolution)")
        fig_col1, fig_col2 = st.columns(2)

        fig1_path = settings.FIGURES_DIR / "retrieval_performance_by_topic.png"
        fig2_path = settings.FIGURES_DIR / "latency_breakdown.png"
        fig3_path = settings.FIGURES_DIR / "overall_rag_metrics.png"

        if fig1_path.exists():
            fig_col1.image(str(fig1_path), caption="Figure 1: Precision@3 and Recall@3 by Tourism Topic")
        if fig2_path.exists():
            fig_col2.image(str(fig2_path), caption="Figure 2: Processing Latency Breakdown by Category")
        if fig3_path.exists():
            st.image(str(fig3_path), caption="Figure 3: Overall System Quality Scores Across In-Domain Questions", width=700)

        st.divider()

        # Detailed Table
        st.markdown("#### Benchmark Results Table")
        st.dataframe(
            df_results[[
                "Question_ID", "Category", "Topic", "Question",
                "Top_Similarity_Score", "Precision@K", "Recall@K",
                "Faithfulness", "Total_Time_sec", "Generated_Answer"
            ]],
            use_container_width=True,
        )

        # Download CSV
        with open(results_csv_path, "rb") as f:
            st.download_button(
                label="📥 Download Full Evaluation CSV",
                data=f.read(),
                file_name="jeju_rag_evaluation_results.csv",
                mime="text/csv",
            )
