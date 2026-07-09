from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from tools import tools

load_dotenv()

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
)

llm_with_tools = llm.bind_tools(tools)

def invoke_llm(messages):
    """
    Invoke the LLM with the current conversation history.
    """
    return llm_with_tools.invoke(messages)

