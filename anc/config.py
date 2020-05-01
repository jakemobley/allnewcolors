import os

#set these values as environment variables prior to deployment.

class Config:
    SECRET_KEY = os.environ.get('ANC_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('ANC_SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('ANC_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('ANC_EMAIL_PASSWORD')