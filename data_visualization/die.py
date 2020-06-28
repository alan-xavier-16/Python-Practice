from random import randint


class Die:
    """Class representing a die"""

    def __init__(self, num_sides=6):
        """Assume 6-sided die as default"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random integer between 1 and num_sides"""
        return randint(1, self.num_sides)
