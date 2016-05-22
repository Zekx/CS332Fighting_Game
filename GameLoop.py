import pygame

from Player import Player
from Gina import Gina
from Otis import Otis
from health_system import HealthSystem
from boxes import Boundaries

LEFT_BOUND = Boundaries(-200, 0, 100, 600)
RIGHT_BOUND = Boundaries(900, 0, 100, 600)

def retract_attack(player):
    player.setAction = False
    player.attack_a = False
    player.crouch_attack_a = False
    player.attack_b = False
    player.crouch_attack_b = False
    player.attack_c = False
    player.crouch_attack_c = False

    player.off_set = False
    player.off_set_value = 0
    player.hit_box_fill_once = False
    player.hit_box_fill_twice = False

    player.character.hit_box.clear()

def check_bounds(player):
    check = None

    if player.x <= LEFT_BOUND.x + LEFT_BOUND.width:
        print('left')
        player.x = LEFT_BOUND.x + LEFT_BOUND.width
        check = 'left'

    if player.x + player.character.rect.width >= RIGHT_BOUND.x:
        print('right')
        player.x = RIGHT_BOUND.x - player.character.rect.width
        check = 'right'

    return check


def game_loop():
    """
    Main game loop for the actual fighting of two players. Currently the game can read player one movement inputs
    and draws both players. However, the second player inputs and attack inputs are not currently working.
    :return:
    """
    pygame.init()
    gameExit = False
    display_width = 800
    display_height = 600
    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Conflict Resolution')

    playerOne = Player(Gina(), 1, display_width/2 - 250, display_height/2.3)
    playerTwo = Player(Gina(), 2, display_width/2 + 120, display_height/2.3)
    health_bar = HealthSystem(playerOne, playerTwo)

    stage = pygame.image.load('Sprites/Stages/TrainingRoom.png')

    x1_change = 0
    x2_change = 0
    fpsClock = pygame.time.Clock()

    stage_x = -100
    stage_y = 0

    while gameExit != True:
        #gameDisplay.fill((255, 255, 255))
        game_display.blit(stage, (stage_x, stage_y))
        health_bar.show_bar(game_display, playerOne, playerTwo)

        playerOne.update(x1_change)
        playerTwo.update(x2_change)
        playerOne.display_player(game_display, playerOne.x, playerOne.y)
        playerTwo.display_player(game_display, playerTwo.x, playerTwo.y)

        LEFT_BOUND.draw_bounds(game_display)
        RIGHT_BOUND.draw_bounds(game_display)

        #print("P1 Blocking low? ", playerOne.blockingLow)
        #print("P1 Blocking high? ", playerOne.blockingHigh)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_KP7]:
                if not playerTwo.attack_b and not playerTwo.attack_c:
                    if playerTwo.crouching is True:
                        if not playerTwo.setAction:
                            playerTwo.crouch_attack_a = True
                    else:
                        if not playerTwo.setAction:
                            playerTwo.attack_a = True
            elif keys[pygame.K_KP8]:
                if not playerTwo.attack_a and not playerTwo.attack_c:
                    if playerTwo.crouching is True:
                        if not playerTwo.setAction:
                            playerTwo.crouch_attack_b = True
                    else:
                        if not playerTwo.setAction:
                            playerTwo.attack_b = True
            elif keys[pygame.K_KP9]:
                if not playerTwo.attack_a and not playerTwo.attack_b:
                    if playerTwo.crouching is True:
                        if not playerTwo.setAction:
                            playerTwo.crouch_attack_c = True
                    else:
                        if not playerTwo.setAction:
                            playerTwo.attack_c = True
            elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
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
                        playerTwo.blockingLow = True
                        x2_change = 0
                    else:
                        x2_change = 0
                else:
                    if playerTwo.facingRight:
                        playerTwo.blockingHigh = True
                        x2_change = -1.5
                    else:
                        x2_change = -1.5
            elif keys[pygame.K_RIGHT]:
                if keys[pygame.K_DOWN]:
                    playerTwo.crouching = True
                    if playerTwo.facingRight:
                        x2_change = 0
                    else:
                        playerTwo.blockingLow = True
                        x2_change = 0
                else:
                    if playerTwo.facingRight:
                        x2_change = 1.5
                    else:
                        playerTwo.blockingHigh = True
                        x2_change = 1.5
            elif keys[pygame.K_DOWN]:
                playerTwo.crouching = True
                x2_change = 0

            if keys[pygame.K_u]:
                if not playerOne.attack_b and not playerOne.attack_c:
                    if playerOne.crouching is True:
                        if not playerOne.setAction:
                            playerOne.crouch_attack_a = True
                    else:
                        if not playerOne.setAction:
                            playerOne.attack_a = True
            elif keys[pygame.K_i]:
                if not playerOne.attack_a and not playerOne.attack_c:
                    if playerOne.crouching is True:
                        if not playerOne.setAction:
                            playerOne.crouch_attack_b = True
                    else:
                        if not playerOne.setAction:
                            playerOne.attack_b = True
            elif keys[pygame.K_o]:
                if not playerOne.attack_a and not playerOne.attack_b:
                    if playerOne.crouching is True:
                        if not playerOne.setAction:
                            playerOne.crouch_attack_c = True
                    else:
                        if not playerOne.setAction:
                            playerOne.attack_c = True
            elif keys[pygame.K_w] and keys[pygame.K_a]:
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
                        playerOne.blockingLow = True
                        x1_change = 0
                    else:
                        x1_change = 0
                else:
                    if playerOne.facingRight:
                        playerOne.blockingHigh = True
                        x1_change = -1.5
                    else:
                        x1_change = -1.5
            elif keys[pygame.K_d]:
                if keys[pygame.K_s]:
                    playerOne.crouching = True
                    if playerOne.facingRight:
                        x1_change = 0
                    else:
                        playerOne.blockingLow = True
                        x1_change = 0
                else:
                    if playerOne.facingRight:
                        x1_change = 1.5
                    else:
                        playerOne.blockingHigh = True
                        x1_change = 1.5
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

        # Checks to see for hit collision between the two players...
        player_one_attack = playerOne.check_attack_collision(playerTwo)
        player_two_attack = playerTwo.check_attack_collision(playerOne)
        if player_one_attack is not None:
            confirm = playerOne.calculate_damage(playerTwo, player_one_attack)
            if confirm:
                retract_attack(playerTwo)
                if playerTwo.isJumping or playerTwo.isDescending:
                    playerTwo.got_air_hit = True
                else:
                    playerTwo.got_hit = True
            else:
                retract_attack(playerTwo)
                playerTwo.block_hit = True
            playerOne.hit_confirm = True
        if player_two_attack is not None:
            confirm = playerTwo.calculate_damage(playerOne, player_two_attack)
            if confirm:
                retract_attack(playerOne)
                if playerOne.isJumping or playerOne.isDescending:
                    playerOne.got_air_hit = True
                else:
                    playerOne.got_hit = True
            else:
                retract_attack(playerOne)
                playerOne.block_hit = True
            playerTwo.hit_confirm = True

        playerOne.check_facing(playerTwo)
        playerOne.button_buffer_decrease()

        playerTwo.check_facing(playerOne)
        playerTwo.button_buffer_decrease()

        player_one_hit_wall = check_bounds(playerOne)
        player_two_hit_wall = check_bounds(playerTwo)

        if playerOne.x <= 0:
            if playerTwo.x + playerTwo.character.rect.width < 800:
                diff = 0 - playerOne.x
                playerOne.x = 0

                LEFT_BOUND.move_wall(diff)
                RIGHT_BOUND.move_wall(diff)
                playerTwo.x += diff
                if player_one_hit_wall != 'left':
                    stage_x += diff
            else:
                playerOne.x = 0

        if playerOne.x + playerOne.character.rect.width >= 800:
            if playerTwo.x > 0:
                diff = (playerOne.x + playerOne.character.rect.width) - 800
                playerOne.x = 800 - playerOne.character.rect.width

                RIGHT_BOUND.move_wall(-diff)
                LEFT_BOUND.move_wall(-diff)
                playerTwo.x -= diff
                if player_one_hit_wall != 'right':
                    stage_x -= diff
            else:
                playerOne.x = 800 - playerOne.character.rect.width

        if playerTwo.x <= 0:
            if playerOne.x + playerOne.character.rect.width < 800:
                diff = 0 - playerTwo.x
                playerTwo.x = 0

                LEFT_BOUND.move_wall(diff)
                RIGHT_BOUND.move_wall(diff)
                playerOne.x += diff
                if player_two_hit_wall != 'left':
                    stage_x += diff
            else:
                playerTwo.x = 0

        if playerTwo.x + playerTwo.character.rect.width >= 800:
            if playerOne.x > 0:
                diff = (playerTwo.x + playerTwo.character.rect.width) - 800
                playerTwo.x = 800 - playerTwo.character.rect.width

                RIGHT_BOUND.move_wall(-diff)
                LEFT_BOUND.move_wall(-diff)
                playerOne.x -= diff
                if player_two_hit_wall != 'right':
                    stage_x -= diff
            else:
                playerTwo.x = 800 - playerTwo.character.rect.width

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
                            playerOne.x = playerTwo.x - playerOne.character.rect.width
                        elif player_two_hit_wall == 'left':
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
                                playerTwo.x = playerOne.x - playerTwo.character.rect.width
                            elif player_one_hit_wall == 'left':
                                playerTwo.x = playerOne.x + playerOne.character.rect.width
                            else:
                                playerOne.x = playerTwo.max_collision_right(playerOne) - 30
                    elif playerTwo.isDescending:
                        playerOne.x = playerTwo.max_collision_right(playerOne)

        fpsClock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    game_loop()