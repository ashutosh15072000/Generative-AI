from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
load_dotenv()



llm=HuggingFaceEndpoint(
    repo_id="google/gemma-2-9b-it",
    task="text-generation",
)

model=ChatHuggingFace(llm=llm)

## Ist Prompt -> Detailed report
template_1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
## 2nnd Prompy -> Summary
template_2=PromptTemplate(
    template="Write a 5 line summary on the following text /n {text}",
    input_variables=["text"]
)

prompt1=template_1.invoke({'topic':"black hole"})

result=model.invoke(prompt1)

prompt2=template_2.invoke({'text':result.content})

result1=model.invoke(prompt2)

print(result1)