import sys
import pygame
from settings import Settings

class AlienInvasion:
    """This class runs the game assets and behavior."""

    def __init__(self):
        """Initalize the game, create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230) # set default bg color

    def run_game(self):
        """Start the main loop for the game."""
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # exit
                    sys.exit()

            self.screen.fill(self.settings.bg_color) # display default bg color

            pygame.display.flip()

if __name__ == '__main__':
    # makes a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game() # run_game function