from core.llm_client import LLMClient
import logging
logger = logging.getLogger(__name__)
class ResearchAgent:
    def __init__(self):
        self.llm_client = LLMClient()
    def sanitize_response(self, response_text: str) -> str:
        """
        Sanitize the LLM's response by stripping unnecessary whitespace.
        """
        return response_text.strip()    
        
    def generate_prompt(self, question, context):
        prompt = f"""
            You are an AI assistant designed to provide precise and factual answers based on the given context.

            **Instructions:**
            - Answer the following question using only the provided context.
            - Be clear, concise, and factual.
            - Return as much information as you can get from the context.
            
            **Question:** {question}
            **Context:**
            {context}

            **Provide your answer below:**
        """
        return prompt  
    def generate_answer(self, question, documents):         
        context = "\n\n".join([doc.page_content for doc in documents])
        prompt = self.generate_prompt(question, context)
        try:
            response = self.llm_client.invoke(prompt)
            llm_response = self.sanitize_response(response.content.strip())
            print(f"Raw LLM response:\n{llm_response}")
        except Exception as e:
            logger.error(f"Failed to generate answer: {e}")
            llm_response = "I cannot answer this question based on the provided documents."
        
        draft_answer = self.sanitize_response(llm_response)
        return {
                "draft_answer": draft_answer,
                "context_used": context
            }
    
        
            