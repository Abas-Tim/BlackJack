"""This is the library for most of the game actions"""

import hand
import chips
import deck

def take_bet(players_chips):
	while True:
		try:
			bet = int(input("Please enter your bet: "))
			players_chips.bet = bet
			break
		except TypeError:
			print("Please use only integer number")
			continue

def hit(deck, hand):
	hand.add_card(deck.get_card())
	return hand.value

def hit_or_stand(deck, hand):
	if input("Do you want to hit?: ").lower() in ['y', 'yes']:
		hit(deck,hand)
		return True
	else:
		return False