import os
import googleapiclient.discovery
import googleapiclient.errors
from pprint import pprint


def get_playlist_data(response_dict):
    # playlist data dictionary : [id, title, description]

    playlist_data_dict_list = response_dict['items']

    return playlist_data_dict_list


def display(data):
    pprint(data)


api_service_name = "youtube"
api_version = "v3"
api_key = os.environ.get('YT_API_KEY')
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
request = youtube.playlists().list(part="id,snippet,contentDetails", channelId="UCbjjRr-zfV6st2J_LBOhoHw", maxResults=50)
response = request.execute()

yt_playlist_data = get_playlist_data(response)
amount_of_playlists = len(yt_playlist_data)



"""

def get_playlist_titles(response_dict):
    playlist_titles = []
    for i in range(len(response_dict)):
        playlist_titles.append(response_dict['items'][i]['snippet']['localized']['title'])

    return playlist_titles


def get_playlist_descriptions(response_dict):
    playlist_descriptions = []
    for i in range(len(response_dict)):
        playlist_descriptions.append(response_dict['items'][i]['snippet']['localized']['description'])

    return playlist_descriptions

"""