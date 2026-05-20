from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.1)
parser = StrOutputParser()

system_prompt = "Translate the user sentence to {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)

chain = prompt_template | model | parser


if __name__ == "__main__":
    response = chain.invoke({"language":"en","text" : "İyi Günler"})
    print(response)