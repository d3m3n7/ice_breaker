import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from utils import get_webpage


def run_chain():
    # information = get_webpage('https://en.wikipedia.org/wiki/Elon_Musk')
    information = '''
        Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX, angel investor, CEO and product architect of Tesla, Inc., owner, chairman and CTO of X Corp., founder of the Boring Company, a co-founder of Neuralink and OpenAI, and the president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$217 billion as of August 2023, according to the Bloomberg Billionaires Index, and $219 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[3][4][5]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother.[6] Two years later, he matriculated at Queen's University in Kingston, Ontario. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics there. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and with $12 million of the money he made, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. 
    '''
    summary_template = '''
        Given the information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them
    '''
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    api_key = os.environ.get('OPENAI_API_KEY')
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.run(information=information)
    print(result)

run_chain()
