# TEST = 1

import pyttsx3

engine = pyttsx3.init()

engine.say("First sentence")
engine.runAndWait()

print("First finished")

engine = pyttsx3.init()

engine.say("Second sentence")
engine.runAndWait()

print("Second finished")


# TEST = 2

# from dotenv import load_dotenv
# import os

# load_dotenv()

# openai_api_key = os.getenv("OpenAI_API_KEY")
# news_api_key = os.getenv("News_API_KEY")

# print("OpenAI key loaded:", bool(openai_api_key))
# print("News key loaded:", bool(news_api_key))


# TEST = 3

# from dotenv import load_dotenv
# import os
# import requests

# load_dotenv()

# news_api_key = os.getenv("News_API_KEY")

# r = requests.get(
#     f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}",
#     timeout=10
# )

# print("Status:", r.status_code)
# print("Response:")
# print(r.json())