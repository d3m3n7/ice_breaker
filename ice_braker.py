import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from utils import get_webpage


def run_chain():
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
    linkedin_data = scrape_linkedin_profile(
        url="TODO: THIS IS A MOCKUP, returns cached"
    )
    result = chain.run(information=linkedin_data)
    print(result)


run_chain()
