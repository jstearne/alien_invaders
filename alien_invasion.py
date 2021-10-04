import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """This class runs the game assets and behavior."""

    def __init__(self):
        """Initalize the game, create resources."""
        pygame.init()
        self.settings = Settings()

# fullscreen mode follows:
#        self.screen = pygame.display.set_mode((0, 0), pygame,FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230) # set default bg color
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True: 
            self._check_events()
            self._update_screen()
            self.ship.update() # continuously updates ship's position while game is running


    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exit (priority)
                sys.exit()
            elif event.type == pygame.KEYDOWN: # KEYDOWN is python for "button pressed"
                self._check_keydown_events(event)# run keydown function

            elif event.type == pygame.KEYUP: # if player releases a key
                self._check_keyup_events(event) # run keyup function


    def _check_keydown_events(self, event): # handles button presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event): # handles button releases
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = False # stop movement
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color) # display default bg color
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # makes a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game() # run_game function