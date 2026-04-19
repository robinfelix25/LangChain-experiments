from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.chat_models import ChatOllama

from langchain_ollama import ChatOllama


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} simply"
)

model = ChatOllama(model="gemma3:4b")

chain = prompt | model

print(chain.invoke({"topic": "overfitting"}).content)