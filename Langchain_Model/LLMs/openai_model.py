from langchain_openai import OpenAI
from dotenv import load_env
import os
load_env()

llm=OpenAI(model="gpt-3.5-turbo-intruct",)

result=llm.invoke("What is the capital of India")

print(result)