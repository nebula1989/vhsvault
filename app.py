from flask import Flask, render_template, request
from forms import ContactForm
import get_yt__playlist_data

import os
from flask_mail import Message, Mail


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/videos')
def video():
    return render_template(
        'videos.html',
        playlist_data=get_yt__playlist_data.yt_playlist_data,
        playlist_ids=get_yt__playlist_data.yt_playlist_ids,
        playlist_length=get_yt__playlist_data.amount_of_playlists
    )


@app.route('/contactus', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        send_email(name, email, subject, message)
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)


def send_email(name, email, subject, message):
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    mail = Mail(app)

    msg = Message(('You have a message from ' + name + " Subject: " + subject), sender='info@vhsvault.com',
                  recipients=['ben@vhsvault.com'])
    msg.body = ('Message From ' + email + '\n' + message)

    with app.app_context():
        mail.send(msg)


if __name__ == '__main__':
    app.run()
