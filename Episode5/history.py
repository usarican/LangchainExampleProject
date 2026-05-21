from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

sessionIdStore = {}

def get_session_id(session_id: str) -> BaseChatMessageHistory:
    if session_id not in sessionIdStore:
        sessionIdStore[session_id] = InMemoryChatMessageHistory()
    return sessionIdStore[session_id]

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages"),
    ])

chain = prompt_template | model
config = {"configurable" : {"session_id" : "sessionId1"}}
with_message_history = RunnableWithMessageHistory(chain,get_session_id)


if __name__ == "__main__":
    while True:
        user_input = input(">")
        response = with_message_history.invoke(
            [HumanMessage(content=user_input)],
            config=config
        )
        print(response)
