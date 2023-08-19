import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from utils import get_webpage


def summarize_linkedin():
    summary_template = """
        Given the information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    api_key = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_profile_url = lookup(name="John Marty")
    linkedin_data = scrape_linkedin_profile(url=linkedin_profile_url)
    result = chain.run(information=linkedin_data)
    print(result)


def test_twitter():
    scrape_user_tweets(username="@elonmusk")


test_twitter()
