# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
'''each .py file is a module, and we can import functions, variables, and classes from one module into another with the import statement. The name of a module is the filename (without the .py extension).'''
import constants
# write fucntion that prints "Starting astroids"
# add if stament to end of file
def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
'''
This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.
'''


