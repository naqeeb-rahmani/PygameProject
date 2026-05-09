import pygame, math, sys, random
from Player_Class import *
from Platform_Class import *
#screen#

SCREEN_WIDTH = 1280
MAP_WIDTH = 3000
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
####################

#game name: Not Alone
#        * But Together

#---------game-variables------------#

game = True


#-----------------------------------#

pygame.init()

player_1 = player("player_1", 400, 350)


player_2 = player("player_2", 500, 350)
player_2.speed = 6.7
player_2.jump_height = 180


#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not Alone")

#  saving the animations  #

#player_1

player_1_idle_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerIdleRight 48x48.png").convert_alpha()
player_1_idle_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerIdleLeft 48x48.png").convert_alpha()

player_1.get_animations("idle", player_1.animations["idle"]["number of frames"], "right", player_1_idle_spritesheet_right)
player_1.get_animations("idle", player_1.animations["idle"]["number of frames"], "left", player_1_idle_spritesheet_left)

###

player_1_walk_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerWalkRight 48x48.png").convert_alpha()
player_1_walk_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerWalkLeft 48x48.png").convert_alpha()

player_1.get_animations("walk", player_1.animations["walk"]["number of frames"], "right", player_1_walk_spritesheet_right)
player_1.get_animations("walk", player_1.animations["walk"]["number of frames"], "left", player_1_walk_spritesheet_left)

###

player_1_land_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerLandRight 48x48.png").convert_alpha()
player_1_land_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerLandLeft 48x48.png").convert_alpha()

player_1.get_animations("land", player_1.animations["land"]["number of frames"], "right", player_1_land_spritesheet_right)
player_1.get_animations("land", player_1.animations["land"]["number of frames"], "left", player_1_land_spritesheet_left)

player_1_jump_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerJumpRight 48x48.png").convert_alpha()
player_1_jump_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_1\PlayerJumpLeft 48x48.png").convert_alpha()

player_1.get_animations("jump", player_1.animations["jump"]["number of frames"], "right", player_1_jump_spritesheet_right)
player_1.get_animations("jump", player_1.animations["jump"]["number of frames"], "left", player_1_jump_spritesheet_left)

#player_2#
player_2_idle_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerIdleRight 48x48.png").convert_alpha()
player_2_idle_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerIdleLeft 48x48.png").convert_alpha()

player_2.get_animations("idle", player_1.animations["idle"]["number of frames"], "right", player_2_idle_spritesheet_right)
player_2.get_animations("idle", player_1.animations["idle"]["number of frames"], "left", player_2_idle_spritesheet_left)


player_2_run_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerRunRight 48x48.png").convert_alpha()
player_2_run_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerRunLeft 48x48.png").convert_alpha()

player_2.get_animations("run", player_1.animations["run"]["number of frames"], "right", player_2_run_spritesheet_right)
player_2.get_animations("run", player_1.animations["run"]["number of frames"], "left", player_2_run_spritesheet_left)

###

player_2_jump_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerJumpRight 48x48.png").convert_alpha()
player_2_jump_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerJumpLeft 48x48.png").convert_alpha()

player_2.get_animations("jump", player_2.animations["jump"]["number of frames"], "right", player_2_jump_spritesheet_right)
player_2.get_animations("jump", player_2.animations["jump"]["number of frames"], "left", player_2_jump_spritesheet_left)

player_2_land_spritesheet_right = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerLandRight 48x48.png").convert_alpha()
player_2_land_spritesheet_left = pygame.image.load("Assets\Player_Sprites\Player_2\PlayerLandLeft 48x48.png").convert_alpha()

player_2.get_animations("land", player_2.animations["land"]["number of frames"], "right", player_2_land_spritesheet_right)
player_2.get_animations("land", player_2.animations["land"]["number of frames"], "left", player_2_land_spritesheet_left)

#####################################################################

floor = platform(MAP_WIDTH, 270, 0, 450, (150,75,0))
grass = platform(MAP_WIDTH, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))

wall_left = platform(20, SCREEN_HEIGHT + 100, 0, -100, (10,10,10))

#TEST PLATFORM#
platform_1 = platform(200, 20, 0, 320, (0,0,0))

platform_2 = platform(300, 22.5, 340, 150, (0,0,0))

platforms = [floor.rect,grass.rect, wall_left.rect, platform_1.rect, platform_2.rect]



#camera#

def camera(player_1, player_2, platforms, SCREEN_WIDTH):
    middle_xcor = (player_1.x + player_2.x) /2

    deadzone = 50

    if middle_xcor > (((SCREEN_WIDTH)/2) + deadzone):
        move = -5
    elif middle_xcor < (((SCREEN_WIDTH)/2) - deadzone ):
        move = 5
    else:
        move = 0

    for platform in platforms:
        platform.x += move
  
    player_1.x += move; player_1.rect.x = player_1.x
    player_2.x += move; player_2.rect.x = player_2.x


###################################################################################

while game == True:

    screen.fill((255,255,255))

    pygame.draw.rect(screen, floor.colour, floor)
    pygame.draw.rect(screen, grass.colour, grass)
    pygame.draw.rect(screen, wall_left.colour, wall_left)
    pygame.draw.rect(screen, platform_1.colour, platform_1)
    pygame.draw.rect(screen, platform_2.colour, platform_2)

    #pygame.draw.rect(screen, (0,0,0), player_1.rect)
    #pygame.draw.rect(screen, (0,0,0), player_2.rect)


    ###################################
 
    #player_1.animation(screen)
    player_1.movemenet_collision_gravity(platforms)
    player_1.animation(screen)

    player_2.animation(screen)
    player_2.movemenet_collision_gravity(platforms)

    camera(player_1, player_2, platforms, SCREEN_WIDTH)

    ##################################

    pygame.display.update()
    clock.tick(120)
    for event in pygame.event.get():


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: player_1.direction = "Right"
            if event.key == pygame.K_a: player_1.direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: player_1.direction = None; player_1.last_direction = "Right"
            if event.key == pygame.K_a: player_1.direction = None; player_1.last_direction = "Left"
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: 
                if player_1.on_something: player_1.jump = True #trigger on key release to decrease bugs such as double jumping


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: player_2.direction = "Right"
            if event.key == pygame.K_LEFT: player_2.direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: player_2.direction = None; player_2.last_direction = "Right"
            if event.key == pygame.K_LEFT: player_2.direction = None; player_2.last_direction = "Left"
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                if player_2.on_something: player_2.jump = True

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()