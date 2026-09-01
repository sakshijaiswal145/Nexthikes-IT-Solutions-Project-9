from news_service import get_news_articles


print("Fetching news about Tesla...\n")

articles = get_news_articles("Tesla", page_size=5)

print(f"Articles received: {len(articles)}")

for i, article in enumerate(articles, start=1):

    print("\n" + "=" * 60)

    print(f"Article {i}")
    print("Title:", article["title"])
    print("Source:", article["source"])
    print("Published:", article["publishedAt"])
    print("URL:", article["url"])