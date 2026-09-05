from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence, RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

Parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a Report on the topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='SUmmarize the text {text}',
    input_variables=['text']
)

report_chain = prompt1 | model | Parser

Branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, prompt2 | model | Parser),
    RunnablePassthrough()
)

final_Chain = report_chain | Branch_chain
final_Chain.invoke({'topic':'Russia vs Ukriane'})
print(final_Chain)
final_Chain.get_graph().print_ascii()




 