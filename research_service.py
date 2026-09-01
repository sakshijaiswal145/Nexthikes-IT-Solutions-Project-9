from news_service import get_news_articles
from llm_service import summarize_news


def conduct_research(query, page_size=10):
    """
    Complete research workflow.

    1. Fetch relevant news articles.
    2. Clean and deduplicate articles.
    3. Generate an AI-powered research summary.

    Parameters:
        query (str): Research topic or company.
        page_size (int): Number of articles to retrieve.

    Returns:
        dict: Articles and AI-generated summary.
    """

    # Validate query
    if not query or not query.strip():
        return {
            "query": query,
            "articles": [],
            "summary": "Please enter a valid research query."
        }

    query = query.strip()

    # Step 1: Fetch news
    articles = get_news_articles(
        query=query,
        page_size=page_size
    )

    # Step 2: Handle no results
    if not articles:
        return {
            "query": query,
            "articles": [],
            "summary": (
                f"No relevant news articles were found "
                f"for '{query}'."
            )
        }

    # Step 3: Generate AI summary
    summary = summarize_news(
        query=query,
        articles=articles
    )

    # Step 4: Return complete research result
    return {
        "query": query,
        "articles": articles,
        "summary": summary
    }