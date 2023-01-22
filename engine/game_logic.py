import deck_and_players

def hand_value(hand):
    #get the value of the cards in the players hand
    value = []

    for card in hand:
        if card not in ['J','Q','K','A']:
            value.append(int(card))
        else:
            value.append(10)
    
    return sum(value)

def deal_cards(players):
    # deal the first 2 cards to the number of players
    first_card = []
    second_card = []
    for _ in range(players):
        deal_card = deck_and_players.Deck_of_cards()
        first_card.append(deal_card.deal_card())
        second_card.append(deal_card.deal_card())
    return first_card,second_card


def dealt_score(players):
    # deal the cards and find out the value of each players cards
    first_card,second_card = deal_cards(players)
    hand = first_card + second_card
    score = []
    for i in range(players):
        score.append(hand_value(hand[i][1] + hand[i+players][1]))
    return score,hand

def dealer_cards():
    # deal the cards for the dealer
    first_card,second_card = deal_cards(1)
    hand = first_card + second_card
    score = hand_value(hand[0][1] + hand[1][1])

    print('The Dealer has:', score)
    return score



def check_conditions(score):
    # see if the player has a blackjack (1.5 payout)
    if score == 21:
        return 'Blackjack'
    
    # see if the player has busted (0 payout)
    elif score > 21:
        return 'Bust'

    else:
        print('You have', score)
        return 'Value'

def action(cards):

    score = 0

    for i in range(len(cards)):
        score += hand_value(cards[i][1])

    count = check_conditions(score)

    if count == 'Bust':
        print('Busted! You have lost!')
    
    elif count == 'Blackjack':
        print('21! Blackjack! You win!')
        exit()
    else:
 
        decision = input('Would you like a card? (Y/N)')

        if decision == 'Y':

            deal_card = deck_and_players.Deck_of_cards()
            cards.append(deal_card.deal_card())
            print('New Card is: ', cards[-1])

            # new card value
            for i in range(len(cards)):
                score += hand_value(cards[i][1])
                action(cards)
        
        elif decision == 'N':
            for i in range(len(cards)):
                score += hand_value(cards[i][1])
            return score
        
        else:
            print('Please enter a valid answer')
            action(cards)
    
        


players = 1
score,hand = dealt_score(players)
dealer_cards()
action(hand)
















            