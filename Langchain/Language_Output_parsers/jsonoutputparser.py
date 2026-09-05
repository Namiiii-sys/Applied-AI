from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the real name , age, city and family's name of Invincible superhero \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({})
print(result)
