from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("Gemini_API_KEY")

client = genai.Client(api_key=gemini_api_key)

response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents = "What is coding?"
)

print(response.text)