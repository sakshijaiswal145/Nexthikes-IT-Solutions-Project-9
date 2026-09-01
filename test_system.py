import pytest

from news_service import get_news_articles
from analytics_service import (
    analyze_sentiment,
    analyze_sources,
    generate_analytics
)


# =========================================================
# TEST 1 — NEWS RETRIEVAL
# =========================================================

def test_news_retrieval():

    articles = get_news_articles(
        "Tesla",
        page_size=3
    )

    assert isinstance(
        articles,
        list
    )


# =========================================================
# TEST 2 — ARTICLE STRUCTURE
# =========================================================

def test_article_structure():

    articles = get_news_articles(
        "Tesla",
        page_size=3
    )

    if articles:

        article = articles[0]

        assert isinstance(
            article,
            dict
        )

        assert "title" in article

        assert "url" in article


# =========================================================
# TEST 3 — SENTIMENT ANALYSIS
# =========================================================

def test_sentiment_analysis():

    sample_articles = [

        {
            "title": "Company reports strong growth",
            "description": "Revenue increased significantly.",
            "source": "Test Source"
        },

        {
            "title": "Company faces regulatory risk",
            "description": "Investigation raises concerns.",
            "source": "Test Source"
        },

        {
            "title": "Company announces new product",
            "description": "The company released a product.",
            "source": "Test Source"
        }

    ]


    result = analyze_sentiment(
        sample_articles
    )


    assert isinstance(
        result,
        dict
    )

    assert "Positive" in result

    assert "Negative" in result

    assert "Neutral" in result


# =========================================================
# TEST 4 — SOURCE ANALYSIS
# =========================================================

def test_source_analysis():

    sample_articles = [

        {
            "title": "Article 1",
            "source": "Reuters"
        },

        {
            "title": "Article 2",
            "source": "Reuters"
        },

        {
            "title": "Article 3",
            "source": "BBC"
        }

    ]


    result = analyze_sources(
        sample_articles
    )


    assert result["Reuters"] == 2

    assert result["BBC"] == 1


# =========================================================
# TEST 5 — COMPLETE ANALYTICS
# =========================================================

def test_generate_analytics():

    sample_articles = [

        {
            "title": "Strong revenue growth",
            "description": "Profit increased.",
            "source": "Reuters"
        },

        {
            "title": "Regulatory investigation",
            "description": "Company faces risks.",
            "source": "BBC"
        }

    ]


    result = generate_analytics(
        sample_articles
    )


    assert "sentiment" in result

    assert "sources" in result

    assert "positive_signals" in result

    assert "risk_signals" in result

    assert "overall_signal" in result

    # =========================================================
# TEST 6 — EMPTY ARTICLE LIST
# =========================================================

def test_empty_articles():

    result = generate_analytics([])

    assert result["sentiment"]["Positive"] == 0

    assert result["sentiment"]["Negative"] == 0

    assert result["sentiment"]["Neutral"] == 0

    assert result["overall_signal"] == "Neutral"