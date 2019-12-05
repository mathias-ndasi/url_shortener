import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'config.ini'))


class Config:
    SECRET_KEY = config.get('universe', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('universe', 'SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = config.get(
        'universe', 'SQLALCHEMY_TRACK_MODIFICATIONS')
    MAIL_SERVER = config.get('universe', 'MAIL_SERVER')
    MAIL_PORT = config.get('universe', 'MAIL_PORT')
    MAIL_USE_TLS = config.get('universe', 'MAIL_USE_TLS')
    MAIL_USERNAME = config.get('universe', 'MAIL_USERNAME')
    MAIL_PASSWORD = config.get('universe', 'MAIL_PASSWORD')

