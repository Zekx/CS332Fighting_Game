from title_screen import TitleScreen
import pygame

def main_loop():
    """
    Begins the main loop of Conflict Resolution. This method calls for the title screen loop.
    :return:
    """

    title = TitleScreen()
    title.title_loop()

if __name__ == '__main__':
    pygame.init()

    main_loop()