"""This is the library for most of the game actions"""

import hand
import chips
import deck
from show import clear_screen

def take_bet(players_chips):
	while True:
		print(f"You have {players_chips.total} chips")
		
		try:
			bet = int(input("How much do you want to bet? >> "))
		except ValueError:
			clear_screen()
			print("Please use only integer number")
			continue

		if bet < players_chips.total:
			players_chips.bet = bet
			break
		else:
			clear_screen()
			print("You can't bet more chips then you have")
			continue


def hit(deck, hand):
	return hand.add_card(deck.get_card())
	
def hit_or_stand(deck, hand):
	if not input("Enter 'y' or 'yes' if you want to hit: ").lower() in ('y', 'yes'):
		return False
	else:
		hit(deck,hand)
		return True
	#return playing

def player_busts(value):
	return value > 21

def player_wins(player_value, dealer_value):
	return player_value > dealer_value

def dealer_busts(value):
	return value > 21

def dealer_wins(player_value, dealer_value):
	return dealer_value > player_value
	
def push(player_value, dealer_value):
	return dealer_value == player_value