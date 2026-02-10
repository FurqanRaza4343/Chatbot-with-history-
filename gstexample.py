from google import genai
from google.genai import types

client=genai.Client()
client = genai.Client(api_key="YOUR_API_KEY")

google_tool= types.Tool(
    google_search = types.GoogleSearch()
)

response=client.models.generate_content(
    model= "gemini-2.5-flash",
    contents= "Tell me about Future of AI",
    config=types.GenerateContentConfig(
    tools=[google_tool]
    )
)

print(response.text)