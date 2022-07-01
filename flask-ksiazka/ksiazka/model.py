from ksiazka import db


class Wydzial(db.Model):
    __tablename__= 'wydzial'
    id = db.Column(db.Integer, primary_key=True)
    wydzial_krotko = db.Column(db.String(5))
    wydzial_pelny = db.Column(db.String(50))
    wydzial_kolej = db.Column(db.Integer())
    users = db.relationship('Urzednik', backref='urzednik_wydz', lazy='dynamic')
    wydzia = db.relationship('Referat', backref='referat_wydz', lazy='dynamic')
    def __repr__(self):
        return '<Wydzial {}>'.format(self.wydzial_pelny)


class Referat(db.Model):
    __tablename__= 'referat'
    id = db.Column(db.Integer, primary_key=True)
    referat_krotko = db.Column(db.String(5))
    referat_pelny = db.Column(db.String(50))
    referat_kolej = db.Column(db.Integer())
    wydzial_id = db.Column(db.Integer, db.ForeignKey('wydzial.id'))
    usera = db.relationship('Urzednik',backref='urzednik_ref', lazy='dynamic')
    
    def __repr__(self):
        return '<Referat {}>'.format(self.referat_pelny)


class Urzednik(db.Model):
    __tablename__= 'urzednik'
    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(20))
    nazwisko = db.Column(db.String(60))
    user_kolej = db.Column(db.Integer())
    pokoj = db.Column(db.String(10))
    tel_wew = db.Column(db.Integer())
    telefon = db.Column(db.Integer())
    fax = db.Column(db.Integer())
    stanowisko = db.Column(db.String(25))
    opis = db.Column(db.String(200))
    referat_id = db.Column(db.Integer, db.ForeignKey('referat.id'))
    wydzial_id = db.Column(db.Integer, db.ForeignKey('wydzial.id'))

    def __repr__(self):
        return '<Imię {} Nazwisko {}'.format(self.imie, self.nazwisko)





