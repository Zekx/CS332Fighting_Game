import pygame

REVEAL_BOXES = False

class HitBox(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, damage = 0, hitstun = 0,
                 knockback = 0, knockdown = False, blocktype = 'stand', attack_level = 1):
        self.damage = damage
        self.hitstun = hitstun
        self.knockback = knockback
        self.knockdown = knockdown
        self.blocktype = blocktype
        self.attack_level = attack_level

        self.hit_box = pygame.Surface((width, height))
        self.rect = self.hit_box.get_rect()
        self.rect.x = x
        self.rect.y = y

        if REVEAL_BOXES:
            self.hit_box.fill((200, 50, 50))
            self.hit_box.set_alpha(100)
        else:
            self.hit_box.set_alpha(0)

    def draw_box(self, game_display):
        game_display.blit(self.hit_box.convert_alpha(), (self.rect.x, self.rect.y))

class GrabBox(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        self.hit_box = pygame.Surface((width, height))
        self.rect = self.hit_box.get_rect()
        self.rect.x = x
        self.rect.y = y

        if REVEAL_BOXES:
            self.hit_box.fill((128, 0, 128))
            self.hit_box.set_alpha(100)
        else:
            self.hit_box.set_alpha(0)

    def draw_box(self, game_display):
        game_display.blit(self.hit_box.convert_alpha(), (self.rect.x, self.rect.y))

class HurtBox(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        self.name = 'hurt'
        self.hurt_box = pygame.Surface((width, height))
        self.rect = self.hurt_box.get_rect()
        self.rect.x = x
        self.rect.y = y

        if REVEAL_BOXES:
            self.hurt_box.fill((50, 200, 50))
            self.hurt_box.set_alpha(100)
        else:
            self.hurt_box.set_alpha(0)

    def draw_box(self, game_display):
        game_display.blit(self.hurt_box.convert_alpha(), (self.rect.x, self.rect.y))

class DamageBox(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        self.name = 'damage'
        self.hurt_box = pygame.Surface((width, height))
        self.rect = self.hurt_box.get_rect()
        self.rect.x = x
        self.rect.y = y

        if REVEAL_BOXES:
            self.hurt_box.fill((120, 250, 50))
            self.hurt_box.set_alpha(100)
        else:
            self.hurt_box.set_alpha(0)

    def draw_box(self, game_display):
        game_display.blit(self.hurt_box.convert_alpha(), (self.rect.x, self.rect.y))

class InvincibleBox(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        self.name = 'invinc'
        self.in_box = pygame.Surface((width, height))
        self.rect = self.in_box.get_rect()
        self.rect.x = x
        self.rect.y = y

        if REVEAL_BOXES:
            self.in_box.fill((255, 255, 61))
            self.in_box.set_alpha(100)
        else:
            self.in_box.set_alpha(0)

    def draw_box(self, game_display):
        game_display.blit(self.in_box.convert_alpha(), (self.rect.x, self.rect.y))

class Boundaries(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if REVEAL_BOXES:
            self.image.fill((100, 100, 100))
            self.image.set_alpha(50)
        else:
            self.image.set_alpha(0)

    def move_wall(self, x_change):
        self.x += x_change

    def draw_bounds(self, game_display):
        game_display.blit(self.image, (self.x, self.y))