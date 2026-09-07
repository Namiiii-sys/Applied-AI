import streamlit as st
from streamlit_chat import message
from Basic_chatbot import Chatbot
from langchain_core.messages import BaseMessage, HumanMessage

config = {"configurable": {"thread_id":"thread_1"}}
#st.session_state -> dict -> 
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#loading the conversation history
for msg in st.session_state['message_history']:
    message(msg['content'], is_user=msg['is_user'])

user_input = st.chat_input('Type here...')

if user_input:

    #first add message to message history
    st.session_state['message_history'].append({'is_user':True,'content': user_input})
    message(user_input, is_user=True)

    #first add message to message history
    #AI response
    response = Chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config = config)
    Ai_message = response['messages'][-1].content
    
    st.session_state['message_history'].append({'is_user':False,'content': Ai_message})
    message(Ai_message)
