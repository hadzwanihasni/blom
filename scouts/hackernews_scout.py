import requests
import pandas as pd
import streamlit as st
from datetime import datetime

def fetch_hackernews_posts(keywords=None, hits_limit=3, min_points=30):
    """
    Fetch top Hacker News posts matching keywords using Algolia API.
    - keywords: list of terms to scan for
    - hits_limit: number of top hits per keyword
    - min_points: minimum upvotes to consider signal-worthy
    Returns a DataFrame with post details.
    """
    if not keywords:
        st.warning("⚠️ No keywords provided for Hacker News scout.")
        return pd.DataFrame()

    results = []

    for kw in keywords:
        try:
            url = f"https://hn.algolia.com/api/v1/search?query={kw}&tags=story&hitsPerPage=10"
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()

            for hit in data.get("hits", []):
                if hit.get("points", 0) < min_points:
                    continue  # filter low-impact posts

                results.append({
                    "keyword": kw,
                    "title": hit.get("title"),
                    "points": hit.get("points"),
                    "author": hit.get("author"),
                    "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                    "posted": datetime.fromtimestamp(hit.get("created_at_i")),
                })

        except Exception as e:
            st.error(f"❌ Failed to fetch Hacker News posts for '{kw}': {e}")

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results)
    return df.sort_values(by=["points", "posted"], ascending=[False, False]).head(hits_limit * len(keywords))
