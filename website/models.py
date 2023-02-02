#database models, one for users and one for info
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    cash = db.Column(db.Integer,default=10000)
    stats = db.Column(db.Integer)
    blackjack = db.relationship('Blackjack')
    cards = db.relationship('Cards')
    gamestate = db.relationship('GameState')

class Blackjack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.String(150))
    card = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Cards(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_url = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class GameState(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    current_value = db.Column(db.Integer)
    current_house_value = db.Column(db.Integer)
    current_stage = db.Column(db.Integer)
    current_bet = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))







