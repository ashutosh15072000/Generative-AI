from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()

prompt_1=PromptTemplate(
    template="Generative tweet about the {topic}",
    input_variables=['topic']
)

prompt_2=PromptTemplate(
    template="Generative a Linkedin post about {topic}",
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt_1,model,parser),
    "linkedin":RunnableSequence(prompt_2,model,parser)
})

result=parallel_chain.invoke({"topic":"ai"})

print(result)