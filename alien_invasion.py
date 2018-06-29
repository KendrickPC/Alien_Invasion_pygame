import pygame

from settings import Settings
from ship import Ship
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

    # Make a ship
    ship = Ship(screen)

    # Set background color RGB values.
    bg_color = (0, 191, 255)

    # Start main loop for game
    # Event loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

# Initializes game and starts main loop
run_game()
