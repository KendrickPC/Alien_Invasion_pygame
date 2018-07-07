import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # Tuple below
    ai_settings = Settings()
    # Surface
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ken's First PyGame")

    # Set background color RGB values.
    bg_color = (0, 191, 255)
    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start main loop for game
    # Event loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Creating an instance of alien
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

# Initializes game and starts main loop
run_game()
