import pygame
from boxes import HurtBox
from boxes import HitBox
from boxes import InvincibleBox
from Character import Character

class Gina(Character):

    def __init__(self):
        super().__init__()

        self.name = 'Gina'
        self.health = 200
        self.meter = 0
        self.jump_height = 400
        self.portrait = pygame.image.load('Sprites/Gina/GinaPortrait.png')

        self.image = pygame.image.load('Sprites/Gina/GinaStand1.png')
        self.rect = self.image.get_rect()
        self.x_offset = 10
        self.y_offset = 30

        self.dashImage = pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFDash.png'), (180, 250))
        self.neutralPosition = pygame.image.load('Sprites/Gina/GinaStand1.png')
        self.jumpImage = pygame.image.load('Sprites/Gina/GinaJump4.png')

        # The following loops add in all of the sprites for the animation...

        # Inserts Gina's standing animation.
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStand1.png'), (130, 250)))
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStand2.png'), (130, 250)))
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStand3.png'), (130, 250)))

        #Inserts Gina's crouching animation.
        for x in range(0, 30):
            self.crouching.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaCrouch1.png'), (130, 250)))
        for x in range(0, 30):
            self.crouching.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaCrouch2.png'), (130, 250)))
        for x in range(0, 30):
            self.crouching.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaCrouch3.png'), (130, 250)))

        #Inserts Gina's dash animation.
        for x in range(0, 85):
            self.dash.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFDash.png'), (180, 250)))

        #Inserts Gina's back-dash animation.
        for x in range(0, 75):
            self.backdash.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaBDash.png'), (150, 250)))

        #Inserts Gina's jumping animation.
        for x in range(0, 30):
            self.jump.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'), (130, 250)))
        for x in range(0, 30):
            self.jump.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'), (130, 250)))
        for x in range(0, 80):
            self.jump.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250)))
        for x in range(0, 100):
            self.jump.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'), (130, 250)))

        #Inserts Gina's Forward walking animation.
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk1.png'), (130, 250)))
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk2.png'), (130, 250)))
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk3.png'), (130, 250)))
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk4.png'), (130, 250)))
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk5.png'), (130, 250)))
        for x in range(0, 15):
            self.walkFoward.append(pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaFWalk6.png'), (130, 250)))

        #Inserts Gina's Backward walking animation.
        for x in range(0, 20):
            self.walkBackward.append(pygame.transform.scale(
                    pygame.image.load('Sprites/Gina/GinaBWalk1.png'), (130, 250)))
        for x in range(0, 20):
            self.walkBackward.append(pygame.transform.scale(
                    pygame.image.load('Sprites/Gina/GinaBWalk2.png'), (130, 250)))
        for x in range(0, 20):
            self.walkBackward.append(pygame.transform.scale(
                    pygame.image.load('Sprites/Gina/GinaBWalk3.png'), (130, 250)))
        for x in range(0, 20):
            self.walkBackward.append(pygame.transform.scale(
                    pygame.image.load('Sprites/Gina/GinaBWalk4.png'), (130, 250)))

        # Inserts Gina's standing A attack animation.
        for x in range(0, 2):
            self.stand_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandA1.png'), (130, 250)
            ))
        for x in range(0, 2):
            self.stand_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandA2.png'), (130, 250)
            ))
        for x in range(0, 6):
            self.stand_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandA3.png'), (150, 250)
            ))
        for x in range(0, 3):
            self.stand_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandA2.png'), (130, 250)
            ))

        # Inserts Gina's crouching A attack animation.
        for x in range(0, 4):
            self.crouch_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchA1.png'), (150, 250)
            ))
        for x in range(0, 4):
            self.crouch_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchA2.png'), (150, 250)
            ))
        for x in range(0, 6):
            self.crouch_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchA3.png'), (150, 250)
            ))
        for x in range(0, 6):
            self.crouch_a_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchA2.png'), (150, 250)
            ))

        # Inserts Gina's standing B attack animation
        for x in range(0, 3):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB1-1.png'), (200, 250)
            ))
        for x in range(0, 4):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB1.png'), (200, 250)
            ))
        for x in range(0, 6):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB2.png'), (200, 250)
            ))
        for x in range(0, 13):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB3.png'), (200, 250)
            ))
        for x in range(0, 7):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB4.png'), (200, 250)
            ))
        for x in range(0, 5):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB1.png'), (200, 250)
            ))
        for x in range(0, 3):
            self.stand_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandB1-1.png'), (200, 250)
            ))

        # Inserts Gina's crouching B attack animation
        for x in range(0, 8):
            self.crouch_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchB1.png'), (130, 250)
            ))
        for x in range(0, 6):
            self.crouch_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchB2.png'), (130, 250)
            ))
        for x in range(0, 6):
            self.crouch_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchB3.png'), (130, 250)
            ))
        for x in range(0, 8):
            self.crouch_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchB2.png'), (130, 250)
            ))
        for x in range(0, 8):
            self.crouch_b_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchB1.png'), (130, 250)
            ))

        # Inserts Gina's standing C attack animation
        for x in range(0, 4):
            self.stand_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandC1.png'), (130, 250)
            ))
        for x in range(0, 8):
            self.stand_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandC2.png'), (160, 250)
            ))
        for x in range(0, 9):
            self.stand_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandC3.png'), (160, 250)
            ))
        for x in range(0, 8):
            self.stand_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandC4.png'), (130, 250)
            ))
        for x in range(0, 10):
            self.stand_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaStandC5.png'), (130, 250)
            ))

        # Inserts Gina's crouching C attack animation
        for x in range(0, 6):
            self.crouch_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchC1.png'), (230, 250)
            ))
        for x in range(0, 8):
            self.crouch_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchC3.png'), (230, 250)
            ))
        for x in range(0, 10):
            self.crouch_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchC4.png'), (230, 250)
            ))
        for x in range(0, 10):
            self.crouch_c_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/Attacks/GinaCrouchC3.png'), (230, 250)
            ))

        # Inserts Gina's wakeup animation
        for x in range(0, 40):
            self.wakeup_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/GinaKnockdown.png'), (240, 130)
            ))
        for x in range(0, 20):
            self.wakeup_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/GinaWakeUp1.png'), (240, 180)
            ))
        for x in range(0, 20):
            self.wakeup_animation.append(pygame.transform.scale(
                pygame.image.load('Sprites/Gina/GinaWakeUp2.png'), (250, 180)
            ))
    # ----------------------------------------------------------------------------------------------------------------

    def update_hurt_box(self, player):
        # Assigns initial hurtboxes and hitboxes for the character...
        self.hurt_box.clear()
        if player.facingRight:
            if not player.setAction:
                if player.crouching:
                    self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
                else:
                    self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value,
                                             player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.isDashing:
                self.hurt_box.append(HurtBox(player.x + 70 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.isJumping or player.isDescending:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height - 30))
            elif player.attack_a:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_a:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
            elif player.attack_b:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_b:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
            elif player.attack_c:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_c:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 120, self.rect.width, self.rect.height - 50))
        else:
            if not player.setAction:
                if player.crouching:
                    self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
                else:
                    self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value,
                                             player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.isDashing:
                self.hurt_box.append(HurtBox(
                        (player.x + 20)+ player.off_set_value
                        , (player.y + 30), self.rect.width + 10, self.rect.height + 30))
            elif player.isJumping or player.isDescending:
                self.hurt_box.append(HurtBox(
                        (player.x + 20) + player.off_set_value
                        , (player.y + 30), self.rect.width + 10, self.rect.height - 30))
            elif player.attack_a:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_a:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
            elif player.attack_b:
                self.hurt_box.append(HurtBox(player.x + 180 - player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_b:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 70, self.rect.width, self.rect.height - 20))
            elif player.attack_c:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 30, self.rect.width + 10, self.rect.height + 30))
            elif player.crouch_attack_c:
                self.hurt_box.append(HurtBox(player.x + 20 + player.off_set_value
                                             , player.y + 120, self.rect.width, self.rect.height - 50))

    # -----------------------------------------------------------------------------------------------------------------

    def stand_a(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.stand_a_animation)-1:
                player.index = 0
            else:
                if player.index > 8 and player.index < 10 and player.hit_box_fill_once is not True:
                    stand_a_hit_box = HitBox(player.x + 100, player.y + 80, 50, 50, damage=5, hitstun=8, knockback= 3,
                                 knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_a_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = player.character.stand_a_animation[player.index]
                player.index += 1
        else:
            if player.index > len(player.character.stand_a_animation)-1:
                player.index = 0
            else:
                if player.index >= 4 and player.index <= 9:
                    if player.off_set is False:
                        player.x -= 17
                        player.off_set = True
                        player.off_set_value = 17
                else:
                    if player.off_set is True:
                        player.x += 17
                        player.off_set = False
                        player.off_set_value = 0
                if player.index > 8 and player.index < 10 and player.hit_box_fill_once is not True:
                    stand_a_hit_box = HitBox(player.x - 20 + player.off_set_value, player.y + 80, 50, 50,
                                             damage=5, hitstun=8, knockback= 3,knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_a_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = \
                    pygame.transform.flip(player.character.stand_a_animation[player.index], True, False)
                player.index += 1

        if player.index > 12:
            self.hit_box.clear()

        if player.index >= len(player.character.stand_a_animation):
            player.setAction = False
            player.attack_a = False
            player.hit_box_fill_once = False

    def crouch_a(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.crouch_a_animation)-1:
                player.index = 0
            else:
                if player.index == 7:
                    player.x += 4
                if player.index > 10 and player.index < 12 and player.hit_box_fill_once is not True:
                    stand_a_hit_box = HitBox(player.x + 100, player.y + 100, 70, 50, damage=5, hitstun=16, knockback= 2,
                                 knockdown= False, blocktype='crouch')
                    self.hit_box.append(stand_a_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = player.character.crouch_a_animation[player.index]
                player.index += 1
        else:
            if player.index > len(player.character.crouch_a_animation)-1:
                player.index = 0
            else:
                if player.index >= 0 and player.index < len(player.character.crouch_a_animation)-1:
                    if player.off_set is False:
                        player.x -= 20
                        player.off_set = True
                        player.off_set_value = 20
                else:
                    if player.off_set is True:
                        player.x += 20
                        player.off_set = False
                        player.off_set_value = 0
                if player.index == 7:
                    player.x -= 4
                if player.index > 10 and player.index < 12 and player.hit_box_fill_once is not True:
                    stand_a_hit_box = HitBox(player.x - 20 + player.off_set_value, player.y + 100, 70, 50,
                                             damage=5, hitstun=16, knockback= 2,knockdown= False, blocktype='crouch')
                    self.hit_box.append(stand_a_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = \
                    pygame.transform.flip(player.character.crouch_a_animation[player.index], True, False)
                player.index += 1

        if player.index > 12:
            self.hit_box.clear()

        if player.index >= len(player.character.crouch_a_animation):
            player.setAction = False
            pygame.transform.flip(
                     pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaCrouch1.png'), (130, 250))
                    , True, False)
            player.crouch_attack_a = False
            player.hit_box_fill_once = False

    def stand_b(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.stand_b_animation):
                player.index = 0
            else:
                if player.index == 5:
                    player.x += 10
                if player.index > 9 and player.index < 18 and player.hit_box_fill_once is not True:
                    stand_b_hit_box = HitBox(player.x + 160, player.y + 120, 50, 50, damage=15, hitstun=20, knockback= 4,
                                 knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_b_hit_box)
                    player.hit_box_fill_once = True

                if player.index > 7 and player.index < 20:
                    self.hurt_box.append(HurtBox(player.x + 130 + player.off_set_value,
                                             player.y + 120, 100, 60))
                player.character.image = player.character.stand_b_animation[player.index]
                if player.index == 34:
                    player.x -= 10

            player.index += 1

            if player.index > 19:
                self.hit_box.clear()
        else:
            if player.index == 5:
                    player.x -= 10
            if player.index >= 0 and player.index < len(player.character.stand_b_animation)-1:
                if player.off_set is False:
                    player.x -= 85
                    player.off_set = True
                    player.off_set_value = 85
            else:
                if player.off_set is True:
                    player.x += 85
                    player.off_set = False
                    player.off_set_value = 0

            if player.index >= 9 and player.index < 18 and player.hit_box_fill_once is not True:
                stand_b_hit_box = HitBox(player.x - 90 + player.off_set_value, player.y + 120, 50, 50,
                                             damage=15, hitstun=20, knockback= 4,knockdown= False, blocktype='stand')
                self.hit_box.append(stand_b_hit_box)
                player.hit_box_fill_once = True

            if player.index > 7 and player.index < 20:
                    self.hurt_box.append(HurtBox(player.x - 115 + player.off_set_value,
                                             player.y + 120, 100, 60))
            if player.index > len(player.character.stand_b_animation) - 1:
                player.character.image = \
                pygame.transform.flip(player.character.stand_b_animation[player.index-2], True, False)
            else:
                player.character.image = \
                pygame.transform.flip(player.character.stand_b_animation[player.index], True, False)

            if player.index == 34:
                    player.x += 10

            if player.index > 19:
                self.hit_box.clear()

            player.index += 1

        if player.index > len(player.character.stand_b_animation)-1:
                player.character.image = \
                pygame.transform.flip(
                     pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStand1.png'), (130, 250))
                    , True, False)

                player.setAction = False
                player.off_set = False
                player.off_set_value = 0
                player.attack_b = False
                player.hit_box_fill_once = False


    def crouch_b(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.crouch_b_animation)-1:
                player.index = 0
            else:
                if player.index > 12 and player.index < 18 and player.hit_box_fill_once is not True:
                    stand_a_hit_box = HitBox(player.x + 70, player.y, 80, 100, damage=15, hitstun=12, knockback= 3,
                                 knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_a_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = player.character.crouch_b_animation[player.index]
                player.index += 1
        else:
            if player.index > len(player.character.crouch_b_animation)-1:
                player.index = 0
            else:
                if player.index >= 12 and player.index <= 18:
                    if player.off_set is False:
                        player.x -= 0
                        player.off_set = True
                        player.off_set_value = 0
                else:
                    if player.off_set is True:
                        player.x += 0
                        player.off_set = False
                        player.off_set_value = 0
                if player.index > 12 and player.index < 18 and player.hit_box_fill_once is not True:
                    crouch_b_hit_box = HitBox(player.x - 20 + player.off_set_value, player.y, 80, 100,
                                             damage=15, hitstun=12, knockback= 3,knockdown= False, blocktype='stand')
                    self.hit_box.append(crouch_b_hit_box)
                    player.hit_box_fill_once = True
                player.character.image = \
                    pygame.transform.flip(player.character.crouch_b_animation[player.index], True, False)
                player.index += 1

        if player.index > 18:
            self.hit_box.clear()

        if player.index >= len(player.character.crouch_b_animation):
            player.setAction = False
            player.crouch_attack_b = False
            player.hit_box_fill_once = False

    def stand_c(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.stand_c_animation)-1:
                player.index = 0
            else:
                if player.index > 13 and player.index < 25 and player.hit_box_fill_once is not True:
                    stand_c_hit_box_1 = HitBox(player.x + 100, player.y + 50, 80, 70,
                                             damage=20, hitstun=12, knockback= 3,
                                                knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_c_hit_box_1)
                    player.hit_box_fill_once = True
                if player.index > 26 and player.index < 34 and player.hit_box_fill_twice is not True:
                    stand_c_hit_box_2 = HitBox(player.x + 110, player.y + 40, 80, 70,
                                             damage=20, hitstun=12, knockback= -3,
                                                knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_c_hit_box_2)
                    player.hit_box_fill_twice = True
                if player.index > 10 and player.index < 35:
                    self.hurt_box.append(HurtBox(player.x + 100 + player.off_set_value,
                                             player.y + 55, 100, 60))
                player.character.image = player.character.stand_c_animation[player.index]
                player.index += 1
        else:
            if player.index > len(player.character.stand_c_animation)-1:
                player.index = 0
            else:
                if player.index >= 4 and player.index <= 20:
                    if player.off_set is False:
                        player.x -= 20
                        player.off_set = True
                        player.off_set_value = 20
                else:
                    if player.off_set is True:
                        player.x += 20
                        player.off_set = False
                        player.off_set_value = 0
                if player.index > 13 and player.index < 25 and player.hit_box_fill_once is not True:
                    stand_c_hit_box_1 = HitBox(player.x - 40 + player.off_set_value, player.y + 50, 80, 70,
                                             damage=5, hitstun=12, knockback= 3,knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_c_hit_box_1)
                    player.hit_box_fill_once = True
                if player.index > 26 and player.index < 34 and player.hit_box_fill_twice is not True:
                    stand_c_hit_box_2 = HitBox(player.x - 50 + player.off_set_value, player.y + 40, 80, 70,
                                             damage=20, hitstun=12, knockback= -3,
                                                knockdown= False, blocktype='stand')
                    self.hit_box.append(stand_c_hit_box_2)
                    player.hit_box_fill_twice = True
                if player.index > 10 and player.index < 35:
                    self.hurt_box.append(HurtBox(player.x - 60 + player.off_set_value,
                                             player.y + 55, 100, 60))
                player.character.image = \
                    pygame.transform.flip(player.character.stand_c_animation[player.index], True, False)
                player.index += 1

        if player.index > 35:
            self.hit_box.clear()

        if player.index >= len(player.character.stand_c_animation):
            player.setAction = False
            player.attack_c = False
            player.hit_box_fill_once = False
            player.hit_box_fill_twice = False

    def crouch_c(self, player):
        if player.setAction is False:
            if player.facingRight is True:
                player.multiplier = 1
            else:
                player.multiplier = -1
            player.index = 0
            player.setAction = True

        if player.multiplier == 1:
            if player.index > len(player.character.crouch_c_animation)-1:
                player.index = 0
            if player.index >= 14 and player.index <= 24 and player.hit_box_fill_once is not True:
                    crouch_c_hit_box_1 = HitBox(player.x + 130, player.y + 200, 100, 20,
                                             damage=12, hitstun=15, knockback= 1,
                                                knockdown= True, blocktype='sweep')
                    self.hit_box.append(crouch_c_hit_box_1)
                    player.hit_box_fill_once = True

            player.character.image =  player.character.crouch_c_animation[player.index]
            player.index += 1
        else:
            if player.index > len(player.character.crouch_c_animation)-1:
                player.index = 0
            if player.index >= 0 and player.index < len(player.character.crouch_c_animation)-1:
                if player.off_set is False:
                    player.x -= 100
                    player.off_set = True
                    player.off_set_value = 90
            else:
                if player.off_set is True:
                    player.x += 100
                    player.off_set = False
                    player.off_set_value = 0

            if player.index >= 14 and player.index <= 24 and player.hit_box_fill_once is not True:
                crouch_c_hit_box_1 = HitBox(player.x, player.y + 200, 100, 20,
                                            damage=12, hitstun=15, knockback= 1,
                                            knockdown= True, blocktype='sweep')
                self.hit_box.append(crouch_c_hit_box_1)
                player.hit_box_fill_once = True

            player.character.image = \
            pygame.transform.flip(player.character.crouch_c_animation[player.index], True, False)
            player.index += 1

        if player.index > 24:
            self.hit_box.clear()

        if player.index > len(player.character.crouch_c_animation)-1:
            if player.multiplier == 1:
                player.character.image = player.character.crouching[0]
            else:
                player.character.image = \
                pygame.transform.flip(player.character.crouching[0], True, False)

            player.setAction = False
            player.crouch_attack_c = False
            player.hit_box_fill_once = False
    # -----------------------------------------------------------------------------------------------------------------

    def being_damaged(self, player):
        if player.facingRight and not player.setAction:
            player.multiplier = -1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.multiplier = 1
            player.setAction = True

        if player.facingRight:
            if player.hitstun > player.max_hitstun/2:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt1.png'), (130, 250))
            else:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt2.png'), (130, 250))

            player.hitstun -= 1
        else:
            if player.hitstun > player.max_hitstun/2:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt1.png'),
                                               (130, 250)), True, False)
            else:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt2.png'),
                                               (130, 250)), True, False)

            player.hitstun -= 1
        player.x += player.knockback * player.multiplier

        if player.hitstun <= 0:
            if player.knockdown is True:
                player.y = player.yKnockdown

                if player.facingRight:

                    player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaKnockdown.png'), (250, 130))
                    player.getting_up = True
                else:
                    player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaKnockdown.png'),
                                               (250, 130)), True, False)
                    player.getting_up = True

            player.got_hit = False
            player.setAction = False
            player.hitstun = 0
            player.max_hitstun = 0
            player.knockback = 0

    def being_air_damaged(self, player):
        if player.facingRight and not player.setAction:
            player.isJumping = False
            player.isDescending = False
            player.multiplier = -1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.isJumping = False
            player.isDescending = False
            player.multiplier = 1
            player.setAction = True

        if player.facingRight:
            if player.hitstun > player.max_hitstun/2:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt1.png'), (130, 250))
                player.y -= 7
                player.current_jump += 15
            elif player.hitstun > player.max_hitstun/4 and player.hitstun < player.max_hitstun/2:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt2.png'), (130, 250))
            elif player.hitstun < player.max_hitstun/4:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaAirHurt.png'), (150, 280))
                player.y += 7
                player.current_jump -= 8
            player.hitstun -= 1
        else:
            if player.hitstun > player.max_hitstun/2:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt1.png'),
                                               (130, 250)), True, False)
                player.y -= 7
                player.current_jump += 15
            elif player.hitstun > player.max_hitstun/4 and player.hitstun < player.max_hitstun/2:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaHurt2.png'),
                                               (130, 250)), True, False)
            elif player.hitstun < player.max_hitstun/4:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaAirHurt.png'),
                                               (150, 280)), True, False)
                player.y += 7
                player.current_jump -= 8
            player.hitstun -= 1
        player.x += player.knockback * 1.5 * player.multiplier

        if player.current_jump <= 0:
            player.knockdown = True
            if player.facingRight:
                player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaKnockdown.png'), (250, 130))
                player.getting_up = True
            else:
                player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaKnockdown.png'),
                                               (250, 130)), True, False)
                player.getting_up = True

            player.current_jump = 0
            player.y = player.yKnockdown

            player.got_air_hit = False
            player.setAction = False
            player.isJumping = False

            player.neutral_jumping = False
            player.forward_jumping = False
            player.back_jumping = False
            player.isDescending = False

            player.hitstun = 0
            player.max_hitstun = 0
            player.knockback = 0

    def wake_up(self, player):
        if player.facingRight and not player.setAction:
            player.index = 0
            player.multiplier = 1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.index = 0
            player.multiplier = -1
            player.setAction = True

        if player.facingRight:
            if player.index > len(player.character.wakeup_animation)-1:
                player.index = 0
            else:
                if player.index >= 0 and player.index < 40:
                    self.hurt_box.append(InvincibleBox(player.x + 20 + player.off_set_value
                                             , player.y, self.rect.width + 30, self.rect.height - 50))
                elif player.index >= 40 and player.index < len(player.character.wakeup_animation)-1:
                    self.hurt_box.append(InvincibleBox(player.x + 20 + player.off_set_value
                                             , player.y, self.rect.width + 30, self.rect.height - 50))

                if player.index >= 40 and player.index < len(player.character.wakeup_animation)-1:
                    if player.off_set is False:
                        player.y -= 60
                        player.off_set = True
                        player.off_set_value = 0
                else:
                    if player.off_set is True:
                        player.y += 60
                        player.off_set = False
                        player.off_set_value = 0
                player.character.image = player.character.wakeup_animation[player.index]
                player.index += 1
        else:
            if player.index > len(player.character.wakeup_animation)-1:
                player.index = 0
            else:
                if player.index >= 0 and player.index < 40:
                    self.hurt_box.append(InvincibleBox(player.x + 20 + player.off_set_value
                                             , player.y, self.rect.width + 30, self.rect.height - 50))
                elif player.index >= 40 and player.index < len(player.character.wakeup_animation)-1:
                    self.hurt_box.append(InvincibleBox(player.x + 20 + player.off_set_value
                                             , player.y, self.rect.width + 30, self.rect.height - 50))

                if player.index >= 40 and player.index < len(player.character.wakeup_animation)-1:
                    if player.off_set is False:
                        player.y -= 60
                        player.x -= 50
                        player.off_set = True
                        player.off_set_value = 50
                else:
                    if player.off_set is True:
                        player.y += 60
                        player.x += 50
                        player.off_set = False
                        player.off_set_value = 0
                player.character.image = pygame.transform.flip(
                            player.character.wakeup_animation[player.index], True, False)
                player.index += 1

        if player.index > len(player.character.wakeup_animation) - 1:
            if player.facingRight:
                player.character.image = player.character.standing[0]
            else:
                player.character.image = pygame.transform.flip(player.character.standing[0], True, False)
            player.knockdown = False
            player.getting_up = False
            player.setAction = False
            player.y = player.yOriginal

    def being_blocked(self, player):
        if player.facingRight and not player.setAction:
            player.multiplier = -1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.multiplier = 1
            player.setAction = True

        if player.facingRight:
            if player.hitstun > 0:
                if player.blockingLow:
                    player.character.image = \
                                pygame.transform.scale(pygame.image.load
                                                       ('Sprites/Gina/GinaCrouchBlock.png'), (130, 250))
                else:
                    player.character.image = \
                                pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStandBlock.png'), (130, 250))

            player.hitstun -= 1
        else:
            if player.hitstun > 0:
                if player.blockingLow:
                    player.character.image = pygame.transform.flip(
                                pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaCrouchBlock.png'),
                                                   (130, 250)), True, False)
                else:
                    player.character.image = pygame.transform.flip(
                                pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaStandBlock.png'),
                                                   (130, 250)), True, False)

            player.hitstun -= 1
        player.x += player.knockback * player.multiplier

        if player.hitstun <= 0:
            player.block_hit = False
            player.setAction = False
            player.hitstun = 0
            player.max_hitstun = 0
            player.knockback = 0

    # -----------------------------------------------------------------------------------------------------------------
    def jumping(self, player):
        if player.facingRight and not player.setAction:
            player.index = 0
            player.multiplier = 1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.index = 0
            player.multiplier = -1
            player.setAction = True
        if player.back_jumping:
            if player.isJumping:
                if player.current_jump < len(player.character.jump)/6:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'),
                                                   (130, 250)), True, False)
                    player.y -= 0
                elif player.current_jump > len(player.character.jump)/6 and \
                                    player.current_jump < len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'),
                                               (130, 250)), True, False)
                    player.y -= 12.2
                    player.x -= 10
                elif player.current_jump > len(player.character.jump)/4 and \
                                    player.current_jump < len(player.character.jump)/1.7:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y -= 18.1
                    player.x -= 8
                elif player.current_jump > len(player.character.jump)/1.7 and \
                                    player.current_jump < len(player.character.jump):
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'),
                                               (130, 250)), True, False)
                    player.y -= 15.3
                    player.x -= 7
                elif player.current_jump > len(player.character.jump):
                    player.y -= 12.1
                player.current_jump += 12.0
            elif player.isDescending:
                if player.current_jump < len(player.character.jump) and \
                                   player.current_jump > len(player.character.jump)/1.7:
                    player.y += 10
                    player.x -= 7
                elif player.current_jump < len(player.character.jump)/1.7 and \
                                    player.current_jump > len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y += 15
                    player.x -= 6
                elif player.current_jump < len(player.character.jump)/4 and \
                                    player.current_jump > len(player.character.jump)/6:
                    player.y += 18
                    player.x -= 5
                elif player.current_jump < len(player.character.jump)/6:
                    player.y += 22
                player.current_jump -= 12.0
        elif player.forward_jumping:
            if player.isJumping:
                if player.current_jump < len(player.character.jump)/6:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'),
                                                   (130, 250)), True, False)
                    player.y -= 0
                elif player.current_jump > len(player.character.jump)/6 and \
                                    player.current_jump < len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'),
                                               (130, 250)), True, False)
                    player.y -= 12.2
                    player.x += 4
                elif player.current_jump > len(player.character.jump)/4 and \
                                    player.current_jump < len(player.character.jump)/1.7:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y -= 17.1
                    player.x += 6
                elif player.current_jump > len(player.character.jump)/1.7 and \
                                    player.current_jump < len(player.character.jump):
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'),
                                               (130, 250)), True, False)
                    player.y -= 15.3
                    player.x += 8
                elif player.current_jump > len(player.character.jump):
                    player.y -= 12.1
                player.current_jump += 12.0
            elif player.isDescending:
                if player.current_jump < len(player.character.jump) and \
                                   player.current_jump > len(player.character.jump)/1.7:
                    player.y += 10
                    player.x += 8
                elif player.current_jump < len(player.character.jump)/1.7 and \
                                    player.current_jump > len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y += 15
                    player.x += 6
                elif player.current_jump < len(player.character.jump)/4 and \
                                    player.current_jump > len(player.character.jump)/6:
                    player.y += 18
                    player.x += 4
                elif player.current_jump < len(player.character.jump)/6:
                    player.y += 22
                player.current_jump -= 12.0
        elif player.neutral_jumping:
            if player.isJumping:
                if player.current_jump < len(player.character.jump)/6:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump1.png'),
                                                   (130, 250)), True, False)
                    player.y -= 0
                elif player.current_jump > len(player.character.jump)/6 and \
                                    player.current_jump < len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump2.png'),
                                               (130, 250)), True, False)
                    player.y -= 12.2
                elif player.current_jump > len(player.character.jump)/4 and \
                                    player.current_jump < len(player.character.jump)/1.7:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y -= 17.1
                elif player.current_jump > len(player.character.jump)/1.7 and \
                                    player.current_jump < len(player.character.jump):
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump4.png'),
                                               (130, 250)), True, False)
                    player.y -= 15.3
                elif player.current_jump > len(player.character.jump):
                    player.y -= 12.1
                player.current_jump += 12.0
            elif player.isDescending:
                if player.current_jump < len(player.character.jump) and \
                                   player.current_jump > len(player.character.jump)/1.7:
                    player.y += 10
                elif player.current_jump < len(player.character.jump)/1.7 and \
                                    player.current_jump > len(player.character.jump)/4:
                    if player.multiplier == 1:
                        player.character.image = \
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'), (130, 250))
                    else:
                        player.character.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load('Sprites/Gina/GinaJump3.png'),
                                               (130, 250)), True, False)
                    player.y += 15
                elif player.current_jump < len(player.character.jump)/4 and \
                                    player.current_jump > len(player.character.jump)/6:
                    player.y += 18
                elif player.current_jump < len(player.character.jump)/6:
                    player.y += 22
                player.current_jump -= 12.0

        if player.current_jump >= len(player.character.jump) and player.isJumping:
            player.isJumping = False
            player.isDescending = True
        elif player.current_jump <= 0 and player.isDescending:
            player.isDescending = False
            player.neutral_jumping = False
            player.forward_jumping = False
            player.back_jumping = False
            player.setAction = False
            player.y = player.yOriginal
            player.current_jump = 0

    def forward_dash(self, player):
        collide_multiplier = 1
        if player.facingRight and not player.setAction:
            player.multiplier = 1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.multiplier = -1
            player.setAction = True

        if player.dash_collide is True:
            collide_multiplier = 0

        if player.currentDash < len(player.character.dash)/2:
            player.x += 6.7*player.multiplier*collide_multiplier
            player.y -= .53
        elif player.currentDash > len(player.character.dash)/2 and \
                                            player.currentDash < len(player.character.dash)/1.5:
            player.x += 5.75*player.multiplier
        elif player.currentDash > len(player.character.dash)/1.5:
            player.x += 5.175*player.multiplier*collide_multiplier
            player.y += 0.46
        player.currentDash += 6
        if player.currentDash >= len(player.character.dash):
            player.isDashing = False
            player.dash_collide = False
            player.setAction = False
            player.y = player.yOriginal
            player.currentDash = 0

        if player.index >= len(player.character.dash):
            player.index = 0
        else:
            if player.multiplier == 1:
                player.character.image = player.character.dash[player.index]
                player.index += 1
            else:
                player.character.image = \
                    pygame.transform.flip(player.character.dash[player.index], True, False)
                player.index += 1


    def back_dash(self, player, x):
        if player.facingRight and not player.setAction:
            player.multiplier = 1
            player.setAction = True
        elif not player.facingRight and not player.setAction:
            player.multiplier = -1
            player.setAction = True

        if player.currentDash < len(player.character.backdash)/2:
            player.x += 3.7*(-1)*player.multiplier
            player.y -= .56
        elif player.currentDash > len(player.character.backdash)/2 \
                                    and player.currentDash < len(player.character.backdash)/1.5:
            player.x += 3.35*(-1)*player.multiplier
        elif player.currentDash > len(player.character.backdash)/1.5:
            player.x += 3.175*(-1)*player.multiplier
            player.y += .48
        player.currentDash += 6
        if player.currentDash >= len(player.character.backdash):
            player.isBackDashing = False
            player.setAction = False
            player.y = player.yOriginal
            player.currentDash = 0

        if player.index >= len(player.character.backdash):
            player.index = 0
        else:
            if player.multiplier == 1:
                player.character.image = player.character.backdash[player.index]
                player.index += 1
            else:
                player.character.image = \
                    pygame.transform.flip(player.character.backdash[player.index], True, False)
                player.index += 1

    # -----------------------------------------------------------------------------------------------------------------

    def update(self, player, x):

        if player.block_hit:
            self.being_blocked(player)
        elif player.got_hit:
            self.being_damaged(player)
        elif player.got_air_hit:
            self.being_air_damaged(player)
        elif player.neutral_jumping or player.forward_jumping \
                or player.back_jumping or player.isDescending:
            self.jumping(player)
        elif player.getting_up:
            self.wake_up(player)
        elif player.isDashing:
            self.forward_dash(player)
        elif player.isBackDashing:
            self.back_dash(player, x)
        elif player.crouch_attack_a:
            self.crouch_a(player)
        elif player.attack_a:
            self.stand_a(player)
        elif player.crouch_attack_b:
            self.crouch_b(player)
        elif player.attack_b:
            self.stand_b(player)
        elif player.crouch_attack_c:
            self.crouch_c(player)
        elif player.attack_c:
            self.stand_c(player)
        elif x < 0:
            player.x += x
            if player.facingRight:
                if player.index >= len(player.character.walkBackward):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.walkBackward[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.walkBackward[player.index],True, False)
                        player.index += 1
            else:
                if player.index >= len(player.character.walkFoward):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.walkFoward[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.walkFoward[player.index], True, False)
                        player.index += 1
        elif x > 0:
            player.x += x
            if player.facingRight:
                if player.index >= len(player.character.walkFoward):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.walkFoward[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.walkFoward[player.index], True, False)
                        player.index += 1
            else:
                if player.index >= len(player.character.walkBackward):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.walkBackward[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.walkBackward[player.index], True, False)
                        player.index += 1
        elif x == 0:
            player.x += x
            if player.crouching != True:
                if player.index >= len(player.character.standing):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.standing[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.standing[player.index], True, False)
                        player.index += 1
            else:
                if player.index >= len(player.character.crouching):
                    player.index = 0
                else:
                    if player.facingRight:
                        player.character.image = player.character.crouching[player.index]
                        player.index += 1
                    else:
                        player.character.image = \
                            pygame.transform.flip(player.character.crouching[player.index], True, False)
                        player.index += 1