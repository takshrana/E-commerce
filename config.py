import os


class Config:
    SECRET_KEY = os.environ.get('FLASK_KEY', 'TakshRana')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
    SQL_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "/app/static/img/products"
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000
