from langchain_openai import ChatOpenAI
from .config import settings

def get_llm():
    llm = ChatOpenAI(model=settings.model, 
                     temperature=settings.model_temperature, 
                     api_key=settings.openai_api_key)
    return llm