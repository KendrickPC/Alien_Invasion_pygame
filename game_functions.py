# This file is created to prevent alien_invasions.py from
# being too lengthy. 
# Also, it will make the logic from alien_invasions.py easier to follow.

import sys

import pygame

def check_events():
    
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """ Update images on the screen and flip to a new screen. """
    # Redraw screen during each pass through the loop.
    # Connected to bg_color RGB values
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
