'''
BlackJack main logic file
'''
from deck import Deck
from card import Card
from hand import Hand
from chips import Chips
import actions
import show

show.clear_screen()
players_chips = Chips(200)
while True:
	playing_deck = Deck()
	dealer = Hand()
	player = Hand()
	print("Hello, player! This is Black Jack game! Let's start")
	actions.take_bet(players_chips)
	
	for i in range(0,4):
		if i in range(0,2):
			actions.hit(playing_deck, dealer)
		else:
			actions.hit(playing_deck, player)
	
	playing = True
	dealer_playing = True
	while playing:
		show.clear_screen()
		print(f"Your bet <<{players_chips.bet}>>")
		show.show_some(player, dealer)
		print(playing)
		playing = actions.hit_or_stand(playing_deck, player)
		if actions.player_busts(player.value):
			dealer_playing = False
			show.clear_screen()
			show.show_some(player, dealer)
			players_chips.lose_bet()
			print(f"You lost. You have {players_chips.total} left.")
			break

	if dealer_playing:
		while dealer.value <= 17:
			actions.hit(playing_deck, dealer)
	
	if input("Enter 'y' or 'yes' if you want to play one more time: ").lower() in ('y', 'yes'):
		break
	else:
		continue