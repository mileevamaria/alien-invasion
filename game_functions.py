import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses (when player press on the keyboard) """

    if event.key == pygame.K_RIGHT:  # When player press "right" arrow key
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # When player press "left" arrow key
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # Create a new bullet and add to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # Exit the game when player press Q
        sys.exit()


def check_keyup_events(event, ship):
    """ Respond to key releases """

    if event.key == pygame.K_RIGHT:  # When player press "right" arrow key
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # When player press "left" arrow key
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Respond to keypress and mouse events """

    for event in pygame.event.get():  # Access to the events (player's actions)
        if event.type == pygame.QUIT:  # When player clicks window's close button
            sys.exit()  # Exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet """

    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """ Create a full fleet of aliens """

    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create te first row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + alien_width * 2 * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Update images on the screen and flip to the new screen """

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)  # Screen's background color

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # Draw the player's ship image
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """ Update the position of bullets and get rid of old bullets """

    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
