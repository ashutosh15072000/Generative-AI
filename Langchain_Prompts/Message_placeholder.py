from langhchain_core.prompts import ChatPromptTemplate,MessagePlaceholder

chat_template=ChatPromptTemplate(
    [
        ("system","You are  a helpful customer agent"),
        MessagePlaceholder(variable_name="chat_history"),
        ("human","{query}")
    ]
)

chat_history=[]
## Load chat history

with open("Chat_History.txt") as f:
    chat_history.append(f.readlines())

prompt=chat_template.invoke({"chat_history":chat_history,"query":"where is my refund"})

print(prompt)