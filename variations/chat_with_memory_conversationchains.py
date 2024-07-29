from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import  HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.chains import ConversationChain

load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-pro")

memory = ConversationBufferMemory(
    return_messages = True,
    memory_key = "messages"
)

prompt = ChatPromptTemplate(
    input_variables=["input", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

chain = ConversationChain(
        llm = chat,
        prompt = prompt,
        memory = memory)

while True:
    human_content = input(">> ")
    response = chain.predict(input=human_content)
    print(response)

