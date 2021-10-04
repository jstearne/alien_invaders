import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): # Sprite import allows Group()
    """Manage the player weapon."""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__() # it's 'inheriting' AlienInvasion's current state and from Sprite!
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then correct it's position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


