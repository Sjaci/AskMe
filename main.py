# Import required Libraries
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import  HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from pyboxen import boxen  #To make the chat look bit pretty !!!

# Loading the env variables
load_dotenv()

# Creating a instance of LLM
chat = ChatGoogleGenerativeAI(model="gemini-pro")

#Prompt template with Human message and history
prompt = ChatPromptTemplate(
    input_variables=["input", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

# Creating a Runnable Chain
chain = prompt | chat

# Creating a dict to store the messages:
store = {}  #TO DO: we can try storing the history in a stable location

#To get the history from above stored dict
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

#Creating a runnable with history
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history= get_session_history,
    input_messages_key="input",
    history_messages_key="messages"
)

while True:
    human_content = input(">> ")
    response = chain_with_memory.invoke(
        {"input":human_content},
        config={"configurable":{"session_id":"sample"}}  # TO DO: we can try switching different session Id
        )
    print(boxen(response.content, title = "AI Assistant"))

