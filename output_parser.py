from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(cescription="Summary of the person")
    facts: List[str] = Field(description="interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        description="Create ice breakers to open a conversation with tne person"
    )

    def to_dict(self) -> dict:
        return dict(
            summary=self.summary,
            facts=self.facts,
            topics_of_interest=self.topics_of_interest,
            ice_breakers=self.ice_breakers,
        )


def get_parser() -> PydanticOutputParser:
    return PydanticOutputParser(pydantic_object=PersonIntel)
