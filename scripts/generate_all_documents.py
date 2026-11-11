"""
Master execution script to generate all 52 new documents into data/documents/.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "data" / "documents"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

# Import batches
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
import build_expanded_corpus_part1 as p1
import build_expanded_corpus_part2 as p2
import build_expanded_corpus_part3 as p3

all_docs = {}
all_docs.update(p1.DOCUMENTS)
all_docs.update(p2.DOCUMENTS)
all_docs.update(p3.DOCUMENTS)

print(f"Total documents to write: {len(all_docs)}")

written_count = 0
for filename, content in all_docs.items():
    file_path = DOCS_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    written_count += 1
    print(f"[{written_count:02d}/{len(all_docs)}] Wrote {filename} ({len(content)} chars)")

# Check total files in data/documents
all_files = list(DOCS_DIR.glob("*"))
print("\n" + "=" * 60)
print(f"SUCCESS! Total files in data/documents: {len(all_files)}")
print(f"TXT files: {len(list(DOCS_DIR.glob('*.txt')))}")
print(f"PDF files: {len(list(DOCS_DIR.glob('*.pdf')))}")
print("=" * 60)
