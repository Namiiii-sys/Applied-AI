#for validation, strict

from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class Person(BaseModel):
    name: str = Field(description='Name of the Person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instr}',
    input_variables=['place'],
    partial_variables={'format_instr':parser.get_format_instructions()}

)

chain = template | model | parser
result = chain.invoke({'place':'nepali'})
print(result)
