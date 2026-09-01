import os
from dotenv import load_dotenv
from newsapi import NewsApiClient


# Load environment variables
load_dotenv()

# Get NewsAPI key securely
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

if not NEWSAPI_KEY:
    raise ValueError(
        "NEWSAPI_KEY not found. Please check your .env file."
    )

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)


def get_news_articles(query, page_size=10):
    """
    Fetch relevant news articles for a given search query.

    Parameters:
        query (str): Topic/company/keyword to search for.
        page_size (int): Number of articles to retrieve.

    Returns:
        list: Cleaned list of article dictionaries.
    """

    if not query or not query.strip():
        return []

    try:
        response = newsapi.get_everything(
            q=query.strip(),
            language="en",
            sort_by="relevancy",
            page_size=page_size,
            page=1
        )

        if response.get("status") != "ok":
            print("NewsAPI Error:", response)
            return []

        articles = response.get("articles", [])

        cleaned_articles = []

        for article in articles:

            # Skip articles without a title
            if not article.get("title"):
                continue

            cleaned_article = {
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article.get("source", {}).get(
                    "name", "Unknown"
                ),
                "author": article.get("author"),
                "publishedAt": article.get("publishedAt"),
                "url": article.get("url"),
                "urlToImage": article.get("urlToImage"),
                "content": article.get("content")
            }

            cleaned_articles.append(cleaned_article)

        return cleaned_articles

    except Exception as e:
        print(f"Error while fetching news: {e}")
        return []