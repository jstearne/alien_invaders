

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

        # weapons mechanics
        self.bullet_speed = 1.5
        self.bullet_width = 3 # for testing purposes
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7
        
        # alien settings
        self.alien_speed = .50
        self.fleet_drop_speed = 5
        # 1 is right, -1 is left
        self.fleet_direction = 1


