import numpy as np

'''
This class creates the deck with the number of decks we want and automatically shuffles it
'''
class Deck_of_cards:
    def __init__(self,total_decks = 4):
        self.suit = ['Clubs','Diamonds','Hearts','Spades']
        self.card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.total_decks = total_decks
        self.deck = list((x,y) for x in self.suit for y in self.card) * self.total_decks
        np.random.shuffle(self.deck)
    
    def deal_card(self,num=1):
        # here we pop off the top card
        if num == 1:
            return self.deck.pop()
        else:
            return list(self.deck.pop() for x in range(num))

    def __str__(self):
        return 'Deck of cards'

    def reset(self):
        # reset the deck back to it's original state
        self.deck = list((x,y) for x in self.suit for y in self.card) * self.total_decks
        np.random.shuffle(self.deck)


'''
This class is for the house. We are keeping track of the dealers cards and values
'''
class Dealer:
    def __init__(self,value=0,cards=[]):
        self.value = value
        self.cards = cards

'''
This class is for the user. We want to keep track of the cards, values, money, and a few other stats
'''
class Player:
    def __init__(self,value=0,cards=[],bank=10000):
        self.value = value
        self.cards = cards
        self.bank = bank


