from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model=ChatOpenAI()

## SCHEMA

class Review(TypedDict):
    summary:Annotated[str, "A Brief summary of the review"]
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review"]
    sentiment:Annotated[str,"Return sentiment of the review either negative ,postive ,or neural"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]],"Write down all the cons inside the list"]
structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""The hardware is great, but the software feels bloated.
                               Theere are too many pre installed apps that i can't remove .also the UI looks outdated compared to other brands.Hoping for a software update to fix this.""")

print(result)