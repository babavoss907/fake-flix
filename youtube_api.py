import requests
import os

API_KEY = os.getenv("API_KEY")
API_URL = 'https://www.googleapis.com/youtube/v3'

# youtube_api.py

def get_videos_by_category(category):
    params = {
        'part': 'snippet,statistics',
        'chart': 'mostPopular',
        'maxResults': 10,
        'videoCategoryId': category,
        'type': 'video',
        'key': API_KEY
    }
    response = requests.get(f'{API_URL}/videos', params=params)
    data = response.json()
    return data['items']

