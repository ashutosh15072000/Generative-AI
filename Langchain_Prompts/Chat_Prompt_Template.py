from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate(
    [
        ("system","You are a Helpful {Domain} experts"),
        ("human","Explain in simple terms , what is {Topic}")
       
    ]
)

prompt=chat_template.invoke({'Domain':"Cricket","topic":"Dusra"})

print(prompt)