from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from url_shortener import config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eec08f2e90a81fe6227f2921bd67865e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rash:<ronalto>;@localhost/url_shortener'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .routes import url_shortener

app.register_blueprint(url_shortener)

def create_app(config_file='config.py'):
    pass
#     app = Flask(__name__)
#     app.config.from_pyfile(config_file)
    
#     db.init_app(app)
    
#     from .routes import url_shortener
    
#     app.register_blueprint(url_shortener)
    
#     return app
