import pygame
from boxes import InvincibleBox
from boxes import DamageBox
from boxes import HurtBox
from boxes import HitBox
from boxes import GrabBox
from projectile import *

class Player:

    def __init__(self, main_character, player_number, x, y):
        """
        Initalizes all of a specific player's current statistics during battle. A player's health is checked here
        and their current action is being performed or not. It also checks for button buffers so that later actions
        can be checked afterwards.
        :param main_character:
        :param player_number:
        :param x:
        :param y:
        :return:
        """

        self.playerNumber = player_number
        self.character = main_character

        self.health_points = self.character.health
        self.max_health = self.character.health

        self.meter_points = self.character.meter/2
        self.max_meter = self.character.meter

        self.points = 0

        #Determines the starting facing position of each player.
        if player_number == 1:
            self.multiplier = 1
            self.facingRight = True
        else:
            self.multiplier = -1
            self.facingRight = False
        self.was_facing_right = True

        self.crouching = False
        #Booleans determine whether the player is blocking high or low
        self.blockingLow = False
        self.blockingHigh = False

        #Determines a button has been pressed and buffers it for future actions.
        self.upPressed = 0
        self.upCount = 0

        self.leftPressed = 0
        self.leftCount = 0

        self.rightPressed = 0
        self.rightCount = 0

        self.downPressed = 0
        self.downCount = 0

        #This checks for the overall action state of the player.
        self.setAction = False

        #Checks a player's current action that renders them unable to do anything else.
        self.isDashing = False
        self.isBackDashing = False
        self.isJumping = False
        self.neutral_jumping = False
        self.forward_jumping = False
        self.back_jumping = False
        self.isDescending = False

        #Checks for player to player movement collision.
        self.dash_collide = False
        self.jump_collide = False

        self.currentDash = 0
        self.current_jump = 0

        #Checks for player attack actions.
        self.reverse_correction = False

        self.hit_confirm = False
        self.hit_box_fill_once = False
        self.hit_box_fill_twice = False

        self.animation_fill_once = False

        self.grabbing = False
        self.grabbed = False
        self.throw = False
        self.timer = 2

        self.attack_a = False
        self.attack_b = False
        self.attack_c = False

        self.crouch_attack_a = False
        self.crouch_attack_b = False
        self.crouch_attack_c = False

        self.jump_attack_a = False
        self.jump_attack_b = False
        self.jump_attack_c = False
        self.air_attack_once = False

        self.special_one = False
        self.special_one_timer = 0

        #Checks for the values of hitstun duration and calculate the damage accordingly.
        self.got_hit = False
        self.got_air_hit = False

        self.getting_up = False
        self.block_hit = False
        self.push_back = False

        self.hitstun = 0
        self.max_hitstun = 0
        self.knockback = 0
        self.knockdown = False
        self.attack_level = 0

        # Used to tell what a character does when they win/lose/timeup
        self.winner = False
        self.finish_win_animation = False
        self.loser = False
        self.finish_lose_animation = False

        # Used to correct pixel animation placements if there are any inconsistencies.
        self.off_set = False
        self.off_set_value = 0

        self.x = x
        self.collision_x = 0
        self.collision_width = 0
        self.y = y
        self.collision_y = 0
        self.collision_height = 0

        self.yOriginal = y
        self.yKnockdown = y + 130
        self.index = 0

    def display_player(self, game_display, x, y):
        """
        Draws the player's character into the screen.
        :param game_display:
        :param x:
        :param y:
        :return:
        """

        game_display.blit(self.character.image, (x, y))

        for x in self.character.hit_box:
            x.draw_box(game_display)
        for x in self.character.hurt_box:
            x.draw_box(game_display)

    def display_effects(self, game_display):
        for effects in self.character.effects_animation:
            if effects.index >= len(effects.effects_animation) - 1:
                self.character.effects_animation.remove(effects)
            else:
                effects.draw_box(game_display)

    def neutral_position(self, other_player):
        """
        Checks to see if the player is not doing anything, then return them to their neutral standing position.
        :param other_player:
        :return:
        """
        if self.facingRight:
            self.character.image = self.character.neutralPosition
        else:
            pygame.transform.flip(self.character.neutralPosition, True, False)

    def check_facing(self, other_player):
        """
        Checks a player's facing position. If the player is to the left of the opponent, then face right, else left.
        :param other_player:
        :return:
        """
        if len(self.character.hurt_box) <= 0 or len(other_player.character.hurt_box) <= 0:
            can_check = False
        else:
            can_check = True

        if can_check:
            if self.collision_x < other_player.collision_x:
                self.facingRight = True
            else:
                self.facingRight = False

    def check_collision(self, two):
        """
        Checks the player-to-player collision of their hurt_boxes.
        :param two:
        :return:
        """

        for first in self.character.hurt_box:
            for second in two.character.hurt_box:
                a_hit = pygame.sprite.collide_rect(first, second)
                if a_hit:
                    collision_box_1 = isinstance(first, DamageBox) and isinstance(second, InvincibleBox)
                    collision_box_2 = isinstance(first, DamageBox) and isinstance(second, HurtBox)
                    collision_box_3 = isinstance(first, HurtBox) and isinstance(second, DamageBox)
                    collision_box_4 = isinstance(first, InvincibleBox) and isinstance(second, DamageBox)

                    if collision_box_1 or collision_box_2 or collision_box_3 or collision_box_4:
                        return False
                    else:
                        r_collide = first.rect.x + first.rect.width > second.rect.x + 10
                        l_collide = first.rect.x  < second.rect.x + second.rect.width - 10

                        if r_collide or l_collide:
                            return True
        return False

    def check_attack_collision(self, two):
        """
        Checks the player's attack to the other player's hurtbox to see if they connected or not.
        :param two:
        :return:
        """
        for first in self.character.hit_box:
            hit_box_temp = first

            for second in two.character.hurt_box:
                invincible = isinstance(second, InvincibleBox)
                grab_box = isinstance(first, GrabBox)

                a_hit = False
                if not invincible:
                    if not grab_box:
                        a_hit = pygame.sprite.collide_rect(first, second)

                if a_hit:
                    gina_fireball = isinstance(first, GinaFireBall)
                    if gina_fireball:
                        a_hit_2 = pygame.sprite.collide_rect(first.hit_box, second)

                        if a_hit_2:
                            hit_box_temp = first.hit_box
                            self.character.hit_box.remove(first)
                            return hit_box_temp
                    else:
                        self.character.hit_box.remove(first)
                        return hit_box_temp
        return None

    def check_grab_collision(self, two):
        """
        Checks the player's grab attack to the other player's hurtbox to see if they connected or not.
        :param two:
        :return:
        """
        for first in self.character.hit_box:
            grab_box = first

            for second in two.character.hurt_box:
                invincible = isinstance(second, InvincibleBox)
                not_grabbable = isinstance(second, DamageBox)
                hit_box = isinstance(first, HitBox)
                fire_ball = isinstance(first, GinaFireBall)
                a_grab = False

                if not invincible:
                    if not not_grabbable:
                        if not hit_box:
                            if not fire_ball:
                                a_grab = pygame.sprite.collide_rect(first, second)
                if a_grab:
                    self.character.hit_box.remove(grab_box)
                    return True

        return False

    def grab_timer(self):
        """
        This method counts down a timer to see if the other player can escape a grab or not.
        :return:
        """
        if self.timer > 0:
            self.timer -= 1 * 0.045
            return False
        else:
            return True

    def calculate_damage(self, two, attack):
        """
        When an attack connects, this method sends the information of the attack to the opposing player. The calculation
        done is determined by the type of attack versus the other player's block pattern.
        :param two:
        :param attack:
        :return:
        """

        if two.blockingHigh is True:
            if attack.blocktype == 'stand':
                two.health_points -= attack.damage * 0.1
                two.hitstun = attack.hitstun * 0.7
                two.max_hitstun = attack.hitstun * 0.8
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return False
            elif attack.blocktype == 'crouch':
                two.health_points -= attack.damage
                two.hitstun = attack.hitstun
                two.max_hitstun = attack.hitstun
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return True
            elif attack.blocktype == 'overhead':
                two.health_points -= attack.damage * 0.1
                two.hitstun = attack.hitstun * 0.7
                two.max_hitstun = attack.hitstun * 0.8
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return False
            elif attack.blocktype == 'sweep':
                two.health_points -= attack.damage
                two.hitstun = attack.hitstun
                two.max_hitstun = attack.hitstun
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                two.knockdown = True
                return True
        elif two.blockingLow is True:
            if attack.blocktype == 'stand':
                two.health_points -= attack.damage * 0.1
                two.hitstun = attack.hitstun * 0.7
                two.max_hitstun = attack.hitstun * 0.8
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return False
            elif attack.blocktype == 'crouch':
                two.health_points -= attack.damage * 0.1
                two.hitstun = attack.hitstun * 0.7
                two.max_hitstun = attack.hitstun * 0.8
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return False
            elif attack.blocktype == 'overhead':
                two.health_points -= attack.damage
                two.hitstun = attack.hitstun
                two.max_hitstun = attack.hitstun
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return True
            elif attack.blocktype == 'sweep':
                two.health_points -= attack.damage * 0.1
                two.hitstun = attack.hitstun * 0.7
                two.max_hitstun = attack.hitstun * 0.8
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                return False
        else:
            if attack.blocktype == 'sweep':
                two.health_points -= attack.damage
                two.hitstun = attack.hitstun
                two.max_hitstun = attack.hitstun
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                two.knockdown = True
                return True
            else:
                two.health_points -= attack.damage
                two.hitstun = attack.hitstun
                two.max_hitstun = attack.hitstun
                two.attack_level = attack.attack_level
                if self.facingRight and self.off_set:
                    two.knockback = -attack.knockback
                else:
                    two.knockback = attack.knockback
                two.knockdown = False
                return True

    def max_collision_right(self, two):
        """
        This method offsets the other player so that their sprites do not stack on top of each other.
        Applies the offset to the right.
        :param two:
        :return:
        """
        initial = True
        x = 0

        for first in self.character.hurt_box:
            r_collide = first.rect.x + first.rect.width
            if x < r_collide and initial is not True:
                x = r_collide
            elif initial is True:
                x = r_collide
                initial = False

        return x - self.character.x_offset

    def max_collision_left(self, two):
        """
        This method offsets the other player so that their sprites do not stack on top of each other.
        Applies the offset to the left.
        :param two:
        :return:
        """
        initial = True
        x = 0

        for first in self.character.hurt_box:
            l_collide = first.rect.x
            if x > l_collide and initial is not True:
                x = l_collide
            elif initial is True:
                x = l_collide
                initial = False

        return x + self.character.x_offset

    def fire_ball_collide(self, two):
        """
        Checks the collision of a projectile from one player to the other player. Checks the first player's projectile
        list in the character versus the other character's hurt box.
        :param two:
        :return:
        """
        for first in self.character.hit_box:
            for second in two.character.hit_box:
                ball_1 = isinstance(first, GinaFireBall)
                ball_2 = isinstance(second, GinaFireBall)

                a_hit = False
                if ball_1:
                    if ball_2:
                        a_hit = pygame.sprite.collide_rect(first, second)

                if a_hit:
                    self.character.hit_box.remove(first)
                    two.character.hit_box.remove(second)

    def button_update(self, direction):
        """
        This method checks the buffering of buttons, specifically if the player double taps a button. If the player
        pressed a button, then a couple of milliseconds will be counted until the buffer is reset. Useful for
        determining if a running or back-dashing actions.
        :param direction:
        :return:
        """
        if direction == 'left':
            if self.leftPressed > 0 and self.leftCount >= 1:
                return True
            else:
                self.leftPressed = 0.5
                self.leftCount += 1
                return False
        elif direction == 'right':
            if self.rightPressed > 0 and self.rightCount >= 1:
                return True
            else:
                self.rightPressed = 0.5
                self.rightCount += 1
                return False
        elif direction == 'down':
            if self.downPressed > 0 and self.downCount >= 1:
                return True
            else:
                self.downPressed = 0.5
                self.downCount += 1
                return False

    def button_buffer_decrease(self):
        """
        This method will be called to constantly lower the timer on the button buffer.
        :return:
        """
        if self.upPressed > 0:
            self.upPressed -= 1 * 0.045
        else:
            self.upPressed = 0
        if self.leftPressed > 0:
            self.leftPressed -= 1 * 0.045
        else:
            self.leftPressed = 0
        if self.rightPressed > 0:
            self.rightPressed -= 1 * 0.045
        else:
            self.rightPressed = 0
        if self.downPressed > 0:
            self.downPressed -= 1 * 0.045
        else:
            self.downPressed = 0

    def update(self, x, two):
        """
        This method will perform the specific actions of the player's character. The method will then jump to that
        character's specific update action as each one are suppose to play differently from each other.
        :param x:
        :return:
        """
        self.character.update_hurt_box(self)
        self.character.update(self, x, two)
