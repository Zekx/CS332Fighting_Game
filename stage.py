import pygame

class Stage():

    def __init__(self, bg, music):
        """
        Initializes the stage background and music appropriate for it.
        :param bg:
        :param music:
        :return:
        """

        self.bg = pygame.image.load(bg)
        pygame.mixer.music.load(music)