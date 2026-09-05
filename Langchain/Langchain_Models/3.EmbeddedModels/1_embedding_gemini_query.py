from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview', dimensions=32)

result = embedding.embed_query("Delhi si the Capital of India")

print(str(result))