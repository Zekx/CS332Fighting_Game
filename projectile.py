import pygame
from boxes import HitBox

class GinaFireBall(pygame.sprite.Sprite):

    def __init__(self, distance, x, y, width, height, damage = 0, hitstun = 0,
                 knockback = 0, knockdown = False, blocktype = 'stand',attack_level=1):
        """
        Initializes the information for Gina's fireball attack.
        :param distance:
        :param x:
        :param y:
        :param width:
        :param height:
        :param damage:
        :param hitstun:
        :param knockback:
        :param knockdown:
        :param blocktype:
        :param attack_level:
        :return:
        """

        self.hit_box = HitBox(x, y, width, height,damage, hitstun, knockback, knockdown, blocktype,attack_level)

        self.distance = distance
        self.distance_traveled = 0

        self.image = None
        self.fire_ball_animation = []

        for x in range(0, 10):
            self.fire_ball_animation.append(pygame.image.load('Sprites/other_sprites/FireBall_1.png'))
        for x in range(0, 30):
            self.fire_ball_animation.append(pygame.image.load('Sprites/other_sprites/FireBall_2.png'))
        for x in range(0, 6):
            self.fire_ball_animation.append(pygame.image.load('Sprites/other_sprites/FireBall_3.png'))
        for x in range(0, 6):
            self.fire_ball_animation.append(pygame.image.load('Sprites/other_sprites/FireBall_4.png'))
        for x in range(0, 6):
            self.fire_ball_animation.append(pygame.image.load('Sprites/other_sprites/FireBall_5.png'))

        self.image = self.fire_ball_animation[0]
        self.index = 0

        self.name = 'gina fireball'
        self.rect = self.image.get_rect()
        self.rect.x = self.hit_box.rect.x
        self.rect.y = self.hit_box.rect.y

        self.off_set = False

    def draw_box(self, game_display):
        """
        Draws Gina's fireball attack.
        :param game_display:
        :return:
        """

        if self.distance > 0 and self.off_set is False:
            self.off_set = True
            self.hit_box.rect.x += 75

        if self.distance > 0:
            # print(self.rect.x)
            self.hit_box.draw_box(game_display)
            game_display.blit(self.image, (self.rect.x, self.rect.y))
            self.rect.x += 5
            self.hit_box.rect.x += 5
            self.distance_traveled += 2
        else:
            self.hit_box.draw_box(game_display)
            game_display.blit(pygame.transform.flip(self.image, True, False),(self.rect.x, self.rect.y))
            self.rect.x -= 5
            self.hit_box.rect.x -= 5
            self.distance_traveled -= 2

        if self.index >= len(self.fire_ball_animation) - 1:
            self.index = len(self.fire_ball_animation) - 1
        else:
            self.index += 1

        self.image = self.fire_ball_animation[self.index]