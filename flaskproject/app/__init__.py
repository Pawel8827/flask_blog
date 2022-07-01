from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestConfig")
else:
        app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)


from app import views, model
