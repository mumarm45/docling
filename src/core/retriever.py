from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers.ensemble import EnsembleRetriever
from src.core.embedding import setup_embedding_model
from src.config.settings import settings
import logging
logger = logging.getLogger(__name__)
class Retriever:
    def __init__(self):
        self.embeddings = setup_embedding_model()
    def build_hybrid_retriever(self, docs):
        """Build a hybrid retriever using BM25 and vector-based retrieval."""
        try:
            vector_store = Chroma.from_documents(
                documents=docs,
                embedding=self.embeddings,
                persist_directory=settings.CHROMA_DB_PATH
            )

            bm25_retriever =  BM25Retriever.from_documents(docs)

            vector_retriever = vector_store.as_retriever(search_kwargs={"k": settings.VECTOR_SEARCH_K})

            hybrid_retriever = EnsembleRetriever(
                retrievers=[bm25_retriever, vector_retriever],
                weights=[0.5, 0.5]
            )
            
            return hybrid_retriever
        except Exception as e:
            logger.error(f"Failed to build vector store: {e}")
            raise