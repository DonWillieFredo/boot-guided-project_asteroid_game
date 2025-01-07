# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
'''each .py file is a module, and we can import functions, variables, and classes from one module into another with the import statement. The name of a module is the filename (without the .py extension).'''
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# write fucntion that prints "Starting astroids"
def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()

        
# add if statement
if __name__ == "__main__":
    main()
'''
This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.
'''


