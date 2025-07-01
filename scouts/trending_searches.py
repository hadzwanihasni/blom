from pytrends.request import TrendReq
import pandas as pd
import streamlit as st

REGION_MAP = {
    "MY": "united_states",        # Patch to US to avoid 404, approximation if available singapore
    "US": "united_states",
    "IN": "india",
    "JP": "japan",
    "HK": "hong_kong",
    "FR": "france",
    "UK": "united_kingdom",
    "DE": "germany",
    "AU": "australia",
}

def fetch_trending_searches(region="US", top_n=5):
    """
    Fetch trending search keywords from Google Trends by region.
    Returns a list of top N keywords or an empty list on failure.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    google_region = REGION_MAP.get(region.upper(), "united_states")

    try:
        trending_df = pytrends.trending_searches(pn=google_region)
        if trending_df.empty:
            st.warning(f"⚠️ No trending searches found for region: {region} (mapped to {google_region})")
            return []
        return trending_df[0].head(top_n).tolist()

    except Exception as e:
        st.error(f"❌ Error fetching trending searches: {e}")
        return []
