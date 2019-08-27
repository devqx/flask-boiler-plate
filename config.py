import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO=True
SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI='postgres://postgres:postgres@localhost/cr8_users'