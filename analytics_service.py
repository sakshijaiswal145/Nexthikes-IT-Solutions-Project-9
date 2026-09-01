from collections import Counter


# =========================================================
# KEYWORD GROUPS
# =========================================================

POSITIVE_KEYWORDS = [
    "growth",
    "profit",
    "profits",
    "revenue",
    "surge",
    "increase",
    "increased",
    "positive",
    "success",
    "successful",
    "launch",
    "launched",
    "expansion",
    "expand",
    "partnership",
    "investment",
    "invest",
    "record",
    "strong",
    "improved",
    "improvement",
    "innovation",
    "demand",
    "deal",
    "agreement"
]


NEGATIVE_KEYWORDS = [
    "loss",
    "losses",
    "decline",
    "declined",
    "drop",
    "dropped",
    "fall",
    "fell",
    "negative",
    "risk",
    "risks",
    "lawsuit",
    "investigation",
    "regulatory",
    "regulation",
    "recall",
    "layoff",
    "layoffs",
    "cut",
    "cuts",
    "crisis",
    "concern",
    "concerns",
    "warning",
    "fraud",
    "controversy",
    "competition"
]


# =========================================================
# ARTICLE TEXT
# =========================================================

def get_article_text(article):
    """
    Combine article title and description
    for keyword analysis.
    """

    title = article.get("title", "") or ""

    description = article.get(
        "description", ""
    ) or ""

    return (
        f"{title} {description}"
    ).lower()


# =========================================================
# SENTIMENT CLASSIFICATION
# =========================================================

def classify_article_sentiment(article):
    """
    Classify an article as Positive, Negative,
    or Neutral using keyword-based analysis.
    """

    text = get_article_text(article)

    positive_score = sum(
        text.count(keyword)
        for keyword in POSITIVE_KEYWORDS
    )

    negative_score = sum(
        text.count(keyword)
        for keyword in NEGATIVE_KEYWORDS
    )

    if positive_score > negative_score:

        return "Positive"

    elif negative_score > positive_score:

        return "Negative"

    return "Neutral"


# =========================================================
# SENTIMENT ANALYSIS
# =========================================================

def analyze_sentiment(articles):
    """
    Calculate sentiment distribution across articles.
    """

    sentiments = []

    for article in articles:

        sentiment = classify_article_sentiment(
            article
        )

        sentiments.append(sentiment)

    counts = Counter(sentiments)

    return {
        "Positive": counts.get(
            "Positive", 0
        ),
        "Negative": counts.get(
            "Negative", 0
        ),
        "Neutral": counts.get(
            "Neutral", 0
        )
    }


# =========================================================
# SOURCE ANALYSIS
# =========================================================

def analyze_sources(articles):
    """
    Count articles by news source.
    """

    sources = []

    for article in articles:

        source = article.get(
            "source",
            "Unknown"
        )

        if source:
            sources.append(source)

    return dict(
        Counter(sources)
    )


# =========================================================
# POSITIVE SIGNALS
# =========================================================

def get_positive_signals(articles):
    """
    Return articles containing positive
    business-related keywords.
    """

    positive_articles = []

    for article in articles:

        text = get_article_text(
            article
        )

        score = sum(
            text.count(keyword)
            for keyword in POSITIVE_KEYWORDS
        )

        if score > 0:

            positive_articles.append({
                "title": article.get(
                    "title",
                    "Untitled"
                ),
                "score": score,
                "source": article.get(
                    "source",
                    "Unknown"
                )
            })

    return sorted(
        positive_articles,
        key=lambda x: x["score"],
        reverse=True
    )


# =========================================================
# RISK SIGNALS
# =========================================================

def get_risk_signals(articles):
    """
    Return articles containing negative
    or risk-related keywords.
    """

    risk_articles = []

    for article in articles:

        text = get_article_text(
            article
        )

        score = sum(
            text.count(keyword)
            for keyword in NEGATIVE_KEYWORDS
        )

        if score > 0:

            risk_articles.append({
                "title": article.get(
                    "title",
                    "Untitled"
                ),
                "score": score,
                "source": article.get(
                    "source",
                    "Unknown"
                )
            })

    return sorted(
        risk_articles,
        key=lambda x: x["score"],
        reverse=True
    )


# =========================================================
# OVERALL SIGNAL
# =========================================================

def get_overall_signal(sentiment):
    """
    Determine an overall news signal.
    """

    positive = sentiment.get(
        "Positive",
        0
    )

    negative = sentiment.get(
        "Negative",
        0
    )

    neutral = sentiment.get(
        "Neutral",
        0
    )


    if positive > negative:

        return "Positive"

    elif negative > positive:

        return "Negative"

    return "Neutral"


# =========================================================
# COMPLETE ANALYTICS
# =========================================================

def generate_analytics(articles):
    """
    Generate all analytical metrics
    for the retrieved news.
    """

    sentiment = analyze_sentiment(
        articles
    )

    sources = analyze_sources(
        articles
    )

    positive_signals = get_positive_signals(
        articles
    )

    risk_signals = get_risk_signals(
        articles
    )

    overall_signal = get_overall_signal(
        sentiment
    )

    return {
        "sentiment": sentiment,
        "sources": sources,
        "positive_signals": positive_signals,
        "risk_signals": risk_signals,
        "overall_signal": overall_signal
    }