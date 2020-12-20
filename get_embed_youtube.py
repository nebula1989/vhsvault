from googleapiclient.discovery import build

api_key = 'AIzaSyAVYW6lTK4vX324BV3woS_HqNpLHpf_p2A'
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
