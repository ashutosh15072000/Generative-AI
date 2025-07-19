from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RouterRunnable

load_dotenv()


prompt_1=PromptTemplate(
    template="Write a joke about the {topic}",
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

prompt_2=PromptTemplate(
    template="explain the following the {text}",
    input_variables=['text']
)

chain=RouterRunnable(prompt_1,model,parser,prompt_2,model,parser)

result=chain.invoke({"topic":"AI"}
)

print(result)