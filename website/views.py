#storing the standard routes for the website for navigation
from flask import Blueprint, render_template, request, flash, Response, jsonify
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from .models import User,Blackjack
from engine import deck_and_players
from . import db
import json

#define that this script is a blueprint - separate the app out so we don't have to have views all defined in one file
views = Blueprint('views', __name__)

#defining our views
@views.route('/', methods=['GET','POST']) # decorator - the url endpoint route for this page
@login_required
def home():
    if request.method == "POST":
        if request.form.get('action1') == 'HIT':
            deal_card = deck_and_players.Deck_of_cards()
            card = deal_card.deal_card()
            card = Blackjack(card=card[0],suit=card[1],user_id=current_user.id)
            db.session.add(card)
            db.session.commit()
        else:
            pass
    return render_template('home.html', user=current_user)


@views.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    return render_template('profile.html',user=current_user)

@views.route('/delete-card', methods=['POST'])
def delete_card():
    card_id = json.loads(request.data)['card']
    card = Blackjack.query.get(card_id)
    if card and card.user_id == current_user.id:
        db.session.delete(card)
        db.session.commit()
        return jsonify({})
    return Response("Couldn't find image",status=400)




