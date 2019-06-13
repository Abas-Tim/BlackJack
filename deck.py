'''
Class for cards deck
'''
from random import shuffle


class Card:
    """Class for card objects"""


    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):

        return (f"The card is {self.rank} "
                + f"of {self.suit} and it's value is {self.value}")



class Deck:
    """Class for deck of cards"""

    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    ranks_values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
                    'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10,
                    'queen':10, 'king':10, 'ace':11}


    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank, value in self.ranks_values.items():
                new_card = Card(rank, suit, value)
                self.deck.append(new_card)
        shuffle(self.deck)

    def __str__(self):
        deck_cards_str = ""
        for card in self.deck:
            deck_cards_str += f'{card.rank}' + ' ' + f'{card.suit}' + ',' + f'{card.value}'+ '\n'
        return deck_cards_str

    def mix(self):
        """Function of shuffling the deck"""
        shuffle(self.deck)

    def get_card(self):
        """Function of taking a card from a deck """
        card = self.deck.pop()
        return card
