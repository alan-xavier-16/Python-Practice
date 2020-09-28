class Player:
    """A class for a player"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num):
        """Draw random card cards from Deck"""
        self.hand = [deck.drawCard() for card in range(num)]

    def showHand(self):
        """Show player's hand"""
        for card in self.hand:
            card.show()
