"""Flask Configuration"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY') or '123'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir,"app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False