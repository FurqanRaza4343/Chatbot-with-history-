from google import genai
from google.genai import types

# GEMINI_API_KEY = "AIzaSyAU5N8tdKT2a9kO8F3J90QG8gT9JgurB90"

client = genai.Client(api_key=YOUR_API_KEY)

print("Chat start here.... type 'endchat' to close ")
chat = []
userinput = input("User : ")

while userinput != "endchat":
    chat.append(userinput)

    systemoutput = client.models.generate_content(
        contents= chat,
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="Answer in 2 line within 100 characters"
        )
    )

    chat.append("Statebot:"+ systemoutput.text)

    print("Statbot :", systemoutput.text)

    userinput = input("User : ")
