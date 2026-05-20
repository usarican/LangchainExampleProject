from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.1)

class OutputMessage(BaseModel):
    userMessage: str = Field(description="The message the user said")
    llmResponse: str = Field(description="Your answer")

parser = JsonOutputParser(pydantic_object=OutputMessage)
format_instructions = parser.get_format_instructions()

messages = [
    SystemMessage(content=(
        "You are a translation expert for Turkish and English. "
        "Translate the user input.\n\n"
        f"{format_instructions}"
    )),
    HumanMessage(content="Hello, How are you?"),
]

if __name__ == "__main__":
    chain = model | parser
    response = chain.invoke(messages)
    print(response)