import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# DEVELOPMENT MODE
# =========================================================

# Keep this True while we are developing without
# OpenAI API credits.

DEVELOPMENT_MODE = True


# =========================================================
# OPENAI CONFIGURATION
# =========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = None

if not DEVELOPMENT_MODE and OPENAI_API_KEY:

    llm = ChatOpenAI(
        model="gpt-5.6-luna",
        temperature=0
    )


# =========================================================
# RESEARCH PROMPT
# =========================================================

research_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI research assistant helping an equity research analyst.

Analyze the provided news articles carefully.

Your response should follow this structure:

## Executive Summary

Provide a concise overview of the most important developments.

## Key Developments

List the 3-5 most significant news developments.

## Business & Market Implications

Explain how these developments could affect the company,
industry, investors, customers, or competitors.

## Positive Signals

Identify developments that may represent opportunities,
growth, or favorable business conditions.

## Risks & Concerns

Identify negative developments, uncertainties,
regulatory concerns, competition, or other risks.

## Analyst Takeaway

Provide a concise evidence-based conclusion.

Important instructions:

- Base factual claims only on the provided articles.
- Do not invent facts, numbers, events, or sources.
- Clearly distinguish facts from interpretation.
- If information is insufficient, say so.
- Do not provide financial advice.
- Maintain a professional equity-research tone.
"""
    ),
    (
        "human",
        """
Research Query:
{query}

News Articles:
{articles}

Prepare a professional research summary.
"""
    )
])


# =========================================================
# DEVELOPMENT MODE SUMMARY
# =========================================================

def create_demo_summary(query, articles):
    """
    Create a structured research summary without
    calling the OpenAI API.
    """

    titles = []
    sources = []

    for article in articles[:5]:

        title = article.get("title")

        if title:
            titles.append(title)

        source = article.get("source")

        if source and source not in sources:
            sources.append(source)


    summary = f"""
## Executive Summary

The search for **{query}** returned
**{len(articles)} relevant news articles**.

The application is currently running in
**Development Mode**, so no OpenAI API call is being made.
The information below is based directly on the retrieved
news articles.

## Key Developments

"""


    for i, title in enumerate(titles, start=1):

        summary += f"**{i}.** {title}\n\n"


    summary += """
## Business & Market Implications

The retrieved news can be reviewed to understand potential
effects on the company's operations, competitive position,
industry environment and market sentiment.

## Positive Signals

The retrieved articles may contain developments related to
growth, new opportunities, technological progress,
partnerships or favorable business conditions.

## Risks & Concerns

The articles may also contain operational, competitive,
regulatory or market-related risks.

## Analyst Takeaway

The current output is a development-mode research summary.
Users should review the original articles before drawing
business or investment conclusions.

"""


    if sources:

        summary += "## Sources\n\n"

        for source in sources:

            summary += f"- {source}\n"


    return summary


# =========================================================
# MAIN SUMMARIZATION FUNCTION
# =========================================================

def summarize_news(query, articles):
    """
    Generate a research summary.

    Development mode:
        Uses a local structured summary.

    Production mode:
        Uses OpenAI through LangChain.
    """

    if not articles:

        return "No relevant news articles were found."


    # -----------------------------------------------------
    # DEVELOPMENT MODE
    # -----------------------------------------------------

    if DEVELOPMENT_MODE:

        return create_demo_summary(
            query,
            articles
        )


    # -----------------------------------------------------
    # OPENAI MODE
    # -----------------------------------------------------

    if llm is None:

        return create_demo_summary(
            query,
            articles
        )


    formatted_articles = []


    for i, article in enumerate(
        articles,
        start=1
    ):

        formatted_articles.append(
            f"""
Article {i}

Title:
{article.get('title', 'N/A')}

Source:
{article.get('source', 'N/A')}

Published:
{article.get('publishedAt', 'N/A')}

Description:
{article.get('description', 'N/A')}

Content:
{article.get('content', 'N/A')}

URL:
{article.get('url', 'N/A')}
"""
        )


    articles_text = "\n".join(
        formatted_articles
    )


    messages = research_prompt.format_messages(
        query=query,
        articles=articles_text
    )


    try:

        response = llm.invoke(messages)

        return response.content


    except Exception as e:

        print(
            f"OpenAI unavailable: {e}"
        )

        return create_demo_summary(
            query,
            articles
        )