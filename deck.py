'''
Class for cards deck
'''
from random import shuffle

class Deck(object):

    """ """

    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks_values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}


    def __init__(self):
        self.deck = []
        
        for suit in self.suits:
            for rank in self.ranks_values.keys():
                self.deck.append((rank,suit))
        
        shuffle(self.deck)

    def __str__(self):
        cards_in_deck = ""
        for card in self.deck:
            cards_in_deck += str(card) + '\n'
        return cards_in_deck

    def mix(self):
        shuffle(self.deck)