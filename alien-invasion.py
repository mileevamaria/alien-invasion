import sys
import pygame

from settings import Settings
from ship import Ship


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

        # Watch for keyboard and mouse events

        for event in pygame.event.get():  # Access to the events (player's actions)
            if event.type == pygame.QUIT:  # When player clicks window's close button
                sys.exit()  # Exit the game

        # Redraw the screen during each pass through the loop

        screen.fill(ai_settings.bg_color)  # Screen's background color
        ship.blitme()  # Draw the player's ship image

        # Make the most recently drawn screen visible.

        pygame.display.flip()


run_game()
