from website import views
from engine import deck_and_players,deposits
from flask import Blueprint
import time

game = Blueprint('game', __name__)

def hand_value(current):
    #get the value of the cards in the players hand and update the player class
    current.value = 0
    _,hand = zip(*current.cards)# splits up the tuples so we just get the values of each hand
    
    if 'A' in hand:
        hand = list(hand)
        [x for x in hand if hand.append(hand.pop(hand.index('A')))] # push all the aces to the end

    for card in hand:
        if card.isnumeric():
            current.value += (int(card))
        elif card in ['J','Q','K']:
            current.value += 10
            
        elif card == 'A':
            if current.value + 11 > 21:
                current.value += 1
            else:
                current.value += 11
    return current

def house_logic(deal,house):
    # runs to determine if the house busts or not
    # in blackjack the dealer MUST hit on 16 or below

    if house.value <= 16:
        house.cards.append(deal.deal_card())
        print(f'Dealer new card is: {house.cards[-1]}')
        house = hand_value(house)
        print(house.value)
        time.sleep(0.5)
        return house_logic(deal,house) # recursive loop
    if house.value > 21:
        print(f'House busts! with {house.value}, You win')
        return house
    else:
        print(f'The dealer has {house.value}')
        return house

@game.route('/', methods=["GET","POST"])
def play_blackjack(deal,player,house):
    # deal the cards and find out the value of each players cards
    player.cards = [deal.deal_card() for _ in range(0,2)]
    house.cards = [deal.deal_card() for _ in range(0,2)]
    player = hand_value(player)
    house = hand_value(house)

    player,bet = deposits.make_bet(player)

    print('You were dealt:', player.cards)

    print('The dealer is showing', house.cards[0])

    action(deal,player,house,bet)

    
    return player

def double_bet(deal,player,bet):
    # if doubling bet we minus the bet again, then double the worth of the bet
    print('Double, 1 card only')
    player.bank -= int(bet)
    bet = bet*2
    player.cards.append(deal.deal_card())
    player = hand_value(player)

    print(player.value)
    
    return player,bet


def action(deal,player,house,bet,double=0):

    player = hand_value(player)
    print('You have', player.value)
    outcome = deposits.check_conditions(player.value)
    
    if outcome == 'Value':
        if double == 0:
            decision = input('Would you like to do? [Hit],[Stick],[Double]? ')
        else:
            decision = input('What would you like to do? [Hit],[Stick]')

        if decision == 'Hit':
            double = 1
            player.cards.append(deal.deal_card())
            print('New card is: ', player.cards[-1])
            # new card value
            action(deal,player,house,bet)
        
        elif decision == 'Stick':

            print(f'Dealer flips over {house.cards[1]}')
            print(house.value)
            house = house_logic(deal,house)
            deposits.winner_calculation(player,house,bet,outcome)
            play_again = input('Would you like to play again? (Y/N) ')

            if play_again == 'Y':
                play_blackjack(deal,player,house)
            else:
                exit()

        elif decision == 'Double':
            double = 1
            house = house_logic(deal,house)
            player,bet = double_bet(deal,player,bet)
            print(f'1 card only: {player.cards[-1]}')
            deposits.winner_calculation(player,house,bet,outcome)
            play_again = input('Would you like to play again? (Y/N) ')

            if play_again == 'Y':
                play_blackjack(deal,player,house)
            else:
                exit()
            
        else:
            print('Please enter a valid answer')
            action(deal,player,house,bet)
    else:
        play_again = input('Would you like to play again? (Y/N) ')

        if play_again == 'Y':
            play_blackjack(deal,player,house)
        else:
            exit()

# initialise the classes 


















            