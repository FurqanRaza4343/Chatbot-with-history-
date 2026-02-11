from google import genai
from google.genai import types

# API key yahan do agar env variable nahi use kar rahe
client = genai.Client()
client = genai.Client(api_key="YOU_API_KEY") # paste your API key here....

# Chat create (history auto handle hoti hai)
chat = client.chats.create(model="gemini-2.5-flash-lite")

print("Chat here... type 'endchat' to close")

userinput = input("User : ")

while userinput != "endchat":

    response = chat.send_message(userinput)
    # print("Statbot :", response.text)
    userinput = input("User : ")
for message in chat.get_history():
    print(f"role- {message.role}")
    print(message.parts[0].text)