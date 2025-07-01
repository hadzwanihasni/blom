# context.py

import streamlit as st
from scouts.trending_searches import fetch_trending_searches

def resolve_keyword_context(mode="Trending (auto)", region="MY"):
    try:
        if mode == "Trending (auto)":
            kw_list = fetch_trending_searches(region=region, top_n=5)
            if not kw_list:
                raise ValueError("No keywords returned")
            return kw_list

        elif mode == "Static (manual)":
            custom_keywords = st.sidebar.text_input("Enter comma-separated keywords", value="AI,automation,python")
            return [kw.strip() for kw in custom_keywords.split(",") if kw.strip()]

    except Exception as e:
        st.warning(f"⚠️ Keyword fallback due to error: {e}")
        return ["AI", "automation", "python"]
