from langchain_huggingface import ChatHuggingFace,HuggingFaceEndPoint
from dotenv import load_env

load_env()
llm=HuggingFaceEndPoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("What is capital of India?")

print(result.content)