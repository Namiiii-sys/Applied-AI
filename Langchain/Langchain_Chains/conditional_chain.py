#Take feedback from user and analyse its sentiment and f pos reply in a positive sense, if neg then reply accordingly

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['Positive','Negative'] = Field(description="Give the sentiment of the given feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template = "Analyse the sentiment of the following feedback whether positive or negatve \n {feedback} \n {format_inst}",
    input_variables=['feedback'],
    partial_variables={"format_inst": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

Prompt2 = PromptTemplate( 
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

Prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
) 

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', Prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', Prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is a beautiful car!'}))
chain.get_graph().print_ascii()