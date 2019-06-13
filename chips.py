"""Class for player's chips"""


class Chips:
    """Class for chips of a player"""


    def __init__(self, amount=100):
        self.total = amount
        self.bet = 0

    def win_bet(self):
        """Method for adding chips in win scenario"""
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        """Method for deducting chips from player in losing scenario"""
        self.total -= self.bet
        self.bet = 0
