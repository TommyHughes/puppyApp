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

    # Register Blueprints
    from puppyApp.owners import bp as owners_bp
    app.register_blueprint(owners_bp, url_prefix='/owners')

    from puppyApp.puppies import bp as puppies_bp
    app.register_blueprint(puppies_bp, url_prefix='/puppies')

    from puppyApp.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from puppyApp import models
