import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set a starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)