from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, pre_load

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False, unique=True)
    country = db.Column(db.String(100), nullable=False)

    def __init__(self, first_name, last_name, email_address,phone_number,country):
        self.last_name = last_name
        self.first_name = first_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.country = country


class UserSchema(ma.Schema):

    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email_address = fields.String(required=True)
    phone_number = fields.String(required=True)
    country = fields.String(required=True)
