'''
BlackJack main logic file
'''
from hand import Hand
from chips import Chips
from deck import Deck
import actions
import show


players_chips = Chips(200)
while True:
    show.clear_screen()
    playing_deck = Deck()
    dealer = Hand()
    player = Hand()
    print("Hello, player! This is Black Jack game! Let's start")
    actions.take_bet(players_chips)

    for i in range(0, 4):
        if i in range(0, 2):
            actions.hit(playing_deck, dealer)
        else:
            actions.hit(playing_deck, player)

    playing = True
    dealer_playing = True
    while playing:
        show.clear_screen()
        #print(f"Your chips <<{players_chips.total}>>")
        print(f"Your bet <<{players_chips.bet}>>")
        show.show_some(player, dealer)
        playing = actions.hit_or_stand(playing_deck, player)

        if actions.player_busts(player.value):
            dealer_playing = False
            show.clear_screen()
            show.show_some(player, dealer)
            players_chips.lose_bet()
            print(f"You lost. You have {players_chips.total} left.")
            break

    if dealer_playing:
        show.clear_screen()
        #print(f"Your chips <<{players_chips.total}>>")
        print(f"Your bet <<{players_chips.bet}>>")
        show.show_all(player, dealer)
        while dealer.value <= 17:
            actions.hit(playing_deck, dealer)
            show.clear_screen()
            #print(f"Your chips <<{players_chips.total}>>")
            print(f"Your bet <<{players_chips.bet}>>")
            show.show_all(player, dealer)


    if actions.dealer_busts(dealer.value):
        print(f"Congratulations! You won {players_chips.bet}!")
        players_chips.win_bet()
    elif actions.player_wins(player.value, dealer.value):
        print(f"Congratulations! You won {players_chips.bet}!")
        players_chips.win_bet()
        players_chips.lose_bet()
        print(f"You lost. You have {players_chips.total} left.")
    elif actions.push(player.value, dealer.value):
        print("Looks like it is a draw!")



    if input("Enter 'y' or 'yes' if you"
             + " want to play one more time: ").lower() in ('y', 'yes'):
        continue
    else:
        break
