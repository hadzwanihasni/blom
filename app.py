import streamlit as st
import pandas as pd
from scouts.scout_registry import SCOUT_REGISTRY
from scouts.trending_searches import fetch_trending_searches

# --- Setup ---
st.set_page_config(page_title="BLOM 🌐 Opportunity Radar", layout="wide")
st.title("🌱 BLOM – Signal Intelligence Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("🛰️ Filter Signals")
region = st.sidebar.selectbox("Region", ["MY", "US", "IN", "JP", "HK", "FR", "UK", "DE", "AU"])
timeframe = st.sidebar.selectbox("Timeframe", ["now 1-d", "now 7-d", "today 1-m", "today 3-m"])
mode = st.sidebar.radio("Keyword Mode", ["Trending (auto)", "Static (manual)"], index=0)

# --- Keyword Resolver ---
try:
    if mode == "Trending (auto)":
        kw_list = fetch_trending_searches(region=region, top_n=5)
        if not kw_list:
            raise ValueError("No trending keywords returned")
    else:
        custom_keywords = st.sidebar.text_input("Enter comma-separated keywords", value="AI,automation,python")
        kw_list = [kw.strip() for kw in custom_keywords.split(",") if kw.strip()]
except Exception as e:
    st.warning(f"⚠️ Error fetching trending keywords: {e}")
    kw_list = ["AI", "automation", "python"]

st.info(f"📊 Scouting keywords: {kw_list}")

# --- Toggle Scout Modules ---
st.sidebar.markdown("---")
st.sidebar.subheader("🧭 Active Scouts")

active_scouts = {}
for key, scout in SCOUT_REGISTRY.items():
    enabled = st.sidebar.checkbox(scout["label"], value=("⚠️" not in scout["label"]))
    if enabled:
        active_scouts[key] = scout

# --- Execute Enabled Scouts ---
for scout_key, scout in active_scouts.items():
    st.subheader(scout["label"])

    # Handle null or disabled scouts gracefully
    if scout["function"] is None:
        st.info(f"ℹ️ {scout['label']} is currently offline.")
        continue

    try:
        if scout_key == "google_trends":
            df = scout["function"](kw_list=kw_list, region=region, timeframe=timeframe)
            if df.empty:
                st.warning("⚠️ No Google Trends data.")
            else:
                st.line_chart(df.set_index("date"))

        elif scout_key == "trending_searches":
            keywords = scout["function"](region=region, top_n=5)
            st.write("Top Trending Keywords:", keywords)

        elif scout_key == "news":
            df = scout["function"]()
            if df.empty:
                st.warning("No news articles available.")
            else:
                st.dataframe(df[["pubDate", "title", "source"]].sort_values("pubDate", ascending=False))

        elif scout_key == "hackernews":
            if not kw_list:
                st.warning("⚠️ No keywords provided for Hacker News scout.")
                continue
            df = scout["function"](keywords=kw_list)
            if df.empty:
                st.warning("No Hacker News results.")
            else:
                st.dataframe(df[["posted", "title", "points", "keyword"]])

        elif scout_key == "youtube":
            df = scout["function"](region=region, limit=10)
            if df.empty:
                st.warning("No YouTube data.")
            else:
                st.dataframe(df[["published", "title", "channel"]])

        elif scout_key == "twitter":
            st.info("🐦 Twitter scout unavailable due to Python 3.13 incompatibility.")
            continue

        else:
            st.warning(f"⚠️ No display logic defined for scout: {scout['label']}")

    except Exception as e:
        st.error(f"❌ Error in '{scout['label']}': {e}")

# --- Footer ---
st.markdown("---")
st.caption("BLOM MVP | Hadzwani Hasni")
