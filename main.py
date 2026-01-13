
from langchain_community.document_loaders import PyPDFLoader
from src.core.retriever import Retriever
from src.agents.workflow import AgentWorkflow

# Global session state dictionary
session_state = {}

def main():
    # Initialize session state if not exists
    if 'retrievers' not in session_state:
        session_state['retrievers'] = {}
    
    file_handler = PyPDFLoader("example/google-2024-environmental-report.pdf")
    chunks1 = file_handler.load()
    # chunks2 = file_handler.get_file_chunks("example/google-2024-environmental-report.pdf", 10, 2)
    retriever = Retriever()
    
    deepseek_retriever = retriever.build_hybrid_retriever(chunks1)
    # google_retriever = retriever.build_hybrid_retriever(chunks2)
    
    # session_state['retrievers']['deepseek'] = deepseek_retriever
    # session_state['retrievers']['google'] = google_retriever

    workflow = AgentWorkflow()
    result = workflow.full_pipeline("What is the company's revenue?", deepseek_retriever)
    print(result)
    
   

def get_session_retriever(name):
    """Helper function to get retriever from session state"""
    return session_state.get('retrievers', {}).get(name)

def add_session_retriever(name, retriever):
    """Helper function to add retriever to session state"""
    if 'retrievers' not in session_state:
        session_state['retrievers'] = {}
    session_state['retrievers'][name] = retriever


if __name__ == "__main__":
    main()