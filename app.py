from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}! </h1>'.format(name)


if __name__ == '__main__':
    app.run()
