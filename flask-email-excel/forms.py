from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,PasswordField,  SubmitField, validators, FileField, EmailField
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):

    tytul = StringField('Tytuł', [
        DataRequired()
    ])
    email = EmailField('Email', [
        DataRequired()
    ])
    message = TextAreaField('Wiadomość',[
         validators.Length(min=4, message=('Napisz więcej')), DataRequired()
    ])
        
    submit =SubmitField('Wyślij')


class ExcelForm(FlaskForm):
    file_upload = FileField('file', [
        DataRequired()
    ])
    Login = StringField('Login', [DataRequired()],render_kw={"placeholder": "pgrabowski@wp.pl"})
    Haslo = PasswordField('Hasło', [DataRequired()])
    submit =SubmitField('submit')