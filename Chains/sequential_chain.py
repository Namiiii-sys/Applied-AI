from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate  2 important pointers on the {text}",
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser

# 

chain.get_graph().print_ascii()