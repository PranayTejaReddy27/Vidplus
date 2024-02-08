from googleapiclient.discovery import build

DEVELOPER_KEY = 'YOUR_API_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=5
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        video = {
            'title': search_result['snippet']['title'],
            'id': search_result['id']['videoId'],
            'url': f"https://www.youtube.com/watch?v={search_result['id']['videoId']}",
            'video_id': search_result['id']['videoId']
        }

        videos.append(video)
    return videos



