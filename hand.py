'''
Class for players hand
'''

class Hand(object):

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.value += card.value
		if card.rank == "ace":
			self.aces += 1
		self.cards.append((card))
		#rank = card.rank
		#suit = card.suit
		#self.cards.append((rank,suit))

	def evaluate(self):
		pass

	def __str__(self):
		cards_in_hand =[]
		for card in self.cards:
			cards_in_hand.append((card.rank,card.suit))
		return (f"Cards in hand are {cards_in_hand}")