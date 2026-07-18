from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat_history = []

print("🤖 Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    chat_history.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": user_input
                }
            ]
        }
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_history
    )

    print("\nGemini:", response.text)
    print()

    chat_history.append(
        {
            "role": "model",
            "parts": [
                {
                    "text": response.text
                }
            ]
        }
    )