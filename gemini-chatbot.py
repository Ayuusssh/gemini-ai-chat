import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the API key for Google Generative AI
genai.configure(api_key=API_KEY)

# Initialize Gemini model and start chat
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Welcome to the chat! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Gemini: ", response.text)