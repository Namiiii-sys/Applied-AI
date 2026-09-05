from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert.'),
    ('human','Help me understand the {topic} in simple terms')
])

prompt = chat_template.invoke({"domain":"medical","topic":"Respiration process"})

print(prompt)