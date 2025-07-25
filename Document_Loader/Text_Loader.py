from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template="Write a summary for the poem \n {poem}",
    input_variables=["poem"],
)
loader=TextLoader("cricket.txt",encoding="utf-8")

docs=loader.load()

print(len(docs))

parser=StrOutputParser()

chain=prompt|model|parser

print(chain.invoke({"poem":docs[0].page_content}))