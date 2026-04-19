from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

model = create_agent(
    model=llm,
    tools=[]
)

print(model)