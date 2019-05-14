import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    # Initialize Pygame, settings, and screen objects.
    pygame.init()  # Initialize Pygame's background settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Screen's width and height
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)

    # Start the main loop for the game
    while True:

        # Watch for events
        gf.check_events(ai_settings, screen, ship, bullets)

        # Reacting on keypress' events
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)

        # Redraw the screen during each pass through the loop and make in visible
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
