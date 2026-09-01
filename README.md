# 🔎 AI News Research Tool

An AI-powered news research application that retrieves relevant news articles using NewsAPI and transforms them into structured research insights through Python, Streamlit, and LangChain.

---

## 📌 Project Overview

The AI News Research Tool is designed to help users quickly research companies, industries, and business topics by collecting relevant news articles and presenting them in an easy-to-understand research dashboard.

The application combines real-time news retrieval, structured analysis, sentiment intelligence, source analysis, and research summarization into a single interactive interface.

---

## 🎯 Problem Statement

Researching a company or business topic manually requires searching multiple news websites, reading several articles, identifying important developments, and analyzing the overall sentiment.

This project aims to simplify that process by:

- Retrieving relevant news automatically
- Cleaning and structuring article information
- Analyzing article sentiment
- Identifying positive, negative, and neutral signals
- Providing an overall research signal
- Presenting results through an interactive dashboard

---

## ✨ Key Features

### 📰 News Retrieval

- Retrieves relevant news articles using NewsAPI
- Supports company, industry, and keyword searches
- Configurable number of articles
- Displays article title, source, publication date, and URL

### 📊 Research Dashboard

The dashboard provides:

- Number of articles retrieved
- Number of news sources
- Research topic
- Research time
- Executive summary
- Key developments
- News intelligence
- Source distribution

### 🧠 News Intelligence

The application categorizes news into:

- 🟢 Positive signals
- 🔴 Negative signals
- ⚪ Neutral signals

It also calculates an overall research signal based on the analyzed news.

### 📈 Analytics

The project provides analytical insights including:

- Sentiment distribution
- Source distribution
- Positive/negative/neutral news counts
- Overall research signal

### 🤖 AI Research Processing

LangChain and OpenAI integration are included for structured research summarization.

When OpenAI API credits are unavailable, the application can operate in Development Mode using the retrieved news data.

### 🔐 Secure API Configuration

API keys are stored using environment variables.

Sensitive files such as `.env` are excluded from Git using `.gitignore`.

---

## 🏗️ System Architecture

```text
                   ┌──────────────────────┐
                   │      User Input      │
                   │ Company / Topic      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │   Streamlit App      │
                   │       app.py         │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │   News Service       │
                   │   NewsAPI            │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Retrieved Articles   │
                   └──────────┬───────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
       ┌──────────────────┐       ┌──────────────────┐
       │ Analytics        │       │ Research Service │
       │ Service          │       │                  │
       └────────┬─────────┘       └────────┬─────────┘
                │                          │
                │                          ▼
                │                 ┌──────────────────┐
                │                 │ LLM Service      │
                │                 │ LangChain/OpenAI │
                │                 └────────┬─────────┘
                │                          │
                └────────────┬─────────────┘
                             ▼
                  ┌────────────────────────┐
                  │ Research Dashboard     │
                  │ Summary + Analytics    │
                  └────────────────────────┘