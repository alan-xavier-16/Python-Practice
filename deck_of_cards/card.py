class Card:
    """A class for a card"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        """Display card details"""
        print(f"{self.value} of {self.suit}")
