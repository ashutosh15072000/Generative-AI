from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_env

load_env()

model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result=model.invoke("what is the capital of india")
print(result.content)