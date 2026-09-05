from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview', dimensions=32)

documents = [
    "Delhi is the Capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the Capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))