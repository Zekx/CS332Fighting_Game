import pygame
from Character import Character

class Otis(Character):

    def __init__(self):
        super().__init__()

        self.name = 'Otis'
        self.health = 200
        self.health = 0
        self.portrait = pygame.image.load('Sprites/Otis/OtisPortrait.png')

        self.image = pygame.image.load('Sprites/Otis/OtisStand1.png')

        self.neutralPosition = pygame.image.load('Sprites/Otis/OtisStand1.png')

        #The following loops add in all of the sprites for the animation...

        #Inserts Otis's standing animation.
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Otis/OtisStand1.png'), (130, 250)))
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Otis/OtisStand2.png'), (130, 250)))
        for x in range(0, 30):
            self.standing.append(pygame.transform.scale(pygame.image.load('Sprites/Otis/OtisStand3.png'), (130, 250)))

    def update(self, player, x):
        if player.isDashing:
            if player.facingRight and not player.setAction:
                player.multiplier = 1
                player.setAction = True
            elif not player.facingRight and not player.setAction:
                player.multiplier = -1
                player.setAction = True

            if player.currentDash < len(player.character.dash)/2:
                player.x += 0.7*player.multiplier
            elif player.currentDash > len(player.character.dash)/2 and \
                                            player.currentDash < len(player.character.dash)/1.5:
                player.x += 0.35*player.multiplier
            elif player.currentDash > len(player.character.dash)/1.5:
                player.x += 0.175*player.multiplier
            player.currentDash += 1.0

            if player.currentDash >= len(player.character.dash):
                player.isDashing = False
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
        elif player.isBackDashing:
            if player.facingRight and not player.setAction:
                player.multiplier = 1
                player.setAction = True
            elif not player.facingRight and not player.setAction:
                player.multiplier = -1
                player.setAction = True

            if player.currentDash < len(player.character.backdash)/2:
                player.x += 0.7*(-1)*player.multiplier
                player.y -= 0.16
            elif player.currentDash > len(player.character.backdash)/2 \
                                        and player.currentDash < len(player.character.backdash)/1.5:
                player.x += 0.35*(-1)*player.multiplier
            elif player.currentDash > len(player.character.backdash)/1.5:
                player.x += 0.175*(-1)*player.multiplier
                player.y += 0.08
            player.currentDash += 1.0
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
                            pygame.transform.flip(self.character.crouching[player.index], True, False)
                        player.index += 1