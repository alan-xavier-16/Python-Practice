from card import Card
from random import shuffle, randint


class Deck:
    """A class for a deck of cards"""

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Create deck of cards using the Card class"""
        self.cards = [Card(s, v) for s in ["Spades", "Diamonds",
                                           "Hearts", "Clubs"] for v in range(1, 14)]

    def show(self):
        """Show all cards"""
        for card in self.cards:
            card.show()

    def shuffle(self):
        """Shuffle deck"""
        shuffle(self.cards)

    def drawCard(self):
        """Draw random Card instance from deck"""
        randomCard = self.cards.pop(randint(1, len(self.cards)-1))
        return randomCard
