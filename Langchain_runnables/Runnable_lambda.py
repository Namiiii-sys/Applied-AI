from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def word_counter(text):
    return len(text.split())

Runnable_word_counter = RunnableLambda(word_counter)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

Parser = StrOutputParser()

prompt = PromptTemplate(
    template='Generate a joke on the topic - {topic}',
    input_variables=['topic']
)


joke_gen_chain = prompt | model | Parser

parallel_chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'Count': Runnable_word_counter
})

merge_chain = joke_gen_chain | parallel_chain 
res = merge_chain.invoke({'topic':'Dance'})
print(res['Joke'])
print("total words are: ", res['Count'])
merge_chain.get_graph().print_ascii()