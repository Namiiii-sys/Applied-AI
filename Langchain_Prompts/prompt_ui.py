from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')
st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)


## Second UI for the same

st.header('Research tool')
paper_input = st.selectbox("Select Research Paper Name", ["Attention is All You Need",
  "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are few-shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-friendly","Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation length",["Short (1-2 paragraphs)", "Medium(3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')
#fill placeholders
prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input': style_input,
    'length_input':length_input

})

if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)


