import pygame
import random
from pygame.locals import *
from Player import Player
from stage import Stage
from Gina import Gina
from Otis import Otis
from boxes import Boundaries
from health_system import HealthSystem
from health_system import MagicSystem

class FightScreen():

    def __init__(self, character_one, character_two):
        """
        Initializes the main variables for the fighting section.

        Holds the main information for player one and player two. The timer is set to 50 seconds. The game is won
        when one of the players win 2 rounds of a set.

        It also holds all the variables to handle transitions and music.
        :param character_one:
        :param character_two:
        :return:
        """

        self.character_one = character_one
        self.character_two = character_two
        self.stage = None

        self.timer = 5000
        self.round = 1

        self.player_one_wins = 0
        self.player_two_wins = 0

        self.index = 255
        self.screen_transition = True

        self.introduce_round = True
        self.round_start = False

        self.music_was_playing = False
        self.music_position = 0

        self.round_end_played = False
        self.who_won = False

    def reset_booleans(self):
        """
        Method is used to reset the booleans and statistics for the next round.
        :return:
        """

        self.timer = 5000

        self.index = 255
        self.screen_transition = True

        self.introduce_round = True
        self.round_start = False

        self.round_end_played = False
        self.who_won = False

    def retract_attack(self, player):
        """
        When a player is hit, the method is used to retract all previously presses actions so that once the damage
        animation is done, the pre-pressed ones aren't done right after.
        :param player:
        :return:
        """

        player.setAction = False
        player.attack_a = False
        player.crouch_attack_a = False
        player.attack_b = False
        player.crouch_attack_b = False
        player.attack_c = False
        player.crouch_attack_c = False

        player.special_one = False

        player.grabbing = False

        player.off_set = False
        player.off_set_value = 0
        player.hit_box_fill_once = False
        player.hit_box_fill_twice = False

        player.character.hit_box.clear()

    def check_bounds(self, player, LEFT_BOUND, RIGHT_BOUND):
        """
        Checks collision when either player one or player two hit the edge of the map or rather their borders.
        :param player:
        :param LEFT_BOUND:
        :param RIGHT_BOUND:
        :return:
        """

        check = None
        if player.collision_x <= LEFT_BOUND.x + LEFT_BOUND.width:
            player.x = LEFT_BOUND.x + LEFT_BOUND.width - (player.collision_x - player.x)
            check = 'left'

        if player.collision_x + player.collision_width >= RIGHT_BOUND.x:
            player.x = RIGHT_BOUND.x - player.character.rect.width + \
                        ((player.x + player.character.rect.width) - (player.collision_x + player.collision_width))
            check = 'right'

        # if player.x <= LEFT_BOUND.x + LEFT_BOUND.width:
        #     player.x = LEFT_BOUND.x + LEFT_BOUND.width
        #     check = 'left'
        #
        # if player.x + player.character.rect.width >= RIGHT_BOUND.x:
        #     player.x = RIGHT_BOUND.x - player.character.rect.width
        #     check = 'right'

        return check

    def attack_rebound(self, player, LEFT_BOUND, RIGHT_BOUND):
        """
        Works similar to check_bounds() bur returns a boolean with an offset of +/- 20. This is used when a player
        is cornered, the the following attacks from the opposing player pushes them back instead.
        :param player:
        :param LEFT_BOUND:
        :param RIGHT_BOUND:
        :return:
        """
        if player.collision_x <= LEFT_BOUND.x + LEFT_BOUND.width + 20:
            return True

        if player.collision_x + player.collision_width >= RIGHT_BOUND.x - 20:
            return True

    def message_display(self, str, game_display, x, y, color):
        """
        Displays a simple message. However, this method allows the changing of color font.
        :param str:
        :param game_display:
        :param x:
        :param y:
        :param color:
        :return:
        """
        text = pygame.font.Font('Fonts/year_is_199x.ttf', 100)
        textSurface = text.render(str, True, color)

        game_display.blit(textSurface, (x, y))

    def round_over(self, message, game_display, fpsClock, x_position, y_position):
        """
        This method is used to transition between rounds so that the statistics can update and reset.
        :param message:
        :param game_display:
        :param fpsClock:
        :param x_position:
        :param y_position:
        :return:
        """

        transition = pygame.Surface((800, 100))
        for x in range(0, 180):
            transition.fill((0, 0, 0))
            transition.set_alpha(x)
            game_display.blit(transition, (x_position, y_position))

            if x > 100:
                if message == 'KO':
                    self.message_display(message, game_display, 350, 400, (255, 255, 255))
                else:
                    self.message_display(message, game_display, 300, 400, (255, 255, 255))

            pygame.display.flip()
            fpsClock.tick(120)

    def fight_loop(self):
        """
        Main game loop for the actual fighting of two players. The bulk of the calculation and and collision detections
        are done here. It checks for player-to-player collision, attack collision, wall collision and victory checks.
        :return:
        """
        pygame.init()
        gameExit = False
        display_width = 800
        display_height = 600
        game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Conflict Resolution')

        LEFT_BOUND = Boundaries(-200, 0, 100, 600)
        RIGHT_BOUND = Boundaries(900, 0, 100, 600)

        playerOne = Player(self.character_one, 1, display_width/2 - 250, display_height/2.3)
        playerTwo = Player(self.character_two, 2, display_width/2 + 120, display_height/2.3)
        health_bar = HealthSystem(playerOne, playerTwo)
        magic_bar = MagicSystem(playerOne, playerTwo)

        pygame.mixer.music.set_endevent(USEREVENT)

        x1_change = 0
        x2_change = 0
        fpsClock = pygame.time.Clock()

        stage_x = -100
        stage_y = 0

        while gameExit != True:

            # ---------------------------------------------------------------------------------------------------------

            #gameDisplay.fill((255, 255, 255))
            game_display.blit(self.stage.bg, (stage_x, stage_y))
            health_bar.show_bar(game_display, playerOne, playerTwo)
            magic_bar.show_bar(game_display, playerOne, playerTwo)

            if playerOne.meter_points >= 100:
                playerOne.meter_points = 100
            if playerTwo.meter_points >= 100:
                playerTwo.meter_points = 100

            playerOne.update(x1_change, playerTwo)
            playerTwo.update(x2_change, playerOne)
            playerOne.display_player(game_display, playerOne.x, playerOne.y)
            playerTwo.display_player(game_display, playerTwo.x, playerTwo.y)
            playerOne.display_effects(game_display)
            playerTwo.display_effects(game_display)

            LEFT_BOUND.draw_bounds(game_display)
            RIGHT_BOUND.draw_bounds(game_display)

            # ---------------------------------------------------------------------------------------------------------

            if self.index <= 0:
                self.screen_transition = False

            if self.screen_transition:
                transition = pygame.Surface((800, 600))
                transition.fill((0, 0, 0))
                transition.set_alpha(self.index)
                game_display.blit(transition, (0, 0))
                self.index -= 3

            if self.screen_transition is False and self.introduce_round:
                transparency = self.index
                if self.index >= 150:
                    transparency = 150

                border_top = pygame.Surface((800, 200))
                border_top.fill((0, 0, 0))
                border_bottom = pygame.Surface((800, 200))
                border_bottom.fill((0, 0, 0))

                border_top.set_alpha(transparency)
                border_bottom.set_alpha(transparency)
                game_display.blit(border_top, (0, 0))
                game_display.blit(border_bottom, (0, 400))
                self.index += 1

                if self.index == 100 and self.music_was_playing is False:
                    if self.music_position != 0:
                        pygame.mixer.music.set_pos(self.music_position)
                    pygame.mixer.music.play()
                    self.music_was_playing = True
                if self.index >= 100:
                    self.message_display('ROUND '+ str(self.round), game_display, 100, 100, (255, 255, 255))
                if self.index >= 200:
                    self.message_display('FIGHT!' , game_display, 500, 400, (255, 255, 255))

            if self.index == 256:
                self.introduce_round = False
                self.index = 255

            # ---------------------------------------------------------------------------------------------------------

            #print("P1 Blocking low? ", playerOne.blockingLow)
            #print("P1 Blocking high? ", playerOne.blockingHigh)
            if self.screen_transition is False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == USEREVENT:
                        pygame.mixer.music.play()

                    keys = pygame.key.get_pressed()

                    if self.introduce_round is False:
                        if keys[pygame.K_KP6]:
                            if not playerTwo.setAction:
                                playerTwo.grabbing = True
                        elif keys[pygame.K_KP7]:
                            if not playerTwo.attack_b and not playerTwo.attack_c and not playerTwo.grabbing:
                                if playerTwo.crouching is True:
                                    if not playerTwo.setAction:
                                        playerTwo.crouch_attack_a = True
                                else:
                                    if not playerTwo.setAction:
                                        playerTwo.attack_a = True
                                    elif playerTwo.isJumping or playerTwo.isDescending:
                                        if not playerTwo.jump_attack_b and not playerTwo.jump_attack_c:
                                            playerTwo.jump_attack_a = True
                        elif keys[pygame.K_KP8]:
                            if not playerTwo.attack_a and not playerTwo.attack_c and not playerTwo.grabbing:
                                if playerTwo.crouching is True:
                                    if not playerTwo.setAction:
                                        playerTwo.crouch_attack_b = True
                                else:
                                    if not playerTwo.setAction:
                                        playerTwo.attack_b = True
                                    elif playerTwo.isJumping or playerTwo.isDescending:
                                        if not playerTwo.jump_attack_a and not playerTwo.jump_attack_c:
                                            playerTwo.jump_attack_b = True
                        elif keys[pygame.K_KP9]:
                            if not playerTwo.attack_a and not playerTwo.attack_b and not playerTwo.grabbing:
                                if playerTwo.crouching is True:
                                    if not playerTwo.setAction:
                                        playerTwo.crouch_attack_c = True
                                else:
                                    if not playerTwo.setAction:
                                        playerTwo.attack_c = True
                                    elif playerTwo.isJumping or playerTwo.isDescending:
                                        if not playerTwo.jump_attack_a and not playerTwo.jump_attack_b:
                                            playerTwo.jump_attack_c = True
                        elif keys[pygame.K_KP4]:
                            if not playerTwo.attack_a and not playerTwo.attack_b \
                                and not playerTwo.attack_c and not playerTwo.grabbing and not playerTwo.setAction:
                                if not playerTwo.isJumping and not playerTwo.isDescending:
                                    playerTwo.special_one = True
                            else:
                                pass
                    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                        if not playerTwo.forward_jumping and not playerTwo.neutral_jumping and not playerTwo.setAction:
                            playerTwo.isJumping = True
                            playerTwo.back_jumping = True
                    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                        if not playerTwo.back_jumping and not playerTwo.neutral_jumping and not playerTwo.setAction:
                            playerTwo.isJumping = True
                            playerTwo.forward_jumping = True
                    elif keys[pygame.K_UP]:
                        if not playerTwo.forward_jumping and not playerTwo.back_jumping and not playerTwo.setAction:
                            playerTwo.isJumping = True
                            playerTwo.neutral_jumping = True
                    elif keys[pygame.K_LEFT]:
                        if keys[pygame.K_DOWN]:
                            playerTwo.crouching = True
                            if playerTwo.facingRight:
                                if not playerTwo.isJumping and not playerTwo.isDescending:
                                    playerTwo.blockingLow = True
                                x2_change = 0
                            else:
                                x2_change = 0
                        else:
                            if playerTwo.facingRight:
                                if not playerTwo.isJumping and not playerTwo.isDescending:
                                    playerTwo.blockingHigh = True
                                x2_change = -2.5
                            else:
                                x2_change = -2.5
                    elif keys[pygame.K_RIGHT]:
                        if keys[pygame.K_DOWN]:
                            playerTwo.crouching = True
                            if playerTwo.facingRight:
                                x2_change = 0
                            else:
                                if not playerTwo.isJumping and not playerTwo.isDescending:
                                    playerTwo.blockingLow = True
                                x2_change = 0
                        else:
                            if playerTwo.facingRight:
                                x2_change = 2.5
                            else:
                                if not playerTwo.isJumping and not playerTwo.isDescending:
                                    playerTwo.blockingHigh = True
                                x2_change = 2.5
                    elif keys[pygame.K_DOWN]:
                        playerTwo.crouching = True
                        x2_change = 0

                    if self.introduce_round is False:
                        if keys[pygame.K_l]:
                            if not playerOne.setAction and not playerOne.isJumping and not playerOne.isDescending:
                                playerOne.grabbing = True
                        elif keys[pygame.K_u]:
                            if not playerOne.attack_b and not playerOne.attack_c and not playerOne.grabbing:
                                if playerOne.crouching is True:
                                    if not playerOne.setAction:
                                        playerOne.crouch_attack_a = True
                                else:
                                    if not playerOne.setAction:
                                        playerOne.attack_a = True
                                    elif playerOne.isJumping or playerOne.isDescending:
                                        if not playerOne.jump_attack_b and not playerOne.jump_attack_c:
                                            playerOne.jump_attack_a = True
                        elif keys[pygame.K_i]:
                            if not playerOne.attack_a and not playerOne.attack_c and not playerOne.grabbing:
                                if playerOne.crouching is True:
                                    if not playerOne.setAction:
                                        playerOne.crouch_attack_b = True
                                else:
                                    if not playerOne.setAction:
                                        playerOne.attack_b = True
                                    elif playerOne.isJumping or playerOne.isDescending:
                                        if not playerOne.jump_attack_a and not playerOne.jump_attack_c:
                                            playerOne.jump_attack_b = True
                        elif keys[pygame.K_o]:
                            if not playerOne.attack_a and not playerOne.attack_b and not playerOne.grabbing:
                                if playerOne.crouching is True:
                                    if not playerOne.setAction:
                                        playerOne.crouch_attack_c = True
                                else:
                                    if not playerOne.setAction:
                                        playerOne.attack_c = True
                                    elif playerOne.isJumping or playerOne.isDescending:
                                        if not playerOne.jump_attack_a and not playerOne.jump_attack_b:
                                            playerOne.jump_attack_c = True
                        elif keys[pygame.K_j]:
                            if not playerOne.attack_a and not playerOne.attack_b \
                                and not playerOne.attack_c and not playerOne.grabbing and not playerOne.setAction:
                                if not playerOne.isJumping and not playerOne.isDescending:
                                    playerOne.special_one = True
                            else:
                                pass
                    if keys[pygame.K_w] and keys[pygame.K_a]:
                        if not playerOne.forward_jumping and not playerOne.neutral_jumping and not playerOne.setAction:
                            playerOne.isJumping = True
                            playerOne.back_jumping = True
                    elif keys[pygame.K_w] and keys[pygame.K_d]:
                        if not playerOne.back_jumping and not playerOne.neutral_jumping and not playerOne.setAction:
                            playerOne.isJumping = True
                            playerOne.forward_jumping = True
                    elif keys[pygame.K_w]:
                        if not playerOne.forward_jumping and not playerOne.back_jumping and not playerOne.setAction:
                            playerOne.isJumping = True
                            playerOne.neutral_jumping = True
                    elif keys[pygame.K_a]:
                        if keys[pygame.K_s]:
                            playerOne.crouching = True
                            if playerOne.facingRight:
                                if not playerOne.isJumping and not playerOne.isDescending:
                                    playerOne.blockingLow = True
                                x1_change = 0
                            else:
                                x1_change = 0
                        else:
                            if playerOne.facingRight:
                                if not playerOne.isJumping and not playerOne.isDescending:
                                    playerOne.blockingHigh = True
                                x1_change = -2.5
                            else:
                                x1_change = -2.5
                    elif keys[pygame.K_d]:
                        if keys[pygame.K_s]:
                            playerOne.crouching = True
                            if playerOne.facingRight:
                                x1_change = 0
                            else:
                                if not playerOne.isJumping and not playerOne.isDescending:
                                    playerOne.blockingLow = True
                                x1_change = 0
                        else:
                            if playerOne.facingRight:
                                x1_change = 2.5
                            else:
                                if not playerOne.isJumping and not playerOne.isDescending:
                                    playerOne.blockingHigh = True
                                x1_change = 2.5
                    elif keys[pygame.K_s]:
                        playerOne.crouching = True
                        x1_change = 0

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_s:
                            playerOne.crouching = False
                            playerOne.blockingLow = False
                        if event.key == pygame.K_DOWN:
                            playerTwo.crouching = False
                            playerTwo.blockingLow = False
                        if event.key == pygame.K_a:
                            if playerOne.button_update('left') and playerOne.facingRight and playerOne.setAction is False:
                                playerOne.isBackDashing = True
                            elif playerOne.button_update('right') and not playerOne.facingRight and playerOne.setAction is False:
                                playerOne.isDashing = True
                            if playerOne.facingRight:
                                playerOne.blockingHigh = False
                                x1_change = 0
                            else:
                                x1_change = 0
                        if event.key == pygame.K_d:
                            if playerOne.button_update('right') and playerOne.facingRight and playerOne.setAction is False:
                                playerOne.isDashing = True
                            elif playerOne.button_update('left') and not playerOne.facingRight and playerOne.setAction is False:
                                playerOne.isBackDashing = True
                            if playerOne.facingRight is not True:
                                playerOne.blockingHigh = False
                                x1_change = 0
                            else:
                                x1_change = 0
                        if event.key == pygame.K_LEFT:
                            if playerTwo.button_update('left') and playerTwo.facingRight and playerTwo.setAction is False:
                                playerTwo.isBackDashing = True
                            elif playerTwo.button_update('right') and not playerTwo.facingRight and playerTwo.setAction is False:
                                playerTwo.isDashing = True
                            if playerTwo.facingRight:
                                playerTwo.blockingHigh = False
                                x2_change = 0
                            else:
                                x2_change = 0
                        if event.key == pygame.K_RIGHT:
                            if playerTwo.button_update('right') and playerTwo.facingRight and playerTwo.setAction is False:
                                playerTwo.isDashing = True
                            elif playerTwo.button_update('left') and not playerTwo.facingRight and playerTwo.setAction is False:
                                playerTwo.isBackDashing = True
                            if playerTwo.facingRight is not True:
                                playerTwo.blockingHigh = False
                                x2_change = 0
                            else:
                                x2_change = 0

                playerOne.check_facing(playerTwo)
                playerOne.button_buffer_decrease()

                playerTwo.check_facing(playerOne)
                playerTwo.button_buffer_decrease()

                player_one_hit_wall = self.check_bounds(playerOne, LEFT_BOUND, RIGHT_BOUND)
                player_two_hit_wall = self.check_bounds(playerTwo, LEFT_BOUND, RIGHT_BOUND)

                # Checks to see for hit collision between the two players...
                playerOne.fire_ball_collide(playerTwo)

                player_one_attack = playerOne.check_attack_collision(playerTwo)
                player_two_attack = playerTwo.check_attack_collision(playerOne)
                if player_one_attack is not None:
                    confirm = playerOne.calculate_damage(playerTwo, player_one_attack)
                    if confirm:
                        self.retract_attack(playerTwo)
                        if playerTwo.isJumping or playerTwo.isDescending:
                            playerOne.meter_points += 3
                            playerTwo.got_air_hit = True
                        else:
                            if self.attack_rebound(playerTwo, LEFT_BOUND, RIGHT_BOUND):
                                if playerOne.facingRight is True:
                                    playerOne.x -= playerTwo.knockback * 5
                                else:
                                    playerOne.x += playerTwo.knockback * 5
                            playerOne.meter_points += 3
                            playerTwo.got_hit = True
                    else:
                        self.retract_attack(playerTwo)
                        if self.attack_rebound(playerTwo, LEFT_BOUND, RIGHT_BOUND):
                            if playerOne.facingRight:
                                playerOne.x -= playerTwo.knockback * 5
                            else:
                                playerOne.x += playerTwo.knockback * 5
                        playerOne.meter_points += 1
                        playerTwo.block_hit = True
                    playerOne.hit_confirm = True
                if player_two_attack is not None:
                    confirm = playerTwo.calculate_damage(playerOne, player_two_attack)
                    if confirm:
                        self.retract_attack(playerOne)
                        if playerOne.isJumping or playerOne.isDescending:
                            playerTwo.meter_points += 3
                            playerOne.got_air_hit = True
                        else:
                            if self.attack_rebound(playerOne, LEFT_BOUND, RIGHT_BOUND):
                                if playerTwo.facingRight:
                                    playerTwo.x -= playerOne.knockback * 5
                                else:
                                    playerTwo.x += playerOne.knockback * 5
                            playerTwo.meter_points += 3
                            playerOne.got_hit = True
                    else:
                        self.retract_attack(playerOne)
                        if self.attack_rebound(playerOne, LEFT_BOUND, RIGHT_BOUND):
                            if playerTwo.facingRight:
                                playerTwo.x += playerOne.knockback * 5
                            else:
                                playerTwo.x -= playerOne.knockback * 5
                        playerTwo.meter_points += 1
                        playerOne.block_hit = True
                    playerTwo.hit_confirm = True

                if playerOne.check_grab_collision(playerTwo) and not playerTwo.isJumping and not playerTwo.isDescending:

                    while playerTwo.grab_timer() is False:
                        if playerTwo.grabbing is True:
                            playerOne.grabbing = False
                            playerTwo.grabbing = False

                            playerOne.push_back = True
                            playerTwo.push_back = True

                            playerOne.timer = 2
                            playerTwo.timer = 2

                            break

                    if playerTwo.timer <= 0:
                        playerTwo.setAction = False
                        playerOne.grabbing = False

                        playerOne.throw = True
                        playerTwo.grabbed = True

                if playerTwo.check_grab_collision(playerOne) and not playerOne.isJumping and not playerOne.isDescending:
                    while playerOne.grab_timer() is False:
                        if playerOne.grabbing is True:
                            playerTwo.grabbing = False
                            playerOne.grabbing = False

                            playerTwo.push_back = True
                            playerOne.push_back = True

                            playerOne.timer = 2
                            playerTwo.timer = 2

                            break

                    if playerOne.timer <= 0:
                        playerOne.setAction = False
                        playerTwo.grabbing = False

                        playerTwo.throw = True
                        playerOne.grabbed = True

            # --------------------------------------------------------------------------------------------------------

                # Checks wall collision for both player one and two.
                if playerOne.collision_x <= 0:
                    if playerTwo.collision_x + playerTwo.collision_width < 800:
                        diff = 0 - playerOne.collision_x
                        playerOne.x = 0 - (playerOne.collision_x - playerOne.x)

                        if player_one_hit_wall != 'left':
                            playerTwo.x += diff
                            LEFT_BOUND.move_wall(diff)
                            RIGHT_BOUND.move_wall(diff)
                            stage_x += diff
                    else:
                        playerOne.x = 0 - (playerOne.collision_x + playerOne.x)

                if playerOne.collision_x + playerOne.collision_width > 800:
                    if playerTwo.collision_x > 0:
                        diff = (playerOne.collision_x + playerOne.collision_width) - 800
                        playerOne.x = 800 - playerOne.character.rect.width + \
                            ((playerOne.x + playerOne.character.rect.width) - (playerOne.collision_x + playerOne.collision_width))

                        if player_one_hit_wall != 'right':
                            playerTwo.x -= diff
                            RIGHT_BOUND.move_wall(-diff)
                            LEFT_BOUND.move_wall(-diff)
                            stage_x -= diff
                    else:
                        playerOne.x = 800 - playerOne.character.rect.width + \
                            ((playerOne.x + playerOne.character.rect.width) - (playerOne.collision_x + playerOne.collision_width))

                if playerTwo.collision_x <= 0:
                    if playerOne.collision_x + playerOne.collision_width < 800:
                        diff = 0 - playerTwo.collision_x
                        playerTwo.x = 0 - (playerTwo.collision_x - playerTwo.x)

                        if player_two_hit_wall != 'left':
                            playerOne.x += diff
                            LEFT_BOUND.move_wall(diff)
                            RIGHT_BOUND.move_wall(diff)
                            stage_x += diff
                    else:
                        playerTwo.x = 0 - (playerTwo.collision_x + playerTwo.x)

                if playerTwo.collision_x + playerTwo.collision_width > 800:
                    if playerOne.x > 0:
                        diff = (playerTwo.collision_x + playerTwo.collision_width) - 800
                        playerTwo.x = 800 - playerTwo.character.rect.width + \
                            ((playerTwo.x + playerTwo.character.rect.width) - (playerTwo.collision_x + playerTwo.collision_width))

                        if player_two_hit_wall != 'right':
                            playerOne.x -= diff
                            RIGHT_BOUND.move_wall(-diff)
                            LEFT_BOUND.move_wall(-diff)
                            stage_x -= diff
                    else:
                        playerTwo.x = 800 - playerTwo.character.rect.width + \
                            ((playerTwo.x + playerTwo.character.rect.width) - (playerTwo.collision_x + playerTwo.collision_width))

                # Checks for player_1 hurt_box to player_2 hurt_box collision so that both of them do not overlap.
                if playerOne.check_collision(playerTwo) or playerTwo.check_collision(playerOne):
                    if playerOne.facingRight:
                        if x1_change > 0:
                            if x2_change < 0:
                                x1_change = 0
                                x2_change = 0
                            elif x2_change > 0:
                                if player_two_hit_wall == 'right':
                                    playerOne.x = playerTwo.x - playerOne.character.rect.width
                                elif player_two_hit_wall == 'left':
                                    playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                else:
                                    playerTwo.x = playerTwo.x + x1_change
                            elif x2_change == 0:
                                if player_two_hit_wall == 'right':
                                    playerOne.x = playerTwo.x - playerOne.character.rect.width
                                elif player_two_hit_wall == 'left':
                                    playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                else:
                                    playerTwo.x = playerTwo.x + x1_change

                        if x2_change < 0:
                            if x1_change > 0:
                                x2_change = 0
                                x1_change = 0
                            elif x1_change < 0:
                                if player_one_hit_wall == 'right':
                                    playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                elif player_one_hit_wall == 'left':
                                    playerTwo.x = playerOne.x + playerOne.character.rect.width
                                else:
                                    playerOne.x = playerOne.x + x2_change
                            elif x1_change == 0:
                                if player_one_hit_wall == 'right':
                                    playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                elif player_one_hit_wall == 'left':
                                    playerTwo.x = playerOne.x + playerOne.character.rect.width
                                else:
                                    playerOne.x = playerOne.x + x2_change

                        if playerOne.crouching:
                            x2_change = 0

                        if playerOne.setAction:
                            if playerOne.isDashing:
                                if playerTwo.isDashing:
                                    playerOne.dash_collide = True
                                    playerTwo.dash_collide = True
                                else:
                                    if player_two_hit_wall == 'right':
                                        playerOne.x = playerTwo.x - playerOne.character.rect.width
                                    elif player_two_hit_wall == 'left':
                                        playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                    else:
                                        playerTwo.x = playerOne.max_collision_right(playerTwo) - 30
                            elif playerOne.isDescending:
                                playerTwo.x = playerOne.max_collision_right(playerTwo)

                        if playerTwo.setAction:
                            if playerTwo.isDashing:
                                if playerOne.isDashing:
                                    playerOne.dash_collide = True
                                    playerTwo.dash_collide = True
                                else:
                                    if player_one_hit_wall == 'right':
                                        playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                    elif player_one_hit_wall == 'left':
                                        playerTwo.x = playerOne.x + playerOne.character.rect.width
                                    else:
                                        playerOne.x = playerTwo.max_collision_left(playerOne) - 120
                            elif playerTwo.isDescending:
                                playerOne.x = playerTwo.max_collision_left(playerOne) - 120
                    else:
                        if x1_change < 0:
                            if x2_change > 0:
                                x1_change = 0
                                x2_change = 0
                            elif x2_change < 0:
                                if player_two_hit_wall == 'right':
                                    playerOne.x = playerTwo.x - playerOne.character.rect.width
                                elif player_two_hit_wall == 'left':
                                    playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                else:
                                    playerTwo.x = playerTwo.x + x1_change
                            elif x2_change == 0:
                                if player_two_hit_wall == 'right':
                                    if playerOne.isDescending:
                                        playerOne.x = playerTwo.max_collision_left(playerOne)
                                    else:
                                        playerOne.x = playerTwo.x - playerOne.character.rect.width
                                elif player_two_hit_wall == 'left':
                                    if playerOne.isDescending:
                                        playerOne.x = playerTwo.max_collision_right(playerOne)
                                    else:
                                        playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                else:
                                    playerTwo.x = playerTwo.x + x1_change

                        if x2_change > 0:
                            if x1_change < 0:
                                x2_change = 0
                                x1_change = 0
                            elif x1_change > 0:
                                if player_one_hit_wall == 'right':
                                    playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                elif player_one_hit_wall == 'left':
                                    playerTwo.x = playerOne.x + playerOne.character.rect.width
                                else:
                                    playerOne.x = playerOne.x + x2_change
                            elif x1_change == 0:
                                if player_one_hit_wall == 'right':
                                    if playerTwo.isDescending:
                                        playerTwo.x = playerOne.max_collision_left(playerTwo)
                                    else:
                                        playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                elif player_one_hit_wall == 'left':
                                    if playerTwo.isDescending:
                                        playerTwo.x = playerOne.max_collision_right(playerTwo)
                                    else:
                                        playerTwo.x = playerOne.x + playerOne.character.rect.width
                                else:
                                    playerOne.x = playerOne.x + x2_change

                        if playerOne.crouching:
                            x2_change = 0

                        if playerOne.setAction:
                            if playerOne.isDashing:
                                if playerTwo.isDashing:
                                    playerOne.dash_collide = True
                                    playerTwo.dash_collide = True
                                else:
                                    if player_two_hit_wall == 'right':
                                        if playerOne.isDescending:
                                            playerOne.x = playerTwo.max_collision_left(playerOne)
                                        else:
                                            playerOne.x = playerTwo.x - playerOne.character.rect.width
                                    elif player_two_hit_wall == 'left':
                                        if playerOne.isDescending:
                                            playerOne.x = playerTwo.max_collision_right(playerOne)
                                        else:
                                            playerOne.x = playerTwo.x + playerTwo.character.rect.width
                                    else:
                                        playerTwo.x = playerOne.max_collision_left(playerTwo) - 120
                            elif playerOne.isDescending:
                                playerTwo.x = playerOne.max_collision_left(playerTwo) - 120
                        if playerTwo.setAction:
                            if playerTwo.isDashing:
                                if playerOne.isDashing:
                                    playerOne.dash_collide = True
                                    playerTwo.dash_collide = True
                                else:
                                    if player_one_hit_wall == 'right':
                                        if playerTwo.isDescending:
                                            playerTwo.x = playerOne.max_collision_left(playerTwo)
                                        else:
                                            playerTwo.x = playerOne.x - playerTwo.character.rect.width
                                    elif player_one_hit_wall == 'left':
                                        if playerTwo.isDescending:
                                            playerTwo.x = playerOne.max_collision_right(playerTwo)
                                        else:
                                            playerTwo.x = playerOne.x + playerOne.character.rect.width
                                    else:
                                        playerOne.x = playerTwo.max_collision_right(playerOne) - 30
                            elif playerTwo.isDescending:
                                playerOne.x = playerTwo.max_collision_right(playerOne)

            # --------------------------------------------------------------------------------------------------------

            if self.screen_transition is False and self.introduce_round is False:
                self.message_display(str(int(self.timer/100)), game_display, 380, 0, (0, 0, 0))
                if self.timer > 0:
                    self.timer -= 1
                else:
                    self.timer = 0

            if (playerOne.finish_win_animation and playerTwo.finish_lose_animation):
                self.transitionIn(game_display, fpsClock)
                self.music_position = pygame.mixer.music.get_pos()
                return 1
            elif (playerOne.finish_lose_animation and playerTwo.finish_win_animation):
                self.transitionIn(game_display, fpsClock)
                self.music_position = pygame.mixer.music.get_pos()
                return 2

            fpsClock.tick(60)
            pygame.display.flip()

            # --------------------------------------------------------------------------------------------------------
            if playerOne.health_points <= 0 and self.round_end_played is False:
                playerOne.setAction = False
                playerOne.loser = True
                if self.round_end_played is False:
                    self.round_over('KO', game_display, fpsClock, 0, 380)
                    self.round_end_played = True
            elif playerTwo.health_points <= 0 and self.round_end_played is False:
                playerOne.setAction = False
                playerTwo.loser = True
                if self.round_end_played is False:
                    self.round_over('KO', game_display, fpsClock, 0, 380)
                    self.round_end_played = True

            if self.timer <= 0:
                if playerOne.health_points > playerTwo.health_points:

                    playerTwo.loser = True
                    if self.round_end_played is False:
                        self.round_over('TIME OUT', game_display, fpsClock, 0, 380)
                        self.round_end_played = True
                elif playerTwo.health_points > playerOne.health_points:

                    playerOne.loser = True
                    if self.round_end_played is False:
                        self.round_over('TIME OUT', game_display, fpsClock, 0, 380)
                        self.round_end_played = True

            if playerOne.winner and self.who_won is False:
                self.round_over('PLAYER 1 WINS', game_display, fpsClock, 0, 380)
                self.who_won = True
            elif playerTwo.winner and self.who_won is False:
                self.round_over('PLAYER 2 WINS', game_display, fpsClock, 0, 380)
                self.who_won = True

    def transitionIn(self, screen, clock):
        """
        This method darkens the screen using pygame.surface and gradually increases the alpha levels for a
        smoother transition between menus.
        :param screen:
        :param clock:
        :return:
        """
        transition = pygame.Surface((800, 600))
        for x in range(0, 256, 10):
            transition.fill((0, 0, 0))
            transition.set_alpha(x)
            screen.blit(transition, (0, 0))
            pygame.display.flip()
            clock.tick(120)

    def game_condition(self):
        """
        The other main loop of the game. When the fight_loop is complete, this loop checks to see if one the players
        have achieved 2 points.
        :return:
        """
        random.seed()
        selection = random.randint(0, 2)

        if selection == 0:
            stage = 'Sprites/Stages/TrainingRoom.png'
            music = 'Sprites/sfx/bgm/bgmme37.ogg'
        else:
            stage = 'Sprites/Stages/sidewalks.png'
            music = 'Sprites/sfx/bgm/bgmme42.ogg'

        self.stage = Stage(stage, music)

        while self.player_one_wins < 2 and self.player_two_wins < 2:
            player_won = self.fight_loop()

            if player_won == 1:
                self.player_one_wins += 1
            else:
                self.player_two_wins += 1
            self.round += 1
            #print('player_one: ', self.player_one_wins, 'player_two: ', self.player_two_wins)

            self.reset_booleans()

        pygame.mixer.music.fadeout(2000)
        pygame.time.wait(2000)