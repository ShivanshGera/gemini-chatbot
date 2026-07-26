from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""
    Analyze this student.

    Student knows:
    - Node.js
    - React
    - MongoDB
    """,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "OBJECT",
            "properties": {
                "skills": {
                    "type": "ARRAY",
                    "items": {
                        "type": "STRING"
                    }
                },
                "experience_level": {
                    "type": "STRING"
                },
                "career_path": {
                    "type": "STRING"
                }
            }
        }
    )
)

data = json.loads(response.text)

print(data)