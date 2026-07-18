from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Store conversation history
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

    # Variable to store complete AI response
    full_response = ""

    # Generate streaming response with system instruction
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=chat_history,
        config=types.GenerateContentConfig(
            system_instruction="""
            You are an expert AI tutor.

            Your job is to teach programming and AI concepts.

            Rules:
            - Explain everything in simple language.
            - Use real-world examples.
            - Keep answers concise.
            - If the topic is technical, explain step by step.
            - Be friendly and encouraging.
            """
        )
    )

    print("\nGemini: ", end="")

    # Print response as it streams
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    print("\n")

    # Save model response
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