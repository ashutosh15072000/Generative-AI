from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_env


load_env()

model=ChatOpenAI()

messages=[
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Tell me about the AI?"),
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)