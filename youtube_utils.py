# youtube_utils.py

from googleapiclient.discovery import build

def get_comments(video_id, api_key, max_results=100):
    youtube = build("youtube", "v3", developerKey=api_key)
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(max_results, 100),
        textFormat="plainText"
    )
    response = request.execute()

    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments
