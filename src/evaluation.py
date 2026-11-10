"""
Evaluation module for Jeju Tourism RAG system.
Executes benchmark questions against the persistent ChromaDB database,
computes quantitative retrieval and generation metrics,
exports results to CSV, and generates analytical figures.
"""
import json
import time
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config.settings import settings
from src.generation import RAGGenerationPipeline

logger = logging.getLogger(__name__)


class RAGEvaluator:
    """Evaluates retrieval accuracy, answer faithfulness, and latency."""

    def __init__(self, pipeline: RAGGenerationPipeline = None):
        self.pipeline = pipeline or RAGGenerationPipeline()
        self.benchmark_file = settings.EVAL_DIR / "benchmark_questions.json"
        self.results_csv = settings.RESULTS_DIR / "evaluation_results.csv"
        self.figures_dir = settings.FIGURES_DIR

    def load_benchmark_questions(self) -> List[Dict[str, Any]]:
        """Load benchmark evaluation questions from JSON."""
        if not self.benchmark_file.exists():
            raise FileNotFoundError(f"Benchmark file not found: {self.benchmark_file}")
        with open(self.benchmark_file, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def calculate_precision_at_k(retrieved_docs: List[str], target_docs: List[str], k: int) -> float:
        """
        Precision@k = (Number of retrieved chunks originating from target docs) / k
        For out_of_domain queries (where target_docs is empty), precision is 1.0 if score is low or handled properly.
        """
        if not target_docs:
            return 1.0  # Handled separately in unanswerable metrics
        if k <= 0 or not retrieved_docs:
            return 0.0

        hits = sum(1 for doc in retrieved_docs[:k] if doc in target_docs)
        return round(hits / k, 4)

    @staticmethod
    def calculate_recall_at_k(retrieved_docs: List[str], target_docs: List[str], k: int) -> float:
        """
        Recall@k = (Unique target documents retrieved in top-k) / (Total target documents)
        """
        if not target_docs:
            return 1.0
        unique_targets = set(target_docs)
        unique_retrieved_targets = set(doc for doc in retrieved_docs[:k] if doc in unique_targets)
        return round(len(unique_retrieved_targets) / len(unique_targets), 4)

    @staticmethod
    def calculate_faithfulness(answer: str, context: str) -> float:
        """
        Calculates context faithfulness score in [0.0, 1.0] by measuring the proportion
        of answer content words that exist directly within the retrieved context.
        """
        if not answer:
            return 0.0
        # If the answer is an explicit refusal for unanswerable queries
        refusal_phrases = ["sufficient information is unavailable", "do not contain", "cannot be found"]
        if any(p in answer.lower() for p in refusal_phrases):
            return 1.0

        words_answer = [w.lower() for w in answer.split() if len(w) > 3]
        if not words_answer:
            return 1.0

        context_lower = context.lower()
        supported = sum(1 for w in words_answer if w in context_lower)
        return round(supported / len(words_answer), 4)

    @staticmethod
    def calculate_relevance(answer: str, key_entities: List[str]) -> float:
        """
        Calculates answer relevance score based on presence of essential ground-truth entities.
        """
        if not key_entities:
            return 1.0
        answer_lower = answer.lower()
        matched = sum(1 for entity in key_entities if entity.lower() in answer_lower)
        return round(matched / len(key_entities), 4)

    def run_evaluation(self, top_k: int = 3) -> pd.DataFrame:
        """
        Execute full evaluation benchmark on all questions and collect metrics.
        """
        questions = self.load_benchmark_questions()
        records = []

        logger.info(f"Running evaluation benchmark on {len(questions)} questions (top_k={top_k})...")

        for idx, item in enumerate(questions, start=1):
            qid = item["id"]
            question = item["question"]
            category = item["category"]
            topic = item["topic"]
            target_docs = item["target_documents"]
            key_entities = item.get("key_entities", [])

            # Run RAG Query
            result = self.pipeline.query(question=question, top_k=top_k)

            answer = result["answer"]
            retrieved_chunks = result["retrieved_chunks"]
            retrieved_filenames = [c["filename"] for c in retrieved_chunks]
            top_score = retrieved_chunks[0]["similarity_score"] if retrieved_chunks else 0.0

            # Calculate Metrics
            p_at_k = self.calculate_precision_at_k(retrieved_filenames, target_docs, top_k)
            r_at_k = self.calculate_recall_at_k(retrieved_filenames, target_docs, top_k)
            faithfulness = self.calculate_faithfulness(answer, result["context_text"])
            relevance = self.calculate_relevance(answer, key_entities)

            # Check unanswerable correctness
            is_unanswerable = category == "out_of_domain"
            refusal_detected = (
                "sufficient information is unavailable" in answer.lower()
                or "do not contain" in answer.lower()
                or "cannot be found" in answer.lower()
            )
            correct_refusal = (is_unanswerable and refusal_detected) or (not is_unanswerable and not refusal_detected)

            record = {
                "Question_ID": qid,
                "Category": category,
                "Topic": topic,
                "Question": question,
                "Top_Similarity_Score": top_score,
                "Precision@K": p_at_k,
                "Recall@K": r_at_k,
                "Faithfulness": faithfulness,
                "Relevance": relevance,
                "Correct_Handling": correct_refusal,
                "Retrieval_Time_sec": result["latency"]["retrieval_seconds"],
                "Generation_Time_sec": result["latency"]["generation_seconds"],
                "Total_Time_sec": result["latency"]["total_seconds"],
                "Retrieved_Sources": "; ".join(set(retrieved_filenames)),
                "Generated_Answer": answer[:150] + ("..." if len(answer) > 150 else ""),
            }
            records.append(record)

        df = pd.DataFrame(records)
        # Ensure results dir exists and save
        settings.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(self.results_csv, index=False, encoding="utf-8-sig")
        logger.info(f"Evaluation results successfully saved to '{self.results_csv}'.")

        return df

    def generate_visualizations(self, df: pd.DataFrame) -> List[Path]:
        """Generate academic Matplotlib charts from actual evaluation results."""
        settings.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        figure_paths = []

        # Style configuration
        plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
        plt.rcParams["font.family"] = "sans-serif"

        # Filter out negative controls for retrieval precision/recall charts
        factual_df = df[df["Category"] != "out_of_domain"]

        # -------------------------------------------------------------
        # Figure 1: Retrieval Precision & Recall by Topic
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
        topic_grp = factual_df.groupby("Topic")[["Precision@K", "Recall@K"]].mean().reset_index()

        x = np.arange(len(topic_grp))
        width = 0.35

        rects1 = ax.bar(x - width / 2, topic_grp["Precision@K"], width, label="Precision@3", color="#1f77b4")
        rects2 = ax.bar(x + width / 2, topic_grp["Recall@K"], width, label="Recall@3", color="#2ca02c")

        ax.set_ylabel("Score (0.0 to 1.0)", fontsize=11, fontweight="bold")
        ax.set_title("Jeju Tourism RAG: Retrieval Precision@3 and Recall@3 by Topic", fontsize=13, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(topic_grp["Topic"], rotation=30, ha="right", fontsize=9)
        ax.set_ylim(0, 1.15)
        ax.legend(loc="upper right")

        for rect in rects1 + rects2:
            height = rect.get_height()
            ax.annotate(f"{height:.2f}", xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8)

        plt.tight_layout()
        f1_path = settings.FIGURES_DIR / "retrieval_performance_by_topic.png"
        fig.savefig(f1_path)
        plt.close(fig)
        figure_paths.append(f1_path)

        # -------------------------------------------------------------
        # Figure 2: Latency Breakdown (Retrieval vs Generation)
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        cat_latency = df.groupby("Category")[["Retrieval_Time_sec", "Generation_Time_sec"]].mean()

        cat_latency.plot(kind="bar", stacked=True, ax=ax, color=["#ff7f0e", "#1f77b4"], width=0.5)
        ax.set_ylabel("Latency (Seconds)", fontsize=11, fontweight="bold")
        ax.set_title("Average Processing Latency by Question Category", fontsize=13, fontweight="bold")
        ax.set_xlabel("Question Category", fontsize=11, fontweight="bold")
        ax.set_xticklabels(cat_latency.index, rotation=0, fontsize=10)
        ax.legend(["Retrieval Time", "Generation Time"], loc="upper right")

        for i, (idx_name, row) in enumerate(cat_latency.iterrows()):
            total = row["Retrieval_Time_sec"] + row["Generation_Time_sec"]
            ax.annotate(f"{total:.3f}s", xy=(i, total), xytext=(0, 3),
                        textcoords="offset points", ha="center", va="bottom", fontsize=9, fontweight="bold")

        plt.tight_layout()
        f2_path = settings.FIGURES_DIR / "latency_breakdown.png"
        fig.savefig(f2_path)
        plt.close(fig)
        figure_paths.append(f2_path)

        # -------------------------------------------------------------
        # Figure 3: Faithfulness and Relevance Distribution
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        metrics = ["Precision@K", "Recall@K", "Faithfulness", "Relevance"]
        mean_vals = [factual_df[m].mean() for m in metrics]
        colors = ["#1f77b4", "#2ca02c", "#9467bd", "#e377c2"]

        bars = ax.bar(metrics, mean_vals, color=colors, width=0.5)
        ax.set_ylabel("Mean Metric Score", fontsize=11, fontweight="bold")
        ax.set_title("Overall RAG Quality Metrics Across In-Domain Questions", fontsize=13, fontweight="bold")
        ax.set_ylim(0, 1.15)

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f"{height:.3f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=9, fontweight="bold")

        plt.tight_layout()
        f3_path = settings.FIGURES_DIR / "overall_rag_metrics.png"
        fig.savefig(f3_path)
        plt.close(fig)
        figure_paths.append(f3_path)

        logger.info(f"Generated 3 analytical figures in '{settings.FIGURES_DIR}'.")
        return figure_paths
