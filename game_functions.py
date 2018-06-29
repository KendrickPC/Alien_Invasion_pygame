# This file is created to prevent alien_invasions.py from
# being too lengthy. 
# Also, it will make the logic from alien_invasions.py easier to follow.

import sys

import pygame

def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                # Moves ship to the right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    """ Update images on the screen and flip to a new screen. """
    # Redraw screen during each pass through the loop.
    # Connected to bg_color RGB values
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
