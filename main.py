from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # loads GOOGLE_API_KEY from .env

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
response = llm.invoke("Hello, Gemini!")
print(response.content)