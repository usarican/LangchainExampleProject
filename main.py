from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.1)

messages = [
    SystemMessage(content="You are translator expert Turkish to English and English to Turkish, Translate the user input"),
    HumanMessage(content="Hello, How are you?"),
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)