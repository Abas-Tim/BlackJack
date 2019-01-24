'''
Class for a card
'''
import deck

class Card(object):

	def __init__(self, rank, suit, value):
		self.rank = rank
		self.suit = suit
		self.value = value

	def __str__(self):
		return (f"The card is {self.rank} of {self.suit} and it's value is {self.value}")