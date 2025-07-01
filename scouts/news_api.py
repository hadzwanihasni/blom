import feedparser
import pandas as pd
import streamlit as st

def fetch_top_news(feed_url="https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", limit=5):
    """
    Fetch recent news headlines using RSS feed. No API key required.
    Returns a DataFrame of headlines, dates, and summaries.
    """
    try:
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            st.warning("⚠️ No RSS entries found.")
            return pd.DataFrame()

        entries = feed.entries[:limit]
        records = [{
            "title": entry.title,
            "pubDate": entry.published,
            "summary": entry.summary,
            "source": feed.feed.get("title", "Unknown")
        } for entry in entries]

        df = pd.DataFrame(records)
        df["pubDate"] = pd.to_datetime(df["pubDate"])
        return df

    except Exception as e:
        st.error(f"❌ Failed to fetch RSS news: {e}")
        return pd.DataFrame()