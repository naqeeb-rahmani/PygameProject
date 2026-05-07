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

player_1 = player( 400, 350)

player_2 = player( 500, 350)


#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#    p1 idle animation sheet   #

player_1_idle_spritesheet = pygame.image.load("Assets\Player_Sprites\Player_1\Player Idle 48x48.png").convert_alpha()

player_1.get_animations("idle", 10, player_1_idle_spritesheet, "left to right")

player_2_idle_spritesheet = pygame.image.load("Assets\Player_Sprites\Player_1\Player Idle 48x48.png").convert_alpha()

player_2.get_animations("idle", 10, player_2_idle_spritesheet, "left to right")


#####################################################################

floor = platform(SCREEN_WIDTH, 270, 0, 450, (150,75,0))
grass = platform(SCREEN_WIDTH, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))
wall_left = platform(20, SCREEN_HEIGHT, 0, 0, (10,10,10))

#TEST PLATFORM#
platform_1 = platform(200, 20, 0, 320, (0,0,0))

platforms = [floor.rect,grass.rect, wall_left.rect, platform_1.rect]

###################################################################################

while game == True:

    screen.fill((255,255,255))

    pygame.draw.rect(screen, floor.colour, floor)
    pygame.draw.rect(screen, grass.colour, grass)
    pygame.draw.rect(screen, wall_left.colour, wall_left)
    pygame.draw.rect(screen, platform_1.colour, platform_1)
#    pygame.draw.rect(screen, platform_1.colour, platform_1)
    pygame.draw.rect(screen, (0,0,0), player_1.rect)
    pygame.draw.rect(screen, (0,0,0), player_2.rect)
#    screen.blit(player_1.animation["idle"][0], (player_1.x-player_1.player_offset_rect_x, player_1.y-player_1.player_offset_rect_y))

    ###################################
 
    player_1.animation(screen)
    player_1.movemenet_collision_gravity(platforms)

    player_2.animation(screen)
    player_2.movemenet_collision_gravity(platforms)

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
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: player_2.direction = "Right"
            if event.key == pygame.K_LEFT: player_2.direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: player_2.direction = None
            if event.key == pygame.K_LEFT: player_2.direction = None
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                if player_2.on_something: player_2.jump = True

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()