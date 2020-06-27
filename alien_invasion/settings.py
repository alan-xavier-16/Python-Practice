class Settings:
    """A class to store game setting for Alien Invasion"""

    def __init__(self):
        """Initilaize game setting"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
