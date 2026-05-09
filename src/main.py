from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# from prompt import get_prompt
# from agent import get_agent
# from llm import get_llm
# from tools import get_search_tool
from pprint import pprint

from .prompt import get_prompt
from .agent import get_agent
from .llm import get_llm
from .tools import get_search_tool


def main(student_class: int = 9, subject: str = "Mathematics", topics: list[str] = ["Coordinate Geometry"], questions: list[str] = ["Multiple Choice", "Short Answer", "Long Answer", "Word Problems"]):
    llm = get_llm()
    search_tool = get_search_tool
    user_prompt = get_prompt('user')
    system_prompt = get_prompt('system')
    tools = [search_tool]
    agent = get_agent(model=llm, tools=tools, response_format=None, system_prompt=system_prompt)
    print('Invoking agent...')
    response = agent.invoke({
        "messages": [{"role": "user", "content": user_prompt.format(student_class=student_class, subject=subject, topics=", ".join(topics), questions=", ".join(questions))}]
    })
    return response
    
