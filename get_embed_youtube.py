from googleapiclient.discovery import build
import os

import urllib.request
import json
import urllib


api_key = os.environ.get('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

yt_channel_request = youtube.channels().list(
    part='contentDetails',
    id='UCbjjRr-zfV6st2J_LBOhoHw'
)

yt_channel = yt_channel_request.execute()
uploads_id = yt_channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']

video_ids = []
video_titles = []
next_page_token = ''

while next_page_token is not None:
    yt_uploads_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=uploads_id,
        pageToken=next_page_token,
        maxResults=50
    )
    yt_uploads = yt_uploads_request.execute()
    for upload in yt_uploads['items']:
        video_ids.append(upload['contentDetails']['videoId'])

    try:
        next_page_token = yt_uploads['nextPageToken']
    except:
        next_page_token = None


for video_id in video_ids:
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        video_titles.append(data['title'])
