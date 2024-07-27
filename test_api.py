from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Write a formal email to the Developer Lead to introduce Gemini API in the project")
print(response.text)