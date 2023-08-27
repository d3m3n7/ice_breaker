import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser

from agents.linkedin_lookup_agent import lookup
from output_parser import get_parser
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from utils import get_webpage


def summarize_linkedin(person_intel_parser: PydanticOutputParser):
    summary_template = """
        Given the information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them
            3. A topic that may interest them
            4. 2 creative Ice breakers to open a conversation with them
                    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    os.environ.get("OPENAI_API_KEY")  # internally ChatOpenAI needs this
    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_profile_url = lookup(name="John Marty")
    linkedin_data = scrape_linkedin_profile(url=linkedin_profile_url)
    return chain.run(information=linkedin_data)


if __name__ == "__main__":
    result = summarize_linkedin(person_intel_parser=get_parser())
    print(result)
