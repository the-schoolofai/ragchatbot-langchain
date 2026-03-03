from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOllama(
    model="qwen2.5-coder:3b",
    temperature=0.7,
    num_predict=1024,
    num_ctx=4096
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in {topic}, Give concise, accurate answers."),
        ("human", "{question}")
    ]
)

chain = prompt | llm | StrOutputParser()

for chunk in chain.stream({"topic": "AI", "question": "What is RAG?"}):
    print(chunk, end="", flush=True)

