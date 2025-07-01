# scouts/yt_trending_scout.py

import feedparser
import pandas as pd
import streamlit as st

YT_TRENDING_FEEDS = {
    "MY": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=MY",
    "US": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=US",
    "IN": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=IN",
    "JP": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=JP",
    "UK": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=GB",
    "AU": "https://www.youtube.com/feeds/videos.xml?chart=mostPopular&regionCode=AU",
}

def fetch_yt_trending(region="MY", limit=10):
    """
    Fetch top trending YouTube videos using region-specific RSS feeds.
    No API key required. Returns DataFrame with title, published, and link.
    """
    feed_url = YT_TRENDING_FEEDS.get(region.upper())
    if not feed_url:
        st.warning(f"No RSS feed available for region: {region}")
        return pd.DataFrame()

    try:
        feed = feedparser.parse(feed_url)
        entries = feed.entries[:limit]
        records = [{
            "title": entry.title,
            "published": entry.get("published", entry.get("updated", None)),
            "channel": entry.get("author", "Unknown"),
            "url": entry.link
        } for entry in entries]

        df = pd.DataFrame(records)
        df["published"] = pd.to_datetime(df["published"])
        return df

    except Exception as e:
        st.error(f"❌ YouTube RSS fetch error: {e}")
        return pd.DataFrame()
