import deck_and_players
import time

def hand_value(player):
    #get the value of the cards in the players hand
    player.value = 0
    _,hand = zip(*player.cards)
    for card in hand:
        if card.isnumeric():
            player.value += (int(card))
        if card in ['J','Q','K']:
            player.value += 10
            
        elif card is ['A']:
            if sum(player.value) + 11 > 21:
                player.value += 1
            else:
                player.value += 11
    return (player)

def house_logic(deal,house):
    if house.value <= 16:
        house.cards.append(deal.deal_card())
        print('Dealer new card is: ', house.cards[-1])
        house = hand_value(house)
        time.sleep(0.5)
        return house_logic(deal,house) # recursive loop
    else:
        print('The dealer sticks on', house.value)
        return house

def win_lose(player,house):
    if player.value > house.value:
        print('You win!')
        return 'Win'
    elif player.value < house.value:
        print('The house wins!')
        return 'Lose'
    else:
        print('Push! No winner!')
        return 'Push'



def play_blackjack(deal,player,house):
    # deal the cards and find out the value of each players cards
    player.cards = [deal.deal_card() for _ in range(0,2)]
    house.cards = [deal.deal_card() for _ in range(0,2)]
    player = hand_value(player)
    house = hand_value(house)

    print('You were dealt:', player.cards)
    print('You have', player.value)
    print('The dealer is showing', house.cards)
    print('The dealer has', house.value)

    action(deal,player,house)

    return player

def check_conditions(score):
    # see if the player has a blackjack (1.5 payout)
    if score == 21:
        return 'Blackjack'
    
    # see if the player has busted (0 payout)
    elif score > 21:
        return 'Bust'
    else:
        return 'Value'

def action(deal,player,house):

    player = hand_value(player)
    outcome = check_conditions(player.value)

    if outcome == 'Bust':
        print(player.value)
        print('Busted! You have lost!')
    
    elif outcome == 'Blackjack':
        print('21! Blackjack! You win!')
        exit()
    else:
 
        decision = input('Would you like a card? (Y/N)')

        if decision == 'Y':

            player.cards.append(deal.deal_card())
            print('New card is: ', player.cards[-1])

            # new card value
            player.value = hand_value(player)
            action(deal,player,house)
        
        elif decision == 'N':
            house_logic(deal,house)
            outcome = win_lose(player,house)

            play_again = input('Would you like to play again?')

            if play_again == 'Y':
                play_blackjack(deal,player,house)
            else:
                exit()

        
        else:
            print('Please enter a valid answer')
            action(deal,player,house)
    
# initialise the classes 

deal = deck_and_players.Deck_of_cards()
player = deck_and_players.Player()
house = deck_and_players.Dealer()

play_blackjack(deal,player,house)

















            