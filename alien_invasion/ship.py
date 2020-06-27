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

        # Movement flags for continuous motion
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
