from flask import Flask, render_template
import get_embed_youtube
import get_yt__playlist_data


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/videos')
def video():
    return render_template('videos.html', video_ids=get_embed_youtube.video_ids, playlist_data=get_yt__playlist_data.yt_playlist_data, playlist_length=get_yt__playlist_data.amount_of_playlists)


"""
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}! </h1>'.format(name)
"""


if __name__ == '__main__':
    app.run()
