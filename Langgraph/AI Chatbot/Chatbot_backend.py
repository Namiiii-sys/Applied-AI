from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "chatbot.db"

conn = sqlite3.connect(
    str(DB_PATH),
    check_same_thread=False
)

checkpointer = SqliteSaver(conn=conn)


load_dotenv()

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

def Chat(state: ChatState):

    messages = state['messages']
    res = LLM.invoke(messages)

    return {'messages': [res]}

#checkpointer
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node('Chat', Chat)

graph.add_edge(START, 'Chat')
graph.add_edge('Chat', END)

Chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        thread_id = checkpoint.config["configurable"].get("thread_id")
        if thread_id:
            all_threads.add(thread_id)
    return list(all_threads)


