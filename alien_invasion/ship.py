import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set a starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags for continuous motion
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship position based on movement flag"""
        # Update ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
