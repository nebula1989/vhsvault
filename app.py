from flask import Flask, render_template
import get_embed_youtube


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/videos')
def video():
    return render_template('videos.html', video_ids=get_embed_youtube.video_ids)


"""
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}! </h1>'.format(name)
"""


if __name__ == '__main__':
    app.run()
