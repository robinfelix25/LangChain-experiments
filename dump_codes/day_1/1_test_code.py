# from langchain_ollama import ChatOllama

# model = ChatOllama(model="llama3")

# response = model.invoke("Explain overfitting in Machine learning")

# print(response.content)

# from langchain_ollama import OllamaLLM

# model = OllamaLLM(model = "llama3", temperature= 0.2)

# response = model.invoke("Explain overfitting")

# print(response)


from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")


#PromptTemplate
# from langchain_core.prompts import PromptTemplate

# user_input = input("Enter your topic here")

# dynamic_prompt = PromptTemplate.from_template("Write a fun fact about {topic}")
# print(dynamic_prompt)

# ready_prompt = dynamic_prompt.invoke({"topic" : user_input})

# print(ready_prompt)


#ChatPromptTemplate

from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpfull assistanct'),
    ('human', 'Write func fact about {topic}' )
])

user_input = input("Enter a topic : ")
user_input1 = input("Enter a theme : ")

ready_prompt = prompt_template.invoke({'topic' : user_input, 'theme' : user_input1})

print(ready_prompt)

print(llm.invoke(ready_prompt).content)

