# This file is created to prevent alien_invasions.py from
# being too lengthy.
# Also, it will make the logic from alien_invasions.py easier to follow.

import sys
import pygame
from bullet import Bullet
from alien import Alien


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine the # of rows of alien ships fitting on screen. """
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    """ Determine the number of alien ships that fit in a row """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Create an alien ship and place it in its row """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# Creating a fleet of alien ships
def create_fleet(ai_settings, screen, aliens, ship):
    """ Create a full fleet of alien ships """
    # Create an alien ship and find the number of alien ships in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)

    # Creating first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien ship and place it in its row
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 12-4 Keys test: 274 is down, 275, 273, and 276
    # print(event.key)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # Exit the game with "q" key
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """ Respond to key releases """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet if 3 bullet limit is not reached """
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Update images on the screen and flip to a new screen. """
    # Redraw screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Connected to bg_color RGB values
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets """
    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
