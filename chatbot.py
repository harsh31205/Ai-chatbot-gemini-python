from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("KEY:", key[:8] if key else "NO KEY")

client = genai.Client(
    api_key=key
)

chat = client.chats.create(
    model="gemini-2.5-flash"
)


def get_response(message):
    response = chat.send_message(message)
    return response.text