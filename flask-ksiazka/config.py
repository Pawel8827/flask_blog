import os 
basedir =os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'GDtfDCFYjD'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ABS_PATH_STATIC_FOLDER = "ksiazka/static/"


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    DB_NAME = "developer-db"
    DB_USERNAME = "root"
    DB_PASSWORLD = "example"
    UPLOADS = ""