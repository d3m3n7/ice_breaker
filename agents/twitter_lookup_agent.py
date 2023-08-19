from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

from tools.tools import google_search


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to give me a link to their Twitter profile page 
        and extract from it their username aka handle. 
        Your answer should contain exactly 1 handle, no other words should be included"""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=google_search,
            description="useful for when you need get",
        )
    ]
    return "Twitter username: @elonmusk"
