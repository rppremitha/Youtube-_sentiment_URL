import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_sentiment_chart(df):
    sentiment_counts = df['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']
    fig = px.bar(sentiment_counts, x='Sentiment', y='Count', color='Sentiment', title='Sentiment Distribution')
    st.plotly_chart(fig)

def plot_emotion_chart(df):
    emotion_counts = df['Emotion'].value_counts().reset_index()
    emotion_counts.columns = ['Emotion', 'Count']
    fig = px.bar(emotion_counts, x='Emotion', y='Count', color='Emotion', title='Emotion Distribution')
    st.plotly_chart(fig)

def create_wordcloud(df):
    all_comments = ' '.join(df['Comment'].dropna().astype(str))
    if all_comments.strip():
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
    else:
        st.warning("No valid text available to generate word cloud.")
