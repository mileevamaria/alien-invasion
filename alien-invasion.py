import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    # Initialize Pygame, settings, and screen objects.
    pygame.init()  # Initialize Pygame's background settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Screen's width and height
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:

        # Watch for events
        gf.check_events(ship)

        # Redraw the screen during each pass through the loop and make in visible
        gf.update_screen(ai_settings, screen, ship)


run_game()
