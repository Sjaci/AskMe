# Import required Libraries
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import  HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.chains import LLMChain

# Loading the env variables
load_dotenv()

# Creating a instance of LLM
chat = ChatGoogleGenerativeAI(model="gemini-pro")

# Creates a buffer memory
memory = ConversationBufferMemory(
    return_messages = True,
    memory_key = "messages"
)

#Prompt template with Human message and history
prompt = ChatPromptTemplate(
    input_variables=["input", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

# Creating a chain; this is deprecated : to see the latest one see the ../main.py
chain = LLMChain(
        llm = chat,
        prompt = prompt,
        memory = memory
        )

while True:
    human_content = input(">> ")
    response = chain.predict(input=human_content)
    print(response)

