import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien



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
        # create instance to store game stats
        self.stats = GameStats(self)
        self.bg_color = (230, 230, 230) # set default bg color
        # Player details in game
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # Group() manages all bullets onscreen so we don't have to call update on each one
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True: 
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update() # continuously updates ship's position while game is running
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event): # handles button releases
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = False # stop movement
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self): # preceding underscore indicates HELPER FUNCTION
        """Create new bullet and add it to the bullets group.""" # can we use this for enemies?
        if len(self.bullets) < self.settings.bullets_allowed: # MAX BULLETS
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Responds to bullet-alien collisions."""
        # Removes aliens (and bullets) that collide.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) # False, True for a railgun!
        if not self.aliens:
            # destroy existing bullets and create a new fleet of aliens!
            self.bullets.empty()
            self._create_fleet()


    def _create_fleet(self):
        """Creates a fleet of enemy aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Number of alien rows that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create full fleet of aliens!
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create an alien and put it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond if aliens have reached a screen edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
        
    
    def _change_fleet_direction(self):
        """Drop the fleet one row, and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        """Responds to the player ship being hit by an enemy."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Clear screen of any remaining aliens and bullets (reset)
            self.aliens.empty()
            self.bullets.empty()
            # Create a new enemy fleet and re-center the player ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause while resetships_lef
            sleep(2.5)
        else:
            self.stats.game_active = False
        

    def _update_aliens(self):
        """Check if fleet at the edge of screen, then change direction for fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Looks for alien-player collisions (game over)
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # KEY pygame FUNCTION!
            self._ship_hit()
        # if aliens reach the bottom of the screen
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """Check if aliens have reached the bottom of the screen (successfully invaded)."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom: # if an alien's rectangle is at the the bottom
                self._ship_hit() # call _ship_hit() when game over
                break


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color) # display default bg color
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # makes a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game() # run_game function