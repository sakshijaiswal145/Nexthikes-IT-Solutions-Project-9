import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
newsapi_key = os.getenv("NEWSAPI_KEY")

print("OpenAI key loaded:", bool(openai_key))
print("NewsAPI key loaded:", bool(newsapi_key))