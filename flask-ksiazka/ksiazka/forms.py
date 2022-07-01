from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, validators, ValidationError, SelectField
from wtforms.validators import   DataRequired, Length


class Length(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Pole musi mieć pomiedzy %i a %i znaków.' % (min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)
        

class KordynatorForm(FlaskForm):
    opis = StringField('Opis', validators=[DataRequired(),Length(min=3, max=150, message="Opis powinien zawierać od 3 do 150 znaków")])
    imie = StringField('Imię', validators=[DataRequired(),Length(min=1, max=50, message="Imię powinien zawierać od 1 do 50 znaków")])
    nazwisko = StringField('Nazwisko', validators=[DataRequired(),Length(min=1, max=50, message="Nazwisko powinien zawierać od 1 do 50 znaków")])
    tel = StringField('Nr telefonu', validators=[Length( max=10, message="Nr telefonu powinien zawierać maxymalnie 10 znaków")])
    adres_email = StringField('Adres emil', validators=[Length(min=5, max=10, message="wpisz adres emil")])
    submit = SubmitField("Dodaj")


class WydzialForm(FlaskForm):
    wydzial_krotko = StringField('Wydział skrót nazwa', validators=[DataRequired()])
    wydzial_pelny  = StringField('Wydział pełna nazwa', validators=[DataRequired()])
    wydzial_kolej = StringField('Wydział kolejność', validators=[DataRequired()])
    submit = SubmitField("Dodaj")
    
class ReferatForm(FlaskForm):
    wydzial_id = SelectField( 'Wydzial', coerce=int)
    referat_krotko = StringField('Referat skrót nazwa', [DataRequired(), Length(min=1,max=10)])
    referat_pelny = StringField('Referat pełna nazwa', [DataRequired(), Length(min=3,max=100)])
    referat_kolej = StringField('Referat kolejność', [DataRequired(), Length(min=1,max=4)])
    submit = SubmitField("Dodaj")

class UrzednikForm(FlaskForm):
    imie = StringField('Imię', [Length(min=1,max=10)])
    nazwisko = StringField('Nazwisko', [Length(min=1,max=40)])
    user_kolej = StringField('Kolejność', [Length(min=1,max=4)])
    pokoj = StringField('Pokój',[Length(min=1,max=5)])
    tel_wew = StringField('Telefon wewnętrzny')
    telefon = StringField('Telefon', [Length(min=1,max=10)])
    fax = StringField('Fax')
    stanowisko = StringField('Stanowisko', [Length(min=1,max=30)])
    opis = StringField('Opis', [Length(min=1,max=50)])
    referat_id = SelectField( 'Referat', coerce=int)
    wydzial_id = SelectField( 'Wydzial', coerce=int)
    submit = SubmitField("Dodaj")
