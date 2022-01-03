

class Settings:
    """Stores all settings for the game. Clever!"""

    def __init__(self):
        # Screen Size
        self.screen_width = 1200
        self.screen_height = 800

        # background color
        self.bg_color = (230, 230, 230)

        # player ship movement speed
        self.ship_speed = 1.5 # 1.5 pixels per game loop (higher is faster)
        self.ship_limit = 3 # number of lives

        # weapons mechanics
        self.bullet_speed = 1.5
        self.bullet_width = 3 # for testing purposes
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7
        
        # alien settings
        self.alien_speed = 2.50
        self.fleet_drop_speed = 10
 

        # How quickly difficulty escalates
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change during the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 1 is right, -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale