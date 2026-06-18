from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

#1st prompt -> Detailed report
template1 = PromptTemplate(
    template= 'Write a detailed report on {topic}',
    input_variables=['topic']
)
#2nd prompt -> summary
template2 = PromptTemplate(
    template= 'Write a 5 line summary on following text \n {text}',
    input_variables=['text']
) 
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Black hole'})

print(result)
