# AskMe : A minimal ChatBot
A ChatBot created with the help of LangChain and Gemini API.
This is a test project created as part of my learning on LangChain and LLM's.

## Pre-requisites
Make sure to have the following before starting:
1. Required Libraries: (will add them as I go)
     - python-dotenv (Using this library to secure my API Key; we can also use Colab Secrets or any other)
   ```
   pip3 install python-dotenv
   ```
     - langchain
   ```
   pip3 install langchain
   ```
     - Google Generative AI (to access the Genini's functions)
   ```
   pip3 install google-generativeai
   ```
     - langchain-google-genai
   ```
   pip3 install langchain-google-genai
   ```
2. API Key:
        After getting the API key from the Gemini API website, add them in a `.env` file.
   ```
   GOOGLE_API_KEY=<ENTER_YOUR_API_KEY>
   ```
   
> [!CAUTION]
> Do not checkin the `.env` file or expose them to public as it has the API Key.

To check whether Gemini API is working, you can run the curl coommand as given when creating the key or you can run this `test_api.py`:
```
python3 test_api.py
```
