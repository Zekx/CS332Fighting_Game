import pygame

class Effects(pygame.sprite.Sprite):

    def __init__(self):
        """
        Initializes the "abstract" class for all effects animation.
        :return:
        """

        self.image = None
        self.effects_animation = []
        self.index = 0

class ThrowDust(Effects):

    def __init__(self, x, y):
        """
        Initializes the animation for a throw impact.
        :param x:
        :param y:
        :return:
        """

        super().__init__()

        self.x = x
        self.y = y

        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_1.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_2.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_3.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_4.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_5.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_6.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_7.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_8.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_9.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_10.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_11.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_12.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_13.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_14.png'))
        for x in range(0, 4):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/slamdown_15.png'))

        self.image = self.effects_animation[0]
        self.index = 0

        self.name = 'throw dust'
        self.play_sound = True
        self.impact_sound = pygame.mixer.Sound('Sprites/sfx/sounds/2AH.wav')

    def draw_box(self, game_display):
        """
        Draws the impact animation onto the game screen.
        :param game_display:
        :return:
        """

        if self.play_sound:
            self.impact_sound.play()
            self.play_sound = False

        game_display.blit(self.image, (self.x, self.y))

        self.index += 1
        if self.index >= len(self.effects_animation) - 1:
            self.index = len(self.effects_animation) - 1

        self.image = self.effects_animation[self.index]

class DamageAnimation(Effects):

    def __init__(self, x, y, facing, attack_level):
        """
        Initializes the animation for a player being damaged.
        :param x:
        :param y:
        :param facing:
        :param attack_level:
        :return:
        """

        super().__init__()

        self.x = x
        self.y = y
        self.facing = facing

        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana00.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana01.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana02.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana03.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana04.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana05.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana06.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana07.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana08.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana09.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana10.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana11.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana12.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana13.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/hibana14.png'))

        self.image = self.effects_animation[0]
        self.index = 0

        self.name = 'damage animation'
        self.play_sound = True
        if attack_level == 1:
            self.damage_sound = pygame.mixer.Sound('Sprites/sfx/sounds/2BH.wav')
        elif attack_level == 2:
            self.damage_sound = pygame.mixer.Sound('Sprites/sfx/sounds/28H.wav')
        else:
            self.damage_sound = pygame.mixer.Sound('Sprites/sfx/sounds/29H.wav')

    def draw_box(self, game_display):
        """
        Draws the damage animation onto the game screen.
        :param game_display:
        :return:
        """

        if self.play_sound:
            self.damage_sound.play()
            self.play_sound = False

        if self.facing:
            game_display.blit(self.image.convert_alpha(), (self.x, self.y))
        else:
            game_display.blit(pygame.transform.flip((self.image), True, False).convert_alpha(), (self.x, self.y))

        self.index += 1
        if self.index >= len(self.effects_animation) - 1:
            self.index = len(self.effects_animation) - 1

        self.image = self.effects_animation[self.index]

class BlockAnimation(Effects):

    def __init__(self, x, y, facing):
        """
        Initializes the animation for a player blocking an attack.
        :param x:
        :param y:
        :param facing:
        :return:
        """

        super().__init__()

        self.x = x
        self.y = y
        self.facing = facing

        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_0.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_1.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_2.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_3.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_4.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_5.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_6.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_7.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_8.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_9.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_10.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_11.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_12.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_13.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_14.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_15.png'))
        for x in range(0, 3):
            self.effects_animation.append(pygame.image.load('Sprites/vfx/block_16.png'))

        self.image = self.effects_animation[0]
        self.index = 0

        self.name = 'block animation'
        self.play_sound = True
        self.block_sound = pygame.mixer.Sound('Sprites/sfx/sounds/2DH.wav')

    def draw_box(self, game_display):
        """
        Draws the blocking animation onto the game screen.
        :param game_display:
        :return:
        """

        if self.play_sound:
            self.block_sound.play()
            self.play_sound = False

        if self.facing:
            game_display.blit(pygame.transform.flip((self.image), True, False), (self.x, self.y))
        else:
            game_display.blit(self.image, (self.x, self.y))

        self.index += 1
        if self.index >= len(self.effects_animation) - 1:
            self.index = len(self.effects_animation) - 1

        self.image = self.effects_animation[self.index]