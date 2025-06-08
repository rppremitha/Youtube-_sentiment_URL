# utils.py

import re

def extract_video_id(url):
    """
    Extracts the YouTube video ID from a URL
    """
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None
