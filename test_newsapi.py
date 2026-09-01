import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

api_key = os.getenv("NEWSAPI_KEY")

newsapi = NewsApiClient(api_key=api_key)

response = newsapi.get_everything(
    q="Tesla",
    language="en",
    sort_by="relevancy",
    page_size=5
)

print("Status:", response["status"])
print("Total results:", response["totalResults"])

for article in response["articles"]:
    print("\nTitle:", article["title"])
    print("Source:", article["source"]["name"])