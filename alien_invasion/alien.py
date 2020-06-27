import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to manage a single alien in a fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image & set rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horiz. position
        self.x = float(self.rect.x)
