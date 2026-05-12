import pygame
from Player_Class import *
from Platform_Class import *
from Pressure_Plates_Class import *
from Lever_Class import *
from Coin_Class import *
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

player_1 = player("player_1", 400, 350, False)


player_2 = player("player_2", 500, 350, True)
player_2.speed = 6.7
player_2.jump_height = 170

#p1_interact_button = E 
#p2_interact_button = RETURN 


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


#levers#

lever_off_sprite = pygame.image.load("Assets\Map\Lever\LeverOff.png").convert_alpha()
lever_on_sprite = pygame.image.load("Assets\Map\Lever\LeverOn.png").convert_alpha()

small_lever_off_sprite = pygame.transform.scale(lever_off_sprite, (50, 55))
small_lever_on_sprite = pygame.transform.scale(lever_on_sprite, (50, 55))

big_lever_off_sprite = pygame.transform.scale(lever_off_sprite, (60, 65))
big_lever_on_sprite = pygame.transform.scale(lever_on_sprite, (60, 65))

###coins###

coin_spritesheet = pygame.image.load("Assets\Map\Coin\Coin 16x16.png")

#################


total_coins = "dont know yet"

#to display number of coins#

display_number_of_coins_font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", 20)

display_number_of_coins = display_number_of_coins_font.render(f"Coin: {player_2.coins_collected} / {total_coins}", True, (0,0,0))


####map####

floor = platform(MAP_WIDTH, 270, 0, 450, (150,75,0))
grass = platform(MAP_WIDTH, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))
roof = platform(MAP_WIDTH, 5, 0,0, (0,0,0))

wall_left = platform(20, SCREEN_HEIGHT + 100, 0, -100, (10,10,10))

###############3

platform_1 = platform(200, 20, 0, 320, (0,0,0))

platform_2 = platform(300, 22.5, 340, 150, (0,0,0))

platform_2_plate = pressure_plate(400, 140)

coin_1 = coin(500, 100, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))
coin_1.get_coin_animation(coin_spritesheet, 14)

wall_under_platform_2 = platform(20, 300, 620, 150, (0,0,0)) #wall_1
wall_above_platform_2 = platform(20, 300, 620, -150, (0,0,0)) #wall_2

###############

wall_3 = platform(20, (820-270), 850, -100, (0,0,0))

lever_1 = lever(740, 395, small_lever_off_sprite, small_lever_on_sprite,"lever_1", True)

platform_3 = platform(90, 20, 760, 320, (0,0,0))
platform_4 = platform(80, 10, 620, 220, (0,0,0))
platform_5 = platform(90,20, 760, 130, (0,0,0))

lever_2 = lever(780, 265, small_lever_off_sprite, small_lever_on_sprite,"lever_2", True)

coin_2 = None

lever_3 = lever(780, 65, big_lever_off_sprite, big_lever_on_sprite,"lever_3", False)

###########



platforms = [floor.rect, grass.rect, wall_left.rect, platform_1.rect, platform_2.rect, platform_2_plate.rect ,wall_under_platform_2.rect, wall_above_platform_2.rect,
wall_3.rect, platform_3.rect, platform_4.rect, platform_5.rect, roof.rect]

pressure_plates = [platform_2_plate]

non_collideable_objects = [lever_1, coin_1, lever_2, lever_3]

levers = [lever_1, lever_2, lever_3]
coins = [coin_1]

#######

#pressure plate activation#

def update_pressure_plates():
    for pressure_plate in pressure_plates:
        if ((player_2.rect.bottom == pressure_plate.rect.top) and (player_2.on_something == True)):
            pressure_plate.activated = True; pressure_plate.colour = (0,0,255)
        else:
            pressure_plate.activated = False; pressure_plate.colour = (255,0,0)

        if pressure_plate.activated == True:
            if (pressure_plate.y - pressure_plate.y_unactivated) < 8:
                pressure_plate.y += 0.5; pressure_plate.rect.y = pressure_plate.y
            
        else:
            if (pressure_plate.y - pressure_plate.y_unactivated) > 0:
                pressure_plate.y -= 0.5; pressure_plate.rect.y = pressure_plate.y

def pressure_plate_and_lever_effects(): #the things they activate
    if platform_2_plate.activated == True or lever_1.on == True:
        if (wall_under_platform_2.start_position_y - wall_under_platform_2.y) < 150:
            wall_under_platform_2.y -= 5; wall_under_platform_2.rect.y = wall_under_platform_2.y
    else:
        if (wall_under_platform_2.start_position_y - wall_under_platform_2.y) > 0:
            wall_under_platform_2.y += 5; wall_under_platform_2.rect.y = wall_under_platform_2.y


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
    for object in non_collideable_objects:
        object.x += move; object.rect.x = object.x
  
    player_1.x += move; player_1.rect.x = player_1.x
    player_2.x += move; player_2.rect.x = player_2.x


###################################################################################

while game == True:

    screen.fill((255,255,255))

    pygame.draw.rect(screen, floor.colour, floor)
    pygame.draw.rect(screen, grass.colour, grass)
    pygame.draw.rect(screen, roof.colour, roof.rect)

        ###################################
 
    #player_1.animation(screen)

    player_1.movemenet_collision_gravity(platforms)
    player_1.animation(screen)

    player_2.animation(screen)
    player_2.movemenet_collision_gravity(platforms)

    update_pressure_plates()

    pressure_plate_and_lever_effects ()

    camera(player_1, player_2, platforms, SCREEN_WIDTH)

    ##################################

    pygame.draw.rect(screen, wall_left.colour, wall_left)
    pygame.draw.rect(screen, platform_1.colour, platform_1)

    pygame.draw.rect(screen, platform_2_plate.colour, platform_2_plate.rect)
    pygame.draw.rect(screen, platform_2.colour, platform_2)

    pygame.draw.rect(screen, wall_under_platform_2.colour, wall_under_platform_2)
    pygame.draw.rect(screen, wall_above_platform_2.colour, wall_above_platform_2)

    #pygame.draw.rect(screen, (0,0,0), lever_1.rect)

    pygame.draw.rect(screen, wall_3.colour, wall_3.rect)

    screen.blit(lever_1.sprite, (lever_1.x, lever_1.y))

    pygame.draw.rect(screen, platform_3.colour, platform_3.rect)

    screen.blit(lever_2.sprite, (lever_2.x, lever_2.y))

    pygame.draw.rect(screen, platform_4.colour, platform_4.rect)

    pygame.draw.rect(screen, platform_5.colour, platform_5.rect)

    screen.blit(lever_3.sprite, (lever_3.x, lever_3.y))


    for coin in coins:
        coin.animate(screen)
        
    player_2.collect_coins(coins)

    display_number_of_coins = display_number_of_coins_font.render(f"Coins: {player_2.coins_collected} / {total_coins}", True, (0,0,0))
    screen.blit(display_number_of_coins, (5, 650))



    ##################################

    pygame.display.update()
    clock.tick(120)
    for event in pygame.event.get():


        if event.type == pygame.KEYDOWN:
            #move#
            if event.key == pygame.K_d: player_1.direction = "Right"
            if event.key == pygame.K_a: player_1.direction = "Left"

            #interact#
            if event.key == pygame.K_e:
                for lever in levers:
                    if player_1.rect.colliderect(lever.rect):
                        if lever.toggleable == True:
                            if lever.button_pressed == False:
                                if lever.on != True:
                                    lever.on = True
                                elif lever.on == True:
                                    lever.on = False
                                lever.button_pressed = True
                        elif lever.toggleable != True:
                            lever.on = True
                        
                        lever.update_lever_sprite_based_on_state()

        if event.type == pygame.KEYUP:
            #move
            if event.key == pygame.K_d: player_1.direction = None; player_1.last_direction = "Right"
            if event.key == pygame.K_a: player_1.direction = None; player_1.last_direction = "Left"

            #interact#
            if event.key == pygame.K_e:
                for lever in levers:
                    if player_1.rect.colliderect(lever.rect):
                        if lever.toggleable == True:
                            lever.button_pressed = False

                        elif lever.toggleable != True:
                            if lever.on == True:
                                lever.on = False
                            
                            lever.update_lever_sprite_based_on_state()
    
                            
            
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: 
                if player_1.on_something: player_1.jump = True #trigger on key release to decrease bugs such as double jumping




        #if event.type == pygame.KEYDOWN:



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: player_2.direction = "Right"
            if event.key == pygame.K_LEFT: player_2.direction = "Left"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: player_2.direction = None; player_2.last_direction = "Right"
            if event.key == pygame.K_LEFT: player_2.direction = None; player_2.last_direction = "Left"
            
            #jump
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                if player_2.on_something: player_2.jump = True;


        #setting player_1 direction to None if they are holding down e for a non toggleable lever so they cant move during that period
        for lever_ in levers:
            if lever_.on == True and lever_.toggleable != True:
                player_1.direction = None

        ########


        if event.type == pygame.QUIT:
            pygame.quit()
            exit()