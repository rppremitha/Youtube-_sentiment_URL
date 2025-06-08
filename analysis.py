# analysis.py

from textblob import TextBlob
import emoji

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def get_emotion(text):
    # Basic emotion detection using keywords — replace with BERT later
    emotions = {
        "joy": ["happy", "joy", "excited", "glad", "awesome"],
        "sadness": ["sad", "disappointed", "unhappy", "depressed"],
        "anger": ["angry", "mad", "furious", "annoyed"],
        "fear": ["afraid", "scared", "fearful"],
    }
    text_lower = text.lower()
    for emotion, keywords in emotions.items():
        if any(word in text_lower for word in keywords):
            return emotion
    return "neutral"

def get_emoji(sentiment):
    return {
        "Positive": "😊",
        "Negative": "😠",
        "Neutral": "😐"
    }.get(sentiment, "❓")

def analyze_comment(comment):
    sentiment = get_sentiment(comment)
    emotion = get_emotion(comment)
    emoji_icon = get_emoji(sentiment)
    return sentiment, emotion, emoji_icon
