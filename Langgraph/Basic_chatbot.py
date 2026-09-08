from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

def Chat(state: ChatState):

    messages = state['messages']
    res = LLM.invoke(messages)

    return {'messages': [res]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node('Chat', Chat)

graph.add_edge(START, 'Chat')
graph.add_edge('Chat', END)

Chatbot = graph.compile(checkpointer=checkpointer)

