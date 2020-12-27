from googleapiclient.discovery import build
import os


api_key = os.environ.get('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

yt_channel_request = youtube.channels().list(
    part='contentDetails',
    id='UCbjjRr-zfV6st2J_LBOhoHw'
)

yt_channel = yt_channel_request.execute()
uploads_id = yt_channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']

video_ids = []
next_page_token = ''

while next_page_token is not None:
    yt_uploads_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PLapw9YE9vAEEMMfVqRLF1ucbsXlyUbYht', # this is the featured playlist, change as necessary
        pageToken=next_page_token,
        maxResults=20
    )
    yt_uploads = yt_uploads_request.execute()
    for upload in yt_uploads['items']:
        video_ids.append(upload['contentDetails']['videoId'])

    try:
        next_page_token = yt_uploads['nextPageToken']
    except:
        next_page_token = None

