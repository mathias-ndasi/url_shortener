from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from url_shortener.config import Config
from flask_cors import CORS


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    CORS(app)
    
    from .routes import url_shortener
    from .api import api
    
    app.register_blueprint(url_shortener)
    app.register_blueprint(api)
    
    return app
