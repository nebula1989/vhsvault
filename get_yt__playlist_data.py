import os
import googleapiclient.discovery
import googleapiclient.errors


def main():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.environ.get('YT_API_KEY')
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    request = youtube.playlists().list(part="snippet,contentDetails", channelId="UCbjjRr-zfV6st2J_LBOhoHw", maxResults=25)
    response = request.execute()

    titles = get_playlist_titles(response)
    descriptions = get_playlist_descriptions(response)

    display(titles, descriptions)


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


def display(t, d):
    print(t)
    print(d)


if __name__ == '__main__':
    main()
