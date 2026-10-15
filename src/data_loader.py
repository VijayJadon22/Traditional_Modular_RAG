
from pathlib import Path
from typing import List, Any

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
    JSONLoader,
)
from langchain_community.document_loaders.excel import UnstructuredExcelLoader


def load_all_documents(data_dir: str) -> List[Any]:
    """Load supported files into LangChain Document objects."""

    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")

    if not data_path.is_dir():
        raise FileNotFoundError(f"Data directory not found: {data_path}")

    documents = []

    # PDF files
    for file in data_path.glob("**/*.pdf"):
        try:
            loaded = PyPDFLoader(str(file)).load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} PDF documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {file}: {e}")

    # TXT files
    for file in data_path.glob("**/*.txt"):
        try:
            loaded = TextLoader(str(file), encoding="utf-8").load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} TXT documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load TXT {file}: {e}")

    # CSV files
    for file in data_path.glob("**/*.csv"):
        try:
            loaded = CSVLoader(str(file)).load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} CSV documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load CSV {file}: {e}")

    # Excel files
    for file in data_path.glob("**/*.xlsx"):
        try:
            loaded = UnstructuredExcelLoader(str(file)).load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} Excel documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load Excel {file}: {e}")

    # Word files
    for file in data_path.glob("**/*.docx"):
        try:
            loaded = Docx2txtLoader(str(file)).load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} Word documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load Word {file}: {e}")

    # JSON files
    for file in data_path.glob("**/*.json"):
        try:
            # Adjust jq_schema to match your JSON structure.
            loaded = JSONLoader(
                file_path=str(file),
                jq_schema=".",
                text_content=False,
            ).load()
            documents.extend(loaded)
            print(f"Loaded {len(loaded)} JSON documents: {file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load JSON {file}: {e}")

    print(f"\nTotal documents loaded: {len(documents)}")
    return documents


all_documents = load_all_documents("../data")
print(all_documents)
