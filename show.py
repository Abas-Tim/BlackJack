'''
Methods of displaying a cards
'''
'''
This module is a terrible mess, I know. 
Just didn't wanted to care more for an interface of console card game.
'''

import hand
import os

suits = {'hearts':'♥', 'diamonds':'♦', 'clubs':'♣', 'spades':'♠'}

def show_some(player,dealer):
	image = ''
	image += "Dealer".center(50,'-') + '\n'
	image += ("---------" +" ") *len(dealer.cards) + '\n'

	i = 0
	for card in dealer.cards:

		if i == 0:
			if card.rank == 'ten':
				vis_value = '  '
			else:
				vis_value = ' '
		elif not card.rank in ['jack','queen','king','ace']:
			vis_value = str(card.value)
		else:
			vis_value = card.rank[0].upper()

		#image += '|' + str(vis_value) + '|'.rjust(7)

		if not card.rank in ['jack','queen','king','ace']:
			if card.rank == 'ten':
				image += '|' + str(vis_value) + '|'.rjust(6)
			else:
				image += '|' + str(vis_value) + '|'.rjust(7)
		else:
			image += '|' + vis_value + '|'.rjust(7)
		image += ' '
		i += 1

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(dealer.cards)+ '\n'

	i = 0
	for card in dealer.cards:
		if i == 0:
			image += '|' + ' '.center(7) + '|'.rjust(0) + ' '
		else:
			image += '|' + suits[card.suit].center(7) + '|'.rjust(0) + ' '
		i += 1

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(dealer.cards)+ '\n'

	i = 0 
	for card in dealer.cards:

		if i == 0:
			if card.rank == 'ten':
				vis_value = '  '
			else:
				vis_value = ' '
		elif not card.rank in ['jack','queen','king','ace']:
			vis_value = str(card.value)
		else:
			vis_value = card.rank[0].upper()

		if not card.rank in ['jack','queen','king','ace']:
			image += '|' + vis_value.rjust(7) + '|'
		else:
			image += '|' + vis_value.rjust(7) + '|'
		image += ' '
		i += 1
	image += '\n'
	image += ("---------" +" ") *len(dealer.cards)

	image += '\n' * 3
	#--------------------------------------------------------------------------------------
	#Player's cards
	#--------------------------------------------------------------------------------------

	image += "Player".center(50,'-') + '\n'
	image += ("---------" +" ") *len(player.cards) + '\n'

	for card in player.cards:
		if not card.rank in ['jack','queen','king','ace']:
			if card.rank == 'ten':
				image += '|' + str(card.value) + '|'.rjust(6)
			else:
				image += '|' + str(card.value) + '|'.rjust(7)
		else:
			image += '|' + card.rank[0].upper() + '|'.rjust(7)
		image += ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(player.cards)+ '\n'

	for card in player.cards:
		image += '|' + suits[card.suit].center(7) + '|'.rjust(0) + ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(player.cards)+ '\n'

	for card in player.cards:
		if not card.rank in ['jack','queen','king','ace']:
			image += '|' + str(card.value).rjust(7) + '|'
		else:
			image += '|' + card.rank[0].upper().rjust(7) + '|'
		image += ' '
	image += '\n'
	image += ("---------" +" ") *len(player.cards) 

	print(image)

def show_all(player,dealer):
	image = ''
	image += "Dealer".center(50,'-') + '\n'
	image += ("---------" +" ") *len(dealer.cards) + '\n'

	for card in dealer.cards:
		if not card.rank in ['jack','queen','king','ace']:
			if card.rank == 'ten':
				image += '|' + str(card.value) + '|'.rjust(6)
			else:
				image += '|' + str(card.value) + '|'.rjust(7)
		else:
			image += '|' + card.rank[0].upper() + '|'.rjust(7)
		image += ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(dealer.cards)+ '\n'

	for card in dealer.cards:
		image += '|' + suits[card.suit].center(7) + '|'.rjust(0) + ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(dealer.cards)+ '\n'

	for card in dealer.cards:
		if not card.rank in ['jack','queen','king','ace']:
			image += '|' + str(card.value).rjust(7) + '|'
		else:
			image += '|' + card.rank[0].upper().rjust(7) + '|'
		image += ' '
	image += '\n'
	image += ("---------" +" ") *len(dealer.cards)

	image += '\n' * 3
	#--------------------------------------------------------------------------------------
	#Player's cards
	#--------------------------------------------------------------------------------------

	image += "Player".center(50,'-') + '\n'
	image += ("---------" +" ") *len(player.cards) + '\n'

	for card in player.cards:
		if not card.rank in ['jack','queen','king','ace']:
			if card.rank == 'ten':
				image += '|' + str(card.value) + '|'.rjust(6)
			else:
				image += '|' + str(card.value) + '|'.rjust(7)
		else:
			image += '|' + card.rank[0].upper() + '|'.rjust(7)
		image += ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(player.cards)+ '\n'

	for card in player.cards:
		image += '|' + suits[card.suit].center(7) + '|'.rjust(0) + ' '

	image += '\n'
	image += ('|' + '|'.rjust(8) + ' ') * len(player.cards)+ '\n'

	for card in player.cards:
		if not card.rank in ['jack','queen','king','ace']:
			image += '|' + str(card.value).rjust(7) + '|'
		else:
			image += '|' + card.rank[0].upper().rjust(7) + '|'
		image += ' '
	image += '\n'
	image += ("---------" +" ") *len(player.cards) 

	print(image)


def clear_screen():
	clear = lambda: os.system('cls')
	clear()