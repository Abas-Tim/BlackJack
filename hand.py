'''
Class for players hand
'''

class Hand(object):

	def __init__(self):
		#Creating an empty hand

		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append((card))
		self.value += card.value
		if card.rank == "ace":
			self.aces += 1
		if self.value > 21:
			self.adjust_for_ace()
		return self.value
		#rank = card.rank
		#suit = card.suit
		#self.cards.append((rank,suit))

	def adjust_for_ace(self):
		if self.aces > 0:
			self.value -= 10
			self.aces -= 1

	def __str__(self):
		cards_in_hand =[]
		for card in self.cards:
			cards_in_hand.append((card.rank,card.suit))
		return (f"Cards in hand are {cards_in_hand}")