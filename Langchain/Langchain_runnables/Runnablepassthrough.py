from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

Parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke on the topic - {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate an explanation of the joke - {joke}',
    input_variables=['text']
)

joke_gen_chain = prompt1 | model | Parser

parallel_chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'Summary': RunnableSequence(prompt2,model,Parser)
})

merge_chain = joke_gen_chain | parallel_chain 
res = merge_chain.invoke({'topic':'AI'})
print(res['Joke'])
print(res['Summary'])
merge_chain.get_graph().print_ascii()