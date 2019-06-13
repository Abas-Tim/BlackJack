'''
Class for players hand
'''

class Hand:
    """Class for players hand"""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """Method for adding a card to player's hand"""
        self.cards.append((card))
        self.value += card.value
        if card.rank == "ace":
            self.aces += 1
        if self.value > 21:
            self.adjust_for_ace()
        return self.value


    def adjust_for_ace(self):
        """Function that adjusts player's score for aces"""
        if self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        cards_in_hand =[]
        for card in self.cards:
            cards_in_hand.append((card.rank,card.suit))
        return f"Cards in hand are {cards_in_hand}"
