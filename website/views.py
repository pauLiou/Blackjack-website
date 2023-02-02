#storing the standard routes for the website for navigation
from flask import Blueprint, render_template, request, Response, jsonify, url_for,redirect
from flask_login import login_required, current_user
from .models import *
from engine import deck_and_players,deposits,game_logic
from . import db
import json
import os
from sqlalchemy import update

#define that this script is a blueprint - separate the app out so we don't have to have views all defined in one file
views = Blueprint('views', __name__)

#defining our views
@views.route('/', methods=['GET','POST']) # decorator - the url endpoint route for this page
@login_required
def home():
    if request.method == "POST":
        
        

        if request.form.get('action_play') == 'BET':

            db.session.add(GameState(current_bet = request.form.get('bet'),user_id = current_user.id))
            db.session.commit()
          
            return redirect(url_for('views.game'))

    return render_template('/html/home.html', user=current_user)

@views.route('/game', methods=['GET','POST']) # decorator - the url endpoint route for this page
@login_required
def game():
    player_value = None
    house_value = None
    deal = deck_and_players.Deck_of_cards()
    player = deck_and_players.Player()
    house = deck_and_players.Dealer()
    if request.method == "POST":
        if request.form.get('action_hit') == 'HIT':

            player,house = game_logic.play_blackjack(deal,player,house)
            player_cards = mutate_url(player.cards)
            house_cards = mutate_url(house.cards)

            db.session.add(GameState(current_value = player.value,
                                    current_house_value = house.value,
                                    current_stage = 1,
                                    user_id = current_user.id))
            for card in player_cards: 
                db.session.add(card)


            for house_card in house_cards:
                db.session.add(house_card)

            db.session.commit()

        elif request.form.get('action_stick') == 'STICK':
            pass
        elif request.form.get('action_double') == 'DOUBLE':
            pass
    return render_template('/html/game.html',user=current_user)

@views.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    return render_template('/html/profile.html',user=current_user)

@views.route('/delete-card', methods=['POST'])
def delete_card():
    card_id = json.loads(request.data)['card']
    card = Cards.query.get(card_id)
    if card and card.user_id == current_user.id:
        db.session.delete(card)
        db.session.commit()
        return jsonify({})
    return Response("Couldn't find image",status=400)

def mutate_url(hand):
    cards = []
    for card in hand:
        cards.append(Cards(card_url = './static/' + card[0].lower()[:-1] + 
        '/card' + card[0] + '_' + card[1] + '.png',user_id=current_user.id))
    return cards


