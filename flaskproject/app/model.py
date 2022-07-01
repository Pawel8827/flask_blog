from app import db
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  nullable=False)
    tresc = db.Column(db.String(400), nullable=False)
    name = db.Column(db.String(300))
    photo = db.Column(db.LargeBinary)
    data_created = db.Column(db.DateTime, default=datetime.utcnow) 

    def __repr__(self):
        return '<Blog %r>' % self.id
