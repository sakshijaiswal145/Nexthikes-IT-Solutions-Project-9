from research_service import conduct_research


print("=" * 70)
print("AI NEWS RESEARCH TOOL")
print("=" * 70)

query = "Tesla"

print(f"\nResearch Query: {query}")
print("\nFetching latest relevant news...")

result = conduct_research(
    query=query,
    page_size=5
)

print("\n" + "=" * 70)
print("ARTICLES FOUND")
print("=" * 70)

print(f"Number of articles: {len(result['articles'])}")

for i, article in enumerate(
    result["articles"],
    start=1
):

    print(f"\n{i}. {article['title']}")
    print(f"   Source: {article['source']}")
    print(f"   Published: {article['publishedAt']}")
    print(f"   URL: {article['url']}")


print("\n" + "=" * 70)
print("AI RESEARCH SUMMARY")
print("=" * 70)

print(result["summary"])

print("\n" + "=" * 70)
print("RESEARCH COMPLETED")
print("=" * 70)