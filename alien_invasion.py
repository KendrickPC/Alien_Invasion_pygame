import sys
import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # Tuple below
    screen = pygame.display.set_mode((1200, 800))
    # Surface
    pygame.display.set_caption("Alien Invasion")

    # Set background color RGB values.
    bg_color = (230, 230, 230)

    # Start main loop for game
    # Event loop
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen during each pass through the loop.
        # Connected to bg_color RGB values
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Initializes game and starts main loop
run_game()
