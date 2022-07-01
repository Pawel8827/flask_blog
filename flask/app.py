from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_cors import CORS



app = Flask(__name__)
app.config['SECRET_KEY']= 'AAA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  nullable=False)
    tresc = db.Column(db.String(400), nullable=False)
    name = db.Column(db.String(300))
    photo = db.Column(db.LargeBinary)
    data_created = db.Column(db.DateTime, default=datetime.now) 

    def __init__(self, title, name, tresc):
        self.title = title
        self.tresc = tresc
        self.name = name
       

class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'tresc', 'name', 'photo', 'data_created' )

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)



@app.route("/blog", methods=['GET'])
def blog():
    blogs = Blog.query.all()
    results = blogs_schema.dump(blogs)
    return jsonify(results)

@app.route("/blog/<id>/", methods=['GET'])
def blog_details(id):
    blog = Blog.query.get(id)
    return blog_schema.jsonify(blog)

@app.route('/add', methods = ['POST'])
def add_blog():
    name = request.json['name']
    title = request.json['title']
    tresc = request.json['tresc']

    blogi = Blog(name, title, tresc)
    db.session.add(blogi)
    db.session.commit()
    return blog_schema.jsonify(blogi)

@app.route('/update/<id>/', methods = ['PUT'])
def update_blog(id):
    blog = Blog.query.get(id)
    name = request.json['name']
    title = request.json['title']
    tresc = request.json['tresc']
    blog.name = name
    blog.title = title
    blog.tresc = tresc

    db.session.commit()
    return blog_schema.jsonify(blog)

@app.route("/delete/<id>/", methods=['DELETE'])
def blog_delete(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return blog_schema.jsonify(blog)


if __name__ == "__main__":
    app.run(debug=True)

