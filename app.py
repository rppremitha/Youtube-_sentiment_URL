""# app.py

import streamlit as st
import pandas as pd
from utils import extract_video_id
from youtube_utils import get_comments
from analysis import analyze_comment
from database import init_db, insert_comment, get_all_comments_df, clear_all_comments
from visualization import plot_sentiment_chart, plot_emotion_chart, create_wordcloud

# Initialize DB
init_db()

st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="wide")
st.title("\U0001F4FA YouTube Comment Sentiment & Emotion Analyzer")

api_key = st.sidebar.text_input("Enter your YouTube API Key", type="password")
video_url = st.sidebar.text_input("Enter a YouTube Video URL")

if st.sidebar.button("Analyze Video"):
    if not api_key or not video_url:
        st.error("Please provide both the API key and video URL.")
    else:
        video_id = extract_video_id(video_url)
        with st.spinner("Fetching comments..."):
            comments = get_comments(video_id, api_key)

        if not comments:
            st.warning("No comments found or video is private/restricted.")
        else:
            results = []
            for comment in comments:
                sentiment, emoji, emotion = analyze_comment(comment)
                insert_comment(video_id, comment, sentiment, emotion, emoji)
                results.append({
                    "Comment": comment,
                    "Sentiment": sentiment,
                    "Emoji": emoji,
                    "Emotion": emotion
                })

            df = pd.DataFrame(results)
            st.subheader("Comment Analysis")
            st.dataframe(df)

            st.subheader("Sentiment Distribution")
            plot_sentiment_chart(df)

            st.subheader("Emotion Distribution")
            plot_emotion_chart(df)

            st.subheader("Word Cloud")
            create_wordcloud(df)

# View past records
st.markdown("---")
st.subheader("Past Analyses")
col1, col2 = st.columns(2)

with col1:
    if st.button("Clear All Records"):
        clear_all_comments()
        st.success("Database cleared.")

with col2:
    df_hist = get_all_comments_df()
    if not df_hist.empty:
        csv = df_hist.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="history.csv", mime="text/csv")

if not df_hist.empty:
    st.dataframe(df_hist)
else:
    st.info("No data found.")
