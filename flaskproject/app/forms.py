from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import Form, StringField, TextField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):

    name = StringField('name', [
        DataRequired()
    ])
    email = StringField('email', [
        DataRequired()
    ])
    message = TextAreaField('message',[
         validators.Length(min=4, message=('Napisz więcej'))
    ])
        
    submit =SubmitField('submit')

class Blogform(FlaskForm):

    title = StringField('tytul', [validators.Length(min=4, max=30),validators.DataRequired()])
    name = StringField('name',[validators.Length(min=4),validators.DataRequired()])
    tresc = TextAreaField('tresc',[validators.Length(min=4),validators.DataRequired()])
    submita = SubmitField('Zamieść')


    



