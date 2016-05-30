import pygame

# -- COLORS
YELLOW = (255, 228, 122)
BLUE = (100, 120, 250)
RED = (255, 100, 100)

WIDTH = 238
HEIGHT = 12

WIDTH_2 = 96
HEIGHT_2 = 22

class MagicSystem(pygame.sprite.Sprite):

    def __init__(self, player_one, player_two):
        """
        Initiates the bar to full with the two player portraits for the game. Game uses a yellow color for
        the health bar and will shorten in length over time.
        :return:
        """
        self.index_one = 0
        self.index_two = 0

        self.magic_bar_one = pygame.image.load('Sprites/Menu/magic_bar.png')
        self.magic_bar_two = pygame.image.load('Sprites/Menu/magic_bar.png')

        self.bar_one = pygame.Surface((70+(96-WIDTH_2*(player_one.meter_points/player_one.max_meter)), HEIGHT_2))
        self.under_one = pygame.Surface((WIDTH_2, HEIGHT_2))
        self.bar_one.fill(BLUE)
        self.under_one.fill(RED)

        self.bar_two = pygame.transform.flip(pygame.Surface((WIDTH_2, HEIGHT_2)), True, False)
        self.under_two = pygame.transform.flip(
            pygame.Surface((WIDTH_2, HEIGHT_2)), True, False
        )
        self.bar_two.fill(BLUE)
        self.under_two.fill(RED)

    def update_bar(self, player_one, player_two):
        if WIDTH_2*(player_one.meter_points/player_one.max_meter) <= 0:
            self.bar_one = pygame.Surface((1, HEIGHT_2))
        else:
            self.bar_one = pygame.Surface((WIDTH_2*(player_one.meter_points/player_one.max_meter), HEIGHT_2))
        self.bar_one.fill(BLUE)

        if WIDTH_2*(player_two.meter_points/player_two.max_meter) <= 0:
            self.bar_two = pygame.transform.flip(pygame.Surface((1, HEIGHT_2)), True, False)
        else:
            self.bar_two = pygame.transform.flip(pygame.Surface(
                (WIDTH_2*(player_two.meter_points/player_two.max_meter), HEIGHT_2)), True, False)
        self.bar_two.fill(BLUE)

    def show_bar(self, game_display, player_one, player_two):
        """
        Draws the health bar and portrait of the players onto the game screen.
        :param game_display:
        :param player_one:
        :param player_two:
        :return:
        """
        self.update_bar(player_one, player_two)

        game_display.blit(self.under_one, (10, 550))
        game_display.blit(self.bar_one, (15+(95-WIDTH_2*(player_one.meter_points/player_one.max_meter)), 550))

        game_display.blit(self.under_two, (680, 550))
        game_display.blit(self.bar_two, (680, 550))

        game_display.blit(self.magic_bar_one, (10, 550))
        game_display.blit(self.magic_bar_two, (680, 550))

class HealthSystem(pygame.sprite.Sprite):
    """
    Generates the image of a bar and the character portrait for the game.
    """

    def __init__(self, player_one, player_two):
        """
        Initiates the bar to full with the two player portraits for the game. Game uses a yellow color for
        the health bar and will shorten in length over time.
        :return:
        """
        self.index_one = 0
        self.index_two = 0

        self.health_bar = pygame.image.load('Sprites/Menu/healthbar.png')

        self.bar_one = pygame.Surface((112+(238-WIDTH*(player_one.health_points/player_one.max_health)), HEIGHT))
        self.under_one = pygame.Surface((WIDTH, HEIGHT))
        self.bar_one.fill(YELLOW)
        self.under_one.fill(RED)

        self.bar_two = pygame.transform.flip(pygame.Surface((WIDTH, HEIGHT)), True, False)
        self.under_two = pygame.transform.flip(
            pygame.Surface((WIDTH*(player_two.health_points/player_two.max_health), HEIGHT)), True, False
        )
        self.bar_two.fill(YELLOW)
        self.under_two.fill(RED)

    def update_bar(self, player_one, player_two):
        if WIDTH*(player_one.health_points/player_one.max_health) <= 0:
            self.bar_one = pygame.Surface((1, HEIGHT))
        else:
            self.bar_one = pygame.Surface((WIDTH*(player_one.health_points/player_one.max_health), HEIGHT))
        self.bar_one.fill(YELLOW)

        if WIDTH*(player_two.health_points/player_two.max_health) <= 0:
            self.bar_two = pygame.transform.flip(pygame.Surface((1, HEIGHT)), True, False)
        else:
            self.bar_two = pygame.transform.flip(pygame.Surface(
                (WIDTH*(player_two.health_points/player_two.max_health), HEIGHT)), True, False)
        self.bar_two.fill(YELLOW)

    def show_bar(self, game_display, player_one, player_two):
        """
        Draws the health bar and portrait of the players onto the game screen.
        :param game_display:
        :param player_one:
        :param player_two:
        :return:
        """
        self.update_bar(player_one, player_two)

        game_display.blit(player_one.character.portrait, (12, 7))
        game_display.blit(self.under_one, (111, 17))
        game_display.blit(self.bar_one, (112+(238-WIDTH*(player_one.health_points/player_one.max_health)), 17))

        game_display.blit(player_two.character.portrait, (702, 7))
        game_display.blit(self.under_two, (450, 17))
        game_display.blit(self.bar_two, (450, 17))

        game_display.blit(self.health_bar, (0, 0))