#database models, one for users and one for info
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    cash = db.Column(db.Integer,default=2000)
    stats = db.Column(db.Integer)
    blackjack = db.relationship('Blackjack')
    

class Blackjack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card = db.Column(db.String(150))
    suit = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))






