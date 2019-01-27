#Class for player's chips

class Chips(object):

	def __init__(self, amount = 100):
		self.total = amount
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet