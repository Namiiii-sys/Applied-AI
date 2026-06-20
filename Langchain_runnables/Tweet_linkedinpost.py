from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate one short tweet on the {topic} topic, no options just 1 post",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="Generate one short Linkedin post on the {topic} topic, no options just 1 post",
    input_variables=['topic']
)

Parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model1 ,parser),
    'Linkedin' : prompt2 | model2 | parser
})

result = Parallel_chain.invoke({'topic':'AI'})
print(result)
