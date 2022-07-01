from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = Flask(__name__)


if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestConfig")
else:
        app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)


from ksiazka import routes, model