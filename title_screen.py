import pygame
from character_select import CharacterSelect

class TitleScreen():

    def __init__(self):
        """
        Initializes the images for the title screen loop. self.image holds the primary image and self.cursor
        holds the image for the cursor selection of the title screen.

        current_selection is the variable that decides the following option that comes when the user presses
        the select button on the title screen.
        :return:
        """

        self.image = pygame.image.load('Sprites/title_screen.png')
        self.cursor = pygame.image.load('Sprites/title_cursor.png')
        self.current_selection = 0

    def title_loop(self):
        """
        The main loop of the title screen. The user can begin the player vs. player session or exit the game.
        This loop also intializes the the window screen size.

        If the current_selection is 0, then the game enters the player vs. player game.
        If the current_selection is 1, then the game exits.
        :return:
        """

        pygame.init()
        title_loop = True
        display_width = 800
        display_height = 600
        game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Conflict Resolution')

        fpsClock = pygame.time.Clock()

        cursor_selection = 300
        character_screen = CharacterSelect(self.current_selection)
        select_sound = pygame.mixer.Sound('Sprites/sfx/sounds/24H.wav')
        confirm_sound = pygame.mixer.Sound('Sprites/sfx/sounds/22H.wav')

        while title_loop is True:
            game_display.blit(self.image, (0, 0))
            game_display.blit(self.cursor, (165, cursor_selection))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    select_sound.play()
                    if self.current_selection == 0:
                        cursor_selection = 400
                        self.current_selection += 1
                    elif self.current_selection == 1:
                        cursor_selection = 300
                        self.current_selection = 0

                if keys[pygame.K_s]:
                    select_sound.play()
                    if self.current_selection == 0:
                        cursor_selection = 400
                        self.current_selection += 1
                    elif self.current_selection == 1:
                        cursor_selection = 300
                        self.current_selection = 0

                elif keys[pygame.K_u]:
                    if self.current_selection == 0:
                        confirm_sound.play()
                        self.transitionIn(game_display, fpsClock)
                        character_screen.select_screen(game_display)
                    else:
                        pygame.quit()
                        quit()

            fpsClock.tick(60)
            pygame.display.flip()

    def transitionIn(self, screen, fpsClock):
        """
        This method darkens the screen using pygame.surface and gradually increases the alpha levels for a
        smoother transition between menus.
        :param screen:
        :param fpsClock:
        :return:
        """

        transition = pygame.Surface((800, 600))
        for x in range(0, 256):
            transition.fill((0, 0, 0))
            transition.set_alpha(x)
            screen.blit(transition, (0, 0))
            pygame.display.flip()
            fpsClock.tick(120)