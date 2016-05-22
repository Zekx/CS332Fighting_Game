import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.name = None
        self.health = 0
        self.f_dash_speed = 0
        self.jump_height = 0
        self.meter = 0

        self.portrait = None
        self.image = None
        self.mask = None

        self.neutral_position = None
        self.dashImage = None
        self.jumpImage = None

        self.hit_box = []
        self.hurt_box = []

        self.standing = []
        self.crouching = []
        self.dash = []
        self.backdash = []
        self.jump = []
        self.walkFoward = []
        self.walkBackward = []

        self.hurt_animation = []
        self.stand_a_animation = []
        self.crouch_a_animation = []
        self.stand_b_animation = []
        self.crouch_b_animation = []
        self.stand_c_animation = []
        self.crouch_c_animation = []

        self.wakeup_animation = []