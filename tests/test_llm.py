from llm_service import summarize_news


test_articles = [
    {
        "title": "Tesla announces major new developments",
        "source": "Test Source",
        "publishedAt": "2026-08-31",
        "description": (
            "Tesla announced several developments "
            "related to its business operations."
        ),
        "content": (
            "The company discussed new initiatives "
            "and future business plans."
        ),
        "url": "https://example.com"
    },
    {
        "title": "Tesla reports changes in its market strategy",
        "source": "Test Source 2",
        "publishedAt": "2026-08-31",
        "description": (
            "Tesla is adjusting aspects of its "
            "business strategy."
        ),
        "content": (
            "The company is focusing on growth "
            "and operational efficiency."
        ),
        "url": "https://example.com"
    }
]


print("Testing OpenAI + LangChain...\n")

summary = summarize_news(
    query="Tesla",
    articles=test_articles
)

print("=" * 70)
print("AI RESEARCH SUMMARY")
print("=" * 70)
print(summary)