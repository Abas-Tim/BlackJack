'''
Class for a card
'''
import deck

class Card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return (f"The card is {self.rank} of {self.suit}")

	def value_of_card(self):
		return  deck.Deck.ranks_values[self.rank]