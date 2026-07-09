"""
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from prompt import summary_prompt

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

summary_chain = (
    summary_prompt
    | llm
    | StrOutputParser()
)
"""