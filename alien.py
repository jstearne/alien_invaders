import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A single enemy alien ship."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien ship at upper left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Alien's initial starting position
        self.x = float(self.rect.x)



