"""This is the library for most of the game actions"""
from show import clear_screen


def take_bet(players_chips):
    """
    Function that takes, check and
    passes entered by the player bet
    """

    while True:
        print (f"You have {players_chips.total} chips")

        try:
            bet = int(input("How much do you want to bet? >> "))
        except ValueError:
            clear_screen()
            print("Please use only integer number")
            continue

        if bet <= players_chips.total:
            players_chips.bet = bet
            break
        else:
            clear_screen()
            print("You can't bet more chips then you have")
            continue


def hit(deck, hand):
    """Get a card from deck to player's hand"""

    return hand.add_card(deck.get_card())

def hit_or_stand(deck, hand):
    """Function determines if player wants to hit or stand"""

    if (not input("Enter 'y' or 'yes' if you want to hit: ").lower()
            in ('y', 'yes')):
        return False
    else:
        hit(deck, hand)
        return True

def player_busts(value):
    """Function that determines if player busts"""

    return value > 21

def player_wins(player_value, dealer_value):
    """Funtion that determines who wins"""

    return player_value > dealer_value

def dealer_busts(value):
    """Function that determines if dealer busts"""
    return value > 21

def dealer_wins(player_value, dealer_value):
    """Function that determines if dealer wins"""

    return dealer_value > player_value

def push(player_value, dealer_value):
    """Function determines if there is a draw"""
    return dealer_value == player_value
