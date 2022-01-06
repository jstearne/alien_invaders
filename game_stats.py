

class GameStats:
    """Track statistics/scoring for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state
        self.game_active = False
        # High score should never reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that change throughout the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0


