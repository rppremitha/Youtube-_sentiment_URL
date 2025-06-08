import sqlite3
import pandas as pd

DB_NAME = "youtube_sentiment.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT,
            comment TEXT,
            sentiment TEXT,
            emotion TEXT,
            emoji TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_comment(video_id, comment, sentiment, emotion, emoji):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO comments (video_id, comment, sentiment, emotion, emoji)
        VALUES (?, ?, ?, ?, ?)
    ''', (video_id, comment, sentiment, emotion, emoji))
    conn.commit()
    conn.close()

def get_all_comments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comments")
    data = cursor.fetchall()
    conn.close()
    return data

def get_all_comments_df():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM comments", conn)
    conn.close()
    return df

def clear_all_comments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comments")
    conn.commit()
    conn.close()