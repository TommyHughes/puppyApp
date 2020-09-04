import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='DevConfig'):
    """Initialize the core application"""
    configuration = 'config.'+str(config_class)
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object(configuration)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    return app

from puppyApp import models
