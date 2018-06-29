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
    bg_color = (255, 255, 255)

    # Start main loop for game
    # Event loop
    while True:
        gf.check_events()

        # Redraw screen during each pass through the loop.
        # Connected to bg_color RGB values
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Initializes game and starts main loop
run_game()
