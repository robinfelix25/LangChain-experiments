# from langchain_community.llms import Ollama
# from langchain.
# llm = Ollama(model="llama3")

# response = llm.invoke("Explain transformers in simple terms")
# print(response)


from langchain.agents import create_agent

agent = create_agent("openai:gpt-5", tools=tools)

from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model='llama4',
    temperature=0.1
    
)