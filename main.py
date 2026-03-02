from langchain_ollama import ChatOllama


# Basic LLM Call
llm = ChatOllama(
    model="qwen2.5-coder:3b", 
    temperature=0.7
)

response = llm.invoke("What is NLP?")
print(response.content)