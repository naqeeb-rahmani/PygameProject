import pygame, sys, random
from Player_Class import *
#screen#

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
####################

#---------game-variables------------#

game = True


#-----------------------------------#

pygame.init()

player_1 = player(None, 400, 395)


#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

###################################################################################

while game == True:

    screen.fill((255,255,255))

    #level 1

    platforms = []

    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0,450, SCREEN_WIDTH + 0, SCREEN_HEIGHT-450))
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(0,450, SCREEN_WIDTH + 0, SCREEN_HEIGHT-710))
    pygame.draw.rect(screen, (0,0,0), player_1.rect)

    ###################################
 
    player_1.move()
    player_1.jump_()
    player_1.gravity_and_collision()
    ##################################

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: player_1.direction = "Right"
            if event.key == pygame.K_a: player_1.direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: player_1.direction = None
            if event.key == pygame.K_a: player_1.direction = None
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_1.jump = True
            



        if event.type == pygame.QUIT:
            pygame.quit()
            exit()