from scouts.news_api import fetch_top_news
from scouts.hackernews_scout import fetch_hackernews_posts
from scouts.yt_trending_scout import fetch_yt_trending

# Disabled / Offline Scouts
from scouts.twitter_scout import fetch_twitter_trends  # ⚠️ Not available on Python 3.13
from scouts.google_trends import fetch_google_trends   # ⚠️ Error 429: rate-limited
from scouts.trending_searches import fetch_trending_searches  # ⚠️ Error 404

SCOUT_REGISTRY = {
    "news": {
        "label": "🗞️ News Headlines",
        "function": fetch_top_news
    },
    "hackernews": {
        "label": "🧠 Hacker News Signals",
        "function": fetch_hackernews_posts
    },
    "youtube": {
        "label": "📺 YouTube Trending",
        "function": fetch_yt_trending
    },
    "google_trends": {
        "label": "📈 Google Trends (⚠️ Unstable)",
        "function": fetch_google_trends
    },
    "trending_searches": {
        "label": "📊 Google Searches (⚠️ Unstable)",
        "function": fetch_trending_searches
    },
    "twitter": {
        "label": "🐦 X Trends (⚠️ Unavailable on Python 3.13)",
        "function": fetch_twitter_trends
    }
}
