import sys
import pygame


def check_events():
    """ Respond to keypress and mouse events """

    for event in pygame.event.get():  # Access to the events (player's actions)
        if event.type == pygame.QUIT:  # When player clicks window's close button
            sys.exit()  # Exit the game


def update_screen(ai_settings, screen, ship):
    """ Update images on the screen and flip to the new screen """

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)  # Screen's background color
    ship.blitme()  # Draw the player's ship image

    # Make the most recently drawn screen visible
    pygame.display.flip()
