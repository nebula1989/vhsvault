from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('under-construction.html')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}! </h1>'.format(name)


if __name__ == '__main__':
    app.run()
