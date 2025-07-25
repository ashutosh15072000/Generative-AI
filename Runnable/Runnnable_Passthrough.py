from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt_1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)
model=ChatOpenAI()

parser=StrOutputParser()

prompt_2=PromptTemplate(
    template="Explain the following joke -{text}",
    input_variables=["text"],
)

joke_gen_chain=RunnableSequence(prompt_1,model,parser)

parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "explanation":RunnableParallel(prompt_2,model,parser),
    }
)

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({
    "topic": "python",
})

print(result)