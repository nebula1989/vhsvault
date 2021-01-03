from flask_wtf import FlaskForm
import wtforms


class ContactForm(FlaskForm):
    name = wtforms.TextField("Name")
    email = wtforms.TextField("Email")
    subject = wtforms.TextField("Subject")
    message = wtforms.TextAreaField("Message")
    submit = wtforms.SubmitField("Send")
