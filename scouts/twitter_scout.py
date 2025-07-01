"""
🐦 Twitter Scout (snscrape-based)
NOTE: snscrape is not compatible with Python 3.13 as of July 2025.
Downgrade to Python 3.10 or 3.11 to activate this scout.

To enable:
1. pip install snscrape
2. Add 'twitter' back to SCOUT_REGISTRY
"""

# 🔒 Disabled by default
def fetch_twitter_trends(*args, **kwargs):
    return None

# --- Archived working logic (requires Python <= 3.11) ---
"""
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta

def fetch_twitter_trends(keyword="AI", max_results=30, days_back=1):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days_back)
    date_filter = f"since:{start_date.date()} until:{end_date.date()}"
    query = f"{keyword} {date_filter}"

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_results:
            break
        tweets.append({
            "date": tweet.date,
            "username": tweet.user.username,
            "content": tweet.content
        })

    return pd.DataFrame(tweets)
"""
