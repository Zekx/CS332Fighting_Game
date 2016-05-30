import pygame
from Gina import Gina
from Otis import Otis
from Player import Player
from fight_screen import FightScreen

class CharacterSelect():

    def __init__(self, mode):
        """
        Initializes the important variables for the the character selection screen. The select.image holds the menu
        screen showing all the characters for the game. The one_select and two_select is the cursors for player 1 and
        player 2. This method also holds all character portraits as well.
        :param mode:
        :return:
        """

        self.mode = mode
        self.player_one = None
        self.player_two = None

        self.select_image = pygame.image.load('Sprites/character_select.png')
        self.one_select = pygame.image.load('Sprites/p1_cursor.png')
        self.two_select = pygame.image.load('Sprites/p2_cursor.png')

        self.gina_image = pygame.transform.scale(pygame.image.load('Sprites/gina_selection.png'), (250, 400))
        self.otis_image = pygame.transform.scale(pygame.image.load('Sprites/otis_selection.png'), (250, 400))

    def select_screen(self, game_display):
        """
        The primary loop for the character select screen.

        0 = Gina
        1 = Otis (not available)
        :param game_display:
        :return:
        """

        select_loop = True
        fpsClock = pygame.time.Clock()
        cursor_selection = 300

        transition_out_once = True
        select_sound = pygame.mixer.Sound('Sprites/sfx/sounds/24H.wav')
        confirm_sound = pygame.mixer.Sound('Sprites/sfx/sounds/22H.wav')
        battle_sound = pygame.mixer.Sound('Sprites/sfx/sounds/9CH.wav')

        one_selection = 0
        one_cursor = 330
        character_one = None

        two_selection = 1
        two_cursor = 360
        character_two = None

        while select_loop is True:
            if transition_out_once:
                self.transitionOut(game_display, fpsClock)
                transition_out_once = False

            if character_one is not None and character_two is not None:
                battle_sound.play()
                pygame.time.wait(5000)
                self.transitionIn(game_display, fpsClock)
                start_fight = FightScreen(character_one, character_two)
                start_fight.game_condition()

                break

            game_display.blit(self.select_image, (0, 0))
            game_display.blit(self.one_select, (one_cursor, 450))
            game_display.blit(self.two_select, (two_cursor, 450))

            if one_selection == 0:
                game_display.blit(self.gina_image, (0, 200))
            else:
                game_display.blit(self.otis_image, (0, 200))

            if two_selection == 0:
                game_display.blit(pygame.transform.flip(self.gina_image, True, False), (550, 200))
            else:
                game_display.blit(pygame.transform.flip(self.otis_image, True, False), (550, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] and character_one is None:
                    select_sound.play()
                    if one_selection == 0:
                        one_cursor = 400
                        one_selection += 1
                    elif one_selection == 1:
                        one_cursor = 330
                        one_selection = 0
                if keys[pygame.K_d] and character_one is None:
                    select_sound.play()
                    if one_selection == 0:
                        one_cursor = 400
                        one_selection += 1
                    elif one_selection == 1:
                        one_cursor = 330
                        one_selection = 0

                if keys[pygame.K_u] and character_one is None:
                    if one_selection == 0:
                        confirm_sound.play()
                        character_one = Gina()
                    else:
                        pass

                if keys[pygame.K_LEFT] and character_two is None:
                    select_sound.play()
                    if two_selection == 0:
                        two_cursor = 360
                        two_selection += 1
                    elif two_selection == 1:
                        two_cursor = 300
                        two_selection = 0
                if keys[pygame.K_RIGHT] and character_two is None:
                    select_sound.play()
                    if two_selection == 0:
                        two_cursor = 360
                        two_selection += 1
                    elif two_selection == 1:
                        two_cursor = 300
                        two_selection = 0

                if keys[pygame.K_KP7] and character_two is None:
                    if two_selection == 0:
                        confirm_sound.play()
                        pygame.time.wait(500)
                        character_two = Gina()
                    else:
                        pass

            if character_one is not None:
                self.message_display('CONFIRMED', game_display, 50, 400)
            if character_two is not None:
                self.message_display('CONFIRMED', game_display, 500, 400)

            fpsClock.tick(60)
            pygame.display.flip()

    def transitionOut(self, screen, clock):
        """
        This method is used to transition into this menu. This menu starts off dark, but this method helps the
        game menu transition from dark to the actually character selection screen.
        :param screen:
        :param clock:
        :return:
        """

        transition = self.select_image
        for x in range(0, 200, 1):
            transition.set_alpha(x)
            screen.blit(transition, (0, 0))
            pygame.display.flip()
            clock.tick(120)

    def transitionIn(self, screen, clock):
        """
        This method darkens the screen using pygame.surface and gradually increases the alpha levels for a
        smoother transition between menus.
        :param screen:
        :param clock:
        :return:
        """

        transition = pygame.Surface((800, 600))
        for x in range(0, 256):
            transition.fill((0, 0, 0))
            transition.set_alpha(x)
            screen.blit(transition, (0, 0))
            pygame.display.flip()
            clock.tick(120)

    def message_display(self, str, game_display, x, y):
        """
        Simple message display to show on the screen.
        :param str:
        :param game_display:
        :param x:
        :param y:
        :return:
        """

        text = pygame.font.Font('Fonts/year_is_199x.ttf', 100)
        textSurface = text.render(str, True, (255, 255, 255))

        game_display.blit(textSurface, (x, y))