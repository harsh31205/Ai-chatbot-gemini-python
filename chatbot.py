from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Gemini AI Chatbot started (type exit to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chat.send_message(user)

    print("\nBot:", response.text, "\n")