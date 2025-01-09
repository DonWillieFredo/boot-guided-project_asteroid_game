import pygame
from player import Player  # Import the Player class
from constants import *
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Instantiate the Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Clock object to control fps
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    # Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill((0, 0, 0))  # Fill screen black

        # Draw the player
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Control FPS / convert milliseconds to seconds
        dt = clock.tick(60) / 1000.0

# Add if statement
if __name__ == "__main__":
    main()

