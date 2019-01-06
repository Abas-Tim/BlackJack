'''
Class for card deck
'''
from random import shuffle

class Deck(object):

    """docstring for Deck."""

    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']


    def __init__(self):
        self.deck = []
        
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((suit,rank))
        
        shuffle(self.deck)

    def __str__(self):
       # return ("The deck is:" + format(self.deck))
        pass

    def mix(self):
        shuffle(self.deck)