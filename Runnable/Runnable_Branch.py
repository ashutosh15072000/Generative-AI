from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableSequence,RunnableBranch

load_dotenv()

def word_counter(text):
    return len(text.split())


runnable_word_counter=RunnableLambda(word_counter)

print(runnable_word_counter.invoke("Hi there how are you ?"))


prompt=PromptTemplate(
    template="Write a Detail report on {topic}",
    input_variables=["topic"]
)
prompt_1=PromptTemplate(
    template="Summarize the following \n {text}",
    input_variables=["text"]
)

model=ChatOpenAI()

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt_1,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

result=final_chain.invoke({"topic":"Russia vs Ukarain"})

print(result)

