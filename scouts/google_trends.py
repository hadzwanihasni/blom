from pytrends.request import TrendReq
import pandas as pd
import streamlit as st
import time

def fetch_google_trends(kw_list, region="US", timeframe="now 7-d"):
    """
    Fetch interest over time for a list of keywords using Google Trends.
    Returns a DataFrame indexed by date.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    df_result = pd.DataFrame()

    for keyword in kw_list:
        try:
            pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=region)
            time.sleep(1)  # Mitigate risk of 429 Too Many Requests
            df = pytrends.interest_over_time()

            if df.empty:
                st.warning(f"⚠️ No data for keyword: {keyword}")
                continue

            df = df[[keyword]].rename(columns={keyword: keyword.lower()})
            df.index.name = "date"
            df.reset_index(inplace=True)

            if df_result.empty:
                df_result = df
            else:
                df_result = pd.merge(df_result, df, on="date", how="outer")

        except Exception as e:
            st.error(f"❌ Error fetching trend for {keyword}: {e}")
            continue

    if df_result.empty:
        return pd.DataFrame()

    df_result.sort_values("date", inplace=True)
    df_result.fillna(0, inplace=True)
    return df_result
