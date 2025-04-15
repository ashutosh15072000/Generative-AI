from langchain_openai import ChatOpenai
from dotenv import load_env

load_env()

chat_model=ChatOpenai(model="gpt-4",temperature=0.2,max_completion_tokens=10)

result=chat_model.invoke("what is captial of India?")

print(result['content'])