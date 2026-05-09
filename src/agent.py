from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import BaseTool
from typing import Optional
from pydantic import BaseModel

def get_agent(model: ChatOpenAI, tools: list[BaseTool], response_format: Optional[BaseModel] = None, system_prompt: Optional[str] = None):
    if response_format:
        agent = create_agent(model=model, tools=tools, response_format=response_format, system_prompt=system_prompt) # pyright: ignore[reportArgumentType]
    else:
        agent = create_agent(model=model, tools=tools, response_format=response_format, system_prompt=system_prompt)
    return agent
