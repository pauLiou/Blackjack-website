#storing the standard routes for the website for navigation
from flask import Blueprint, render_template, request, flash, Response, jsonify, url_for,send_from_directory,redirect
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from .models import User,Blackjack,Cards
from engine import deck_and_players,deposits,game_logic
from . import db
import json
import os

#define that this script is a blueprint - separate the app out so we don't have to have views all defined in one file
views = Blueprint('views', __name__)

#defining our views
@views.route('/', methods=['GET','POST']) # decorator - the url endpoint route for this page
@login_required
def home():
    if request.method == "POST":
        if request.form.get('action_play') == 'PLAY':
          
            return redirect(url_for('views.game'))

            

            # deal_card = deck_and_players.Deck_of_cards()
            # card = deal_card.deal_card()
            # card = Blackjack(card=card[1],suit=card[0],user_id=current_user.id)
            # url_prefix = card.suit.lower()[:-1]
            # card = Cards(card_url = './static/' + url_prefix + '/card' + card.suit + '_' + card.card + '.png',user_id=current_user.id)

            # db.session.add(card)
            # db.session.commit()
        # else:
        #     pass

    return render_template('home.html', user=current_user)

@views.route('/game', methods=['GET','POST']) # decorator - the url endpoint route for this page
@login_required
def game():
    deal = deck_and_players.Deck_of_cards()
    player = deck_and_players.Player()
    house = deck_and_players.Dealer()
    if request.method == "POST":
        if request.form.get('action_hit') == 'HIT':
            player,house = game_logic.play_blackjack(deal,player,house)
            cards=[]
            for card in player.cards:
                cards.append(Cards(card_url = './static/' + card[0].lower()[:-1] + '/card' + card[0] + '_' + card[1] + '.png',user_id=current_user.id))
            print(cards)

            db.session.add(cards)
            db.session.commit()

        elif request.form.get('action_stick') == 'STICK':
            pass
        elif request.form.get('action_double') == 'DOUBLE':
            pass
    return render_template('game.html',user=current_user)

@views.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    return render_template('profile.html',user=current_user)

@views.route('/delete-card', methods=['POST'])
def delete_card():
    card_id = json.loads(request.data)['card']
    card = Cards.query.get(card_id)
    if card and card.user_id == current_user.id:
        db.session.delete(card)
        db.session.commit()
        return jsonify({})
    return Response("Couldn't find image",status=400)

