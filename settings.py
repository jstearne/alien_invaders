

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
        self.bullet_speed = 1.0 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7 # MAX BULLETS option (at standard settings, 6 is the ceiling)