'''
Class for cards deck
'''
from random import shuffle
#from card import Card
import card

class Deck(object):

    """ """

    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks_values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 
    'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}


    def __init__(self):
        self.deck = []
        
        for suit in self.suits:
            for rank in self.ranks_values.keys():
                new_card = card.Card(rank,suit)
                self.deck.append(new_card)
        shuffle(self.deck)

    def __str__(self):
        deck_cards_str = ""
        for card in self.deck:
            deck_cards_str += f'{card.rank}' + ' ' + f'{card.suit}' + '\n'
        return deck_cards_str

    def mix(self):
        shuffle(self.deck)

    def get_card(self):
        card =  self.deck.pop()
        return card