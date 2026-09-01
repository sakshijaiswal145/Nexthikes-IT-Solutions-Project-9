from news_service import get_news_articles
from analytics_service import generate_analytics


print("=" * 60)
print("NEWS ANALYTICS TEST")
print("=" * 60)


query = "Tesla"


print(f"\nSearching for: {query}")

articles = get_news_articles(
    query,
    page_size=5
)


print(
    f"Articles retrieved: {len(articles)}"
)


analytics = generate_analytics(
    articles
)


print("\n" + "=" * 60)
print("SENTIMENT")
print("=" * 60)

print(
    analytics["sentiment"]
)


print("\n" + "=" * 60)
print("OVERALL SIGNAL")
print("=" * 60)

print(
    analytics["overall_signal"]
)


print("\n" + "=" * 60)
print("NEWS SOURCES")
print("=" * 60)

for source, count in analytics[
    "sources"
].items():

    print(
        f"{source}: {count}"
    )


print("\n" + "=" * 60)
print("POSITIVE SIGNALS")
print("=" * 60)

for item in analytics[
    "positive_signals"
]:

    print(
        f"- {item['title']}"
    )


print("\n" + "=" * 60)
print("RISK SIGNALS")
print("=" * 60)

for item in analytics[
    "risk_signals"
]:

    print(
        f"- {item['title']}"
    )