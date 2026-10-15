from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline


##Example Usage

if __name__ == "__main__":
    docs = load_all_documents("data")
    chunks = EmbeddingPipeline().chunk_documents(docs)
    vectors = EmbeddingPipeline().embed_chunks(chunks)
    print(vectors)
