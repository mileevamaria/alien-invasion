import sys
import pygame


def check_events(ship):
    """ Respond to keypress and mouse events """

    for event in pygame.event.get():  # Access to the events (player's actions)
        if event.type == pygame.QUIT:  # When player clicks window's close button
            sys.exit()  # Exit the game

        elif event.type == pygame.KEYDOWN:  # When player press on the keyboard
            if event.key == pygame.K_RIGHT:  # When player press "right" arrow key
                ship.moving_right = True

        elif event.type == pygame.KEYUP:  # When player press on the keyboard
            if event.key == pygame.K_RIGHT:  # When player press "right" arrow key
                ship.moving_right = False


def update_screen(ai_settings, screen, ship):
    """ Update images on the screen and flip to the new screen """

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)  # Screen's background color
    ship.blitme()  # Draw the player's ship image

    # Make the most recently drawn screen visible
    pygame.display.flip()
