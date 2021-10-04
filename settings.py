

class Settings:
    """Stores all settings for the game. Clever!"""

    def __init__(self):
        # Screen Size
        self.screen_width = 1200
        self.screen_height = 800

        # background color
        self.bg_color = (230, 230, 230)

        # ship speed
        self.ship_speed = 1.5 # 1.5 pixels per game loop (higher is faster)