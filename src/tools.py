from .config import settings
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

search_tool = TavilySearch(max_results=3, tavily_api_key=settings.tavily_api_key.get_secret_value())

@tool(description="Use this tool to search the web for relevant information to answerthe user's question. Always use this tool if you don't know the answer to the user's question or if you need more information to answer the user's question.")
def get_search_tool(query: str) -> str:
    return search_tool.run(query)