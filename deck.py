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
                self.deck.append((rank,suit))
        
        shuffle(self.deck)

    def __str__(self):
        cards_in_deck = ""
        for card in self.deck:
            cards_in_deck += str(card) + '\n'
        return cards_in_deck

    def mix(self):
        shuffle(self.deck)