# scouts/reddit_scout.py

import requests
import pandas as pd
import streamlit as st
from datetime import datetime

def fetch_reddit_trends_batch(subreddits=["technology", "Futurology", "Artificial"], limit=5):
    """
    Fetch top posts from multiple subreddits using Pushshift API.
    Returns a combined DataFrame with subreddit column.
    """
    all_records = []

    for sub in subreddits:
        url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={sub}&sort=desc&sort_type=score&size={limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json().get("data", [])

            for post in data:
                all_records.append({
                    "subreddit": sub,
                    "title": post.get("title"),
                    "score": post.get("score", 0),
                    "date": datetime.utcfromtimestamp(post.get("created_utc")),
                    "link": f"https://reddit.com{post.get('permalink')}"
                })

        except Exception as e:
            st.warning(f"⚠️ Reddit scout error for r/{sub}: {e}")
            continue

    if not all_records:
        return pd.DataFrame()

    df = pd.DataFrame(all_records)
    return df.sort_values(by=["subreddit", "score"], ascending=[True, False])
