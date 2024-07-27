from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import  HumanMessagePromptTemplate, ChatPromptTemplate

load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-pro")


prompt = ChatPromptTemplate(
    input_variables=["human_content"],
    messages = [
        HumanMessagePromptTemplate.from_template("{human_content}")
    ]
)

chain = prompt | chat

while True:
    human_content = input(">> ")
    response = chain.invoke({"human_content": human_content})
    print(response.content)

