import streamlit as st
from datetime import datetime
from html import escape

from research_service import conduct_research
from analytics_service import generate_analytics


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI News Research Tool",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main application */

    .main {
        padding-top: 1rem;
    }


    /* Header */

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        font-size: 17px;
        opacity: 0.75;
        margin-bottom: 25px;
    }


    /* KPI cards */

    .kpi-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
        min-height: 120px;
    }

    .kpi-label {
        font-size: 14px;
        opacity: 0.7;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }


    /* Article cards */

    .article-card {
        padding: 20px;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 16px;
    }

    .article-title {
        font-size: 20px;
        font-weight: 700;
        line-height: 1.4;
        margin-bottom: 8px;
    }

    .article-meta {
        font-size: 13px;
        opacity: 0.7;
        margin-bottom: 12px;
    }

    .article-description {
        font-size: 15px;
        line-height: 1.6;
    }


    /* Section headings */

    .section-heading {
        font-size: 27px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
    }


    /* Footer */

    .footer {
        text-align: center;
        opacity: 0.6;
        font-size: 13px;
        padding: 30px 0 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="hero-title">📰 AI News Research Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-subtitle">
    Transform real-time news into structured research insights.
    Search companies, industries and business topics in seconds.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Research Settings")

    page_size = st.slider(
        "Articles to retrieve",
        min_value=3,
        max_value=10,
        value=5,
        step=1
    )

    st.divider()

    st.subheader("🔍 Search Tips")

    st.write(
        """
        Try searches such as:

        • Tesla  
        • Apple  
        • NVIDIA  
        • Microsoft  
        • Electric vehicles  
        • Artificial intelligence  
        • Renewable energy
        """
    )

    st.divider()

    st.subheader("ℹ️ About")

    st.write(
        """
        This application retrieves relevant news using
        NewsAPI and processes the information through
        a modular research pipeline.
        """
    )

    st.info(
        "Development Mode is active. "
        "OpenAI API calls are disabled while API credits "
        "are unavailable."
    )


# =========================================================
# SEARCH AREA
# =========================================================

st.markdown(
    '<div class="section-heading">🔎 Research a Company or Topic</div>',
    unsafe_allow_html=True
)


query = st.text_input(
    "Search",
    placeholder="Example: Tesla, Apple, NVIDIA, AI industry...",
    label_visibility="collapsed"
)


search_button = st.button(
    "🚀 Research News",
    type="primary",
    use_container_width=True
)


# =========================================================
# RESEARCH EXECUTION
# =========================================================

if search_button:

    if not query.strip():

        st.warning(
            "Please enter a company or topic before searching."
        )

        st.stop()


    with st.spinner(
        f"Researching '{query.strip()}'..."
    ):

        try:

            result = conduct_research(
                query=query.strip(),
                page_size=page_size
            )

            st.session_state["research_result"] = result

        except Exception as e:

            st.error(
                "Something went wrong while retrieving the news."
            )

            st.caption(
                f"Technical details: {e}"
            )

            st.stop()


# =========================================================
# DISPLAY SAVED RESULTS
# =========================================================

if "research_result" in st.session_state:

    result = st.session_state["research_result"]

    articles = result.get("articles", [])

    summary = result.get(
        "summary",
        "No summary available."
    )

    analytics = generate_analytics(
        articles
    )

    research_query = result.get(
        "query",
        query
    )


    # =====================================================
    # KPI SECTION
    # =====================================================

    st.divider()

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    📰 Articles Found
                </div>
                <div class="kpi-value">
                    {len(articles)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        sources = set()

        for article in articles:

            source = article.get("source")

            if source:
                sources.add(source)

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    🏢 News Sources
                </div>
                <div class="kpi-value">
                    {len(sources)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    🔎 Research Topic
                </div>
                <div class="kpi-value">
                    {escape(research_query)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        current_time = datetime.now().strftime(
            "%H:%M"
        )

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">
                    🕐 Research Time
                </div>
                <div class="kpi-value">
                    {current_time}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # RESEARCH ANALYSIS
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-heading">📊 Research Analysis</div>',
        unsafe_allow_html=True
    )


    st.markdown(summary)

        # =====================================================
    # NEWS INTELLIGENCE
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-heading">'
        '🧠 News Intelligence'
        '</div>',
        unsafe_allow_html=True
    )


    sentiment = analytics["sentiment"]

    overall_signal = analytics[
        "overall_signal"
    ]


    # -----------------------------------------------------
    # Signal metrics
    # -----------------------------------------------------

    signal_col1, signal_col2, signal_col3, signal_col4 = (
        st.columns(4)
    )


    with signal_col1:

        st.metric(
            "🟢 Positive",
            sentiment["Positive"]
        )


    with signal_col2:

        st.metric(
            "🔴 Negative",
            sentiment["Negative"]
        )


    with signal_col3:

        st.metric(
            "⚪ Neutral",
            sentiment["Neutral"]
        )


    with signal_col4:

        st.metric(
            "Overall Signal",
            overall_signal
        )


    # -----------------------------------------------------
    # Source distribution
    # -----------------------------------------------------

    st.subheader(
        "🏢 Source Distribution"
    )


    source_data = analytics[
        "sources"
    ]


    if source_data:

        st.bar_chart(
            source_data
        )


    # -----------------------------------------------------
    # Positive and risk signals
    # -----------------------------------------------------

    insight_col1, insight_col2 = st.columns(2)


    with insight_col1:

        st.subheader(
            "🟢 Positive Signals"
        )


        positive_signals = analytics[
            "positive_signals"
        ]


        if positive_signals:

            for item in positive_signals[:5]:

                st.success(
                    item["title"]
                )

        else:

            st.info(
                "No strong positive signals "
                "were detected."
            )


    with insight_col2:

        st.subheader(
            "🔴 Risk Signals"
        )


        risk_signals = analytics[
            "risk_signals"
        ]


        if risk_signals:

            for item in risk_signals[:5]:

                st.warning(
                    item["title"]
                )

        else:

            st.info(
                "No strong risk signals "
                "were detected."
            )


    # =====================================================
    # FILTERS
    # =====================================================

    if articles:

        st.divider()

        st.markdown(
            '<div class="section-heading">🎛️ Filter Articles</div>',
            unsafe_allow_html=True
        )


        filter_col1, filter_col2 = st.columns(2)


        # -----------------------------------------------
        # Source filter
        # -----------------------------------------------

        with filter_col1:

            source_options = sorted(
                list(
                    {
                        article.get(
                            "source",
                            "Unknown"
                        )
                        for article in articles
                    }
                )
            )

            selected_source = st.selectbox(
                "Filter by source",
                ["All Sources"] + source_options
            )


        # -----------------------------------------------
        # Keyword filter
        # -----------------------------------------------

        with filter_col2:

            keyword = st.text_input(
                "Filter article titles",
                placeholder="Enter keyword..."
            )


        # -----------------------------------------------
        # Apply filters
        # -----------------------------------------------

        filtered_articles = []

        for article in articles:

            article_source = article.get(
                "source",
                "Unknown"
            )

            article_title = article.get(
                "title",
                ""
            )


            if (
                selected_source != "All Sources"
                and article_source != selected_source
            ):
                continue


            if (
                keyword.strip()
                and keyword.lower()
                not in article_title.lower()
            ):
                continue


            filtered_articles.append(article)


    else:

        filtered_articles = []


    # =====================================================
    # ARTICLE SECTION
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-heading">📰 Relevant News Articles</div>',
        unsafe_allow_html=True
    )


    if not articles:

        st.warning(
            f"No relevant articles were found for "
            f"'{research_query}'. Try another search."
        )


    elif not filtered_articles:

        st.info(
            "No articles match the selected filters."
        )


    else:

        st.caption(
            f"Showing {len(filtered_articles)} "
            f"of {len(articles)} retrieved articles."
        )


        for index, article in enumerate(
            filtered_articles,
            start=1
        ):

            title = article.get(
                "title",
                "Untitled Article"
            )

            description = article.get(
                "description",
                ""
            )

            source = article.get(
                "source",
                "Unknown Source"
            )

            published = article.get(
                "publishedAt",
                "Unknown date"
            )

            url = article.get(
                "url"
            )


            # Clean text for HTML
            safe_title = escape(str(title))

            safe_source = escape(str(source))

            safe_description = escape(
                str(description)
            )


            st.markdown(
                f"""
                <div class="article-card">

                    <div class="article-title">
                        {safe_title}
                    </div>

                    <div class="article-meta">
                        🏢 {safe_source}
                        &nbsp;&nbsp; | &nbsp;&nbsp;
                        📅 {published}
                    </div>

                    <div class="article-description">
                        {safe_description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            if url:

                st.link_button(
                    "🔗 Read Original Article",
                    url
                )


    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-heading">📥 Export Research</div>',
        unsafe_allow_html=True
    )


    report_text = f"""
AI NEWS RESEARCH REPORT
=======================

Research Query:
{research_query}

Articles Found:
{len(articles)}

----------------------------------------
RESEARCH ANALYSIS
----------------------------------------

{summary}


----------------------------------------
NEWS ARTICLES
----------------------------------------
"""


    for i, article in enumerate(
        articles,
        start=1
    ):

        report_text += f"""

Article {i}

Title:
{article.get("title", "N/A")}

Source:
{article.get("source", "N/A")}

Published:
{article.get("publishedAt", "N/A")}

Description:
{article.get("description", "N/A")}

URL:
{article.get("url", "N/A")}

----------------------------------------
"""


    st.download_button(
        label="📄 Download Research Report",
        data=report_text,
        file_name=f"{research_query.replace(' ', '_')}_research_report.txt",
        mime="text/plain"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
    AI News Research Tool • Built with Streamlit, NewsAPI,
    LangChain and OpenAI integration
    </div>
    """,
    unsafe_allow_html=True
)