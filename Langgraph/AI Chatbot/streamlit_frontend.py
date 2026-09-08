import streamlit as st
from streamlit_chat import message
from Chatbot_backend import Chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid

# Utility functions 

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversations(thread_id):
    state = Chatbot.get_state(config={'configurable': {'thread_id':thread_id}})
    return state.values.get('messages',[])


#st.session_state -> dict -> 
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])

st.sidebar.title('Langgraph Chatbot')

#New Chat button
if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        list_of_messages = load_conversations(thread_id)

        temp_messages = []

        for mess in list_of_messages:
            if isinstance(mess, HumanMessage):
                is_user=True
            else:
                is_user=False
            temp_messages.append({'is_user':is_user,'content': mess.content})

        st.session_state['message_history'] = temp_messages


CONFIG = {'configurable': {'thread_id':st.session_state['thread_id']}}


#loading the conversation history
for msg in st.session_state['message_history']:
    message(msg['content'], is_user=msg['is_user'])

user_input = st.chat_input('Type here...')

if user_input:

    #first add message to message history
    st.session_state['message_history'].append({'is_user':True,'content': user_input})
    message(user_input, is_user=True)

    #first add message to message history
    Ai_message = st.write_stream(
        message_chunk.content for message_chunk, metadata in Chatbot.stream(
            {"messages":[HumanMessage(content=user_input)]},
            config = CONFIG,
            stream_mode='messages'
        )
    )
    st.session_state['message_history'].append({'is_user':False,'content': Ai_message})
