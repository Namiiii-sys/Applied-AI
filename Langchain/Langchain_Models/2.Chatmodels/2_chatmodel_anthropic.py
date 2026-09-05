from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='Claude-3.5-sonnet-20241022')
result = model.invoke("Whats the Captal of India?")

print(result.content)