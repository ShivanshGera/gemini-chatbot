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

    # Save user message
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

    # Variable to store the complete response
    full_response = ""

    # Stream the response
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=chat_history
    )

    print("\nGemini: ", end="")

    # Print each chunk as it arrives
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    print("\n")

    # Save Gemini's response to chat history
    chat_history.append(
        {
            "role": "model",
            "parts": [
                {
                    "text": full_response
                }
            ]
        }
    )