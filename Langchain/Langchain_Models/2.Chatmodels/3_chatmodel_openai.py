from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)
result = model.invoke("Whats the Captal of India?")

print(result.content)