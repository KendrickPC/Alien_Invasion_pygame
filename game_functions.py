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
