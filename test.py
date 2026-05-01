import pygame, sys, random
from Player_Class import *
from Platform_Class import *
#screen#

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
####################

#---------game-variables------------#

game = True


#-----------------------------------#

pygame.init()

player_1 = player(None, 400, 350)

#    p1 idle animation    #
#player_1_idle_spritesheet = pygame.image.load(r\) 



#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

###################################################################################

while game == True:

    screen.fill((255,255,255))

    #level 1

    floor = platform(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 450, (150,75,0))
    grass = platform(SCREEN_WIDTH, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))
    #platform_1 = platform(200, 20, 0, 430, (0,0,0))

    platforms = [floor.rect,grass.rect]

    pygame.draw.rect(screen, floor.colour, floor)
    pygame.draw.rect(screen, grass.colour, grass)
    #pygame.draw.rect(screen, platform_1.colour, platform_1)
    pygame.draw.rect(screen, (0,0,0), player_1.rect)

    ###################################
 
    player_1.move()
    player_1.gravity_and_collision(platforms)
    player_1.jump_function()
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
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: 
                if player_1.on_something: player_1.jump = True #trigger on key release to increase bugs such as double jumping
        
        '''keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_1.on_something: player_1.jump = True'''
            



        if event.type == pygame.QUIT:
            pygame.quit()
            exit()