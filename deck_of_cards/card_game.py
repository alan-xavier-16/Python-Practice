"""
- Build a Deck of Cards
- Draw 'n' number of Cards from Deck at random
"""

from deck import Deck
from player import Player


def main():
    """Run game"""
    deck = Deck()

    player1 = Player("Alan")
    player1.draw(deck, 3)

    player1.showHand()


if __name__ == "__main__":
    """Make a Card Game Instance"""
    main()
