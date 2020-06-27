import sys
import pygame


class AlienInvasion:
    """Overall class for managing game assets"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start main game loop"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show new screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()