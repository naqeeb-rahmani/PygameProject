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

game= True

mode = "game"

experiment_failed = False

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


#to display number of coins#

display_number_of_coins_font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", 20)

#display_number_of_coins = display_number_of_coins_font.render(f"Coin: {player_2.coins_collected} / {len(coins)}", True, (0,0,0))


####map####

### background ###

background = pygame.image.load("Assets\Map\Background\Dungeon_brick_wall_grey.png")

##################


floor = platform(MAP_WIDTH + 2000, 270, 0, 450, (150,75,0))
grass = platform(MAP_WIDTH + 2000, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))
roof = platform(MAP_WIDTH, 5, 0,0, (0,0,0))

wall_left = platform(20, SCREEN_HEIGHT + 100, 0, -100, (10,10,10))

###############3

platform_1 = platform(200, 20, 0, 320, (0,0,0))

platform_2 = platform(300, 22.5, 340, 150, (0,0,0))

platform_2_plate = pressure_plate(400, 140)

coin_1 = coin(500, 100, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

wall_under_platform_2 = platform(20, 300, 620, 150, (0,0,0)) #wall_1
wall_above_platform_2 = platform(20, 300, 620, -150, (0,0,0)) #wall_2

###############

wall_3_below = platform(20, 320, 850, 130, (0,0,0))
wall_3_above = platform(20, 130, 850, 0, (0,0,0))

lever_1 = lever(740, 395, small_lever_off_sprite, small_lever_on_sprite,"lever_1", True)

platform_3 = platform(90, 20, 760, 320, (0,0,0))
platform_4 = platform(80, 10, 620, 220, (0,0,0))
platform_5 = platform(90,20, 760, 130, (0,0,0))

lever_2 = lever(780, 265, small_lever_off_sprite, small_lever_on_sprite,"lever_2", True)

coin_2 = coin(650, 170, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

lever_3 = lever(780, 65, big_lever_off_sprite, big_lever_on_sprite,"lever_3", False)

###########

platform_6 = platform(100, 20, 870, 200, (0,0,0))
platform_6_extension = platform(100, 20, 870, 200, (0,0,0))

plate_2 = pressure_plate(900,440)

coin_3 = coin(900, 220, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

wall_4 = platform(20, 250, 970, 200, (0,0,0))

lever_4 = lever(1100, 385, big_lever_off_sprite, big_lever_on_sprite,"lever_4", False)

platform_7 = platform(200, 20, 1200, 300, (0,0,0))

platform_8 = platform(200, 20, 1200, 100, (0,0,0))

lever_5 = lever(1220, 45, small_lever_off_sprite, small_lever_on_sprite,"lever_5", True)

lever_6 = lever(1330, 45, small_lever_off_sprite, small_lever_on_sprite,"lever_6", True)

coin_4 = coin(1270, 250, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

platform_9 = platform(250, 20, 1700, 200, (0,0,0))

plate_3 = pressure_plate(1800, 190)

coin_5 = coin(1800, 220, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

coin_6 = coin(1800, 20, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

wall_5_upper_part = platform(20, 200, 1950, 0, (0,0,0))
wall_5_under_part = platform(20, 250, 1950, 200, (0,0,0))

###################
plate_4 = pressure_plate(2050, 440)

wall_6 = platform(20, 450, 3000, 0, (0,0,0))

platform_10 = platform(200, 20, 1950, 200, (0,0,0))

lever_7 = lever(2000, 150, small_lever_off_sprite, small_lever_on_sprite,"lever_7", True)

platform_11 = platform(150, 20, 2400, 300, (0,0,0))

plate_5 = pressure_plate(2455, 290)

coin_7 = coin(2450, 100, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

coin_8 = coin(2900, 50, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

lever_8 = lever(2035, 145, small_lever_off_sprite, small_lever_on_sprite,"lever_8", True)

lever_9 = lever(2450, 385, big_lever_off_sprite, big_lever_on_sprite,"lever_9", False)

wall_7 = platform(20, 100, 2850, 0, (0,0,0))

platform_12 = platform(150, 20, 2850, 100, (0,0,0))

lever_10 = lever(2850, 395, small_lever_off_sprite, small_lever_on_sprite,"lever_10", True)

plate_6 = pressure_plate(3100, 440)

###############33

exit_roof = platform(2000, 300, 3000, 0, (0,0,0))


platforms = [floor.rect, grass.rect, roof.rect ,wall_left.rect, platform_1.rect, platform_2.rect, platform_2_plate.rect ,wall_under_platform_2.rect, wall_above_platform_2.rect,
wall_3_below.rect, wall_3_above.rect,platform_3.rect, platform_4.rect, platform_5.rect, platform_6.rect, platform_6_extension.rect, plate_2.rect, wall_4.rect, platform_7.rect, platform_8.rect, platform_9.rect, 
wall_5_upper_part.rect, wall_5_under_part.rect, plate_3.rect, wall_6.rect, plate_4.rect, platform_10.rect, platform_11.rect, plate_5.rect,wall_7.rect, platform_12.rect, exit_roof.rect, plate_6.rect]

horizontally_moving_platforms = [platform_6_extension, platform_12]

pressure_plates = [platform_2_plate, plate_2, plate_3, plate_4, plate_5, plate_6]

non_collideable_objects = [lever_1, coin_1, lever_2, coin_2, lever_3, coin_3, lever_4, lever_5, lever_6, coin_4, coin_5, coin_6, coin_7, coin_8, lever_8, lever_9, lever_10]

levers = [lever_1, lever_2, lever_3, lever_4, lever_5, lever_6, lever_7, lever_8, lever_9, lever_10]
coins = [coin_1, coin_2, coin_3, coin_4, coin_5, coin_6, coin_7, coin_8]

total_coins = len(coins)

for coin in coins:
    coin.get_coin_animation(coin_spritesheet, 14)

#######

################
#for testing the map while making it

'''for x in platforms:
    x.x -= 2000
for x in non_collideable_objects:
    x.x -= 2000
for x in horizontally_moving_platforms:
    x.x -= 2000; x.rect.x = x.x; x.start_position_x -= 2000'''


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

    if (lever_1.on != True and lever_2.on != True and lever_3.on == True) or plate_2.activated == True:
        if (wall_3_above.start_position_y - wall_3_above.y) > -130:
            wall_3_above.y += 5; wall_3_above.rect.y = wall_3_above.y
    else:
        if (wall_3_above.start_position_y - wall_3_above.y) < 0:
            wall_3_above.y -= 5; wall_3_above.rect.y = wall_3_above.y
    
    if lever_1.on != True and lever_2.on == True and lever_3.on != True:
        if (platform_6_extension.x - platform_6_extension.start_position_x) <= 90:
            platform_6_extension.x += 5; platform_6_extension.rect.x = platform_6_extension.x

            if player_2.rect.colliderect(platform_6_extension.rect):
                player_2.x += 5
                player_2.rect.x = player_2.x
            
            #its pretty much impossible for player_1 to collide with the platform because of its speed and becauce player_1 is the one that activates it 
            #but i'll still check it just to be safe
            
            if player_1.rect.colliderect(platform_6_extension.rect):
                player_1.x += 5
                player_1.rect.x = player_1.x
    else:
        if (platform_6_extension.x - platform_6_extension.start_position_x) > 0:
            platform_6_extension.x -= 5; platform_6_extension.rect.x = platform_6_extension.x

    if (lever_1.on == True and lever_2.on == True and lever_3.on == True) or lever_4.on == True:
        if (wall_4.start_position_y - wall_4.y) < 200:
            wall_4.y -= 5; wall_4.rect.y = wall_4.y
    else:
        if (wall_4.start_position_y - wall_4.y) > 0:
            wall_4.y += 5; wall_4.rect.y = wall_4.y

        for player in [player_1, player_2]:
            if player.rect.colliderect(wall_4.rect) and player.rect.bottom > wall_4.rect.bottom:
                experiment_failed = True
                
        

    if plate_3.activated == True and lever_5.on != True and lever_6.on == True:
        if (wall_5_upper_part.y - wall_5_upper_part.start_position_y) < 200:
            wall_5_upper_part.y += 5; wall_5_upper_part.rect.y = wall_5_upper_part.y
    else:
        if (wall_5_upper_part.y - wall_5_upper_part.start_position_y) > 0:
            wall_5_upper_part.y -= 5; wall_5_upper_part.rect.y = wall_5_upper_part.y

    if lever_5.on == True and lever_6.on != True and plate_4.activated == True:
        if (wall_5_under_part.start_position_y - wall_5_under_part.y) < 200:
            wall_5_under_part.y -= 5; wall_5_under_part.rect.y = wall_5_under_part.y
    else:
        if (wall_5_under_part.start_position_y - wall_5_under_part.y) > 0:
            wall_5_under_part.y += 5; wall_5_under_part.rect.y = wall_5_under_part.y

    if plate_5.activated == True and lever_9.on == True and lever_8.on != True:
        if (wall_7.start_position_y - wall_7.y) < 100:
            wall_7.y -= 5; wall_7.rect.y = wall_7.y
        if (platform_12.x - platform_12.start_position_x) < 150:
            platform_12.x += 7.5; platform_12.rect.x = platform_12.x

    if ((lever_8.on == True) and (lever_9.on == True) and (lever_10.on == True) and (player_1.coins_collected == len(coins)) and (plate_5.activated != True) and (plate_4.activated != True)) or plate_6.activated == True:
        if (wall_6.start_position_y - wall_6.y) < 150:
            wall_6.y -= 5; wall_6.rect.y = wall_6.y
    else:
        if (wall_6.start_position_y - wall_6.y) > 0:
            wall_6.y += 5; wall_6.rect.y = wall_6.y


# experiment failed - player took damage

def failed_or_not():
    if player_1.y > 720 or player_1.y < 0 or player_2.y > 720 or player_2.y < 0:
        experiment_failed = True
    

#camera#

def camera(player_1, player_2, platforms, horizontally_moving_platforms,SCREEN_WIDTH):
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
    for horizontally_moving_platform in horizontally_moving_platforms:
        horizontally_moving_platform.start_position_x += move; horizontally_moving_platform.x += move; horizontally_moving_platform.rect.x = horizontally_moving_platform.x 
  
    player_1.x += move; player_1.rect.x = player_1.x
    player_2.x += move; player_2.rect.x = player_2.x



###################################################################################

while game == True:

    screen.fill((255,255,255))

    #screen.blit(background, (0,0))

        ###################################
 
    #player_1.animation(screen)

    player_1.movemenet_collision_gravity(platforms)
    player_1.animation(screen)

    player_2.animation(screen)
    player_2.movemenet_collision_gravity(platforms)

    failed_or_not()

    update_pressure_plates()

    pressure_plate_and_lever_effects ()

    camera(player_1, player_2, platforms, horizontally_moving_platforms,SCREEN_WIDTH)

    ##################################


    pygame.draw.rect(screen, wall_left.colour, wall_left)
    pygame.draw.rect(screen, platform_1.colour, platform_1)

    pygame.draw.rect(screen, platform_2_plate.colour, platform_2_plate)
    pygame.draw.rect(screen, platform_2.colour, platform_2)

    pygame.draw.rect(screen, wall_under_platform_2.colour, wall_under_platform_2)
    pygame.draw.rect(screen, wall_above_platform_2.colour, wall_above_platform_2)

    #pygame.draw.rect(screen, (0,0,0), lever_1.rect)

    pygame.draw.rect(screen, wall_3_below.colour, wall_3_below)
    pygame.draw.rect(screen, wall_3_above.colour, wall_3_above)

    screen.blit(lever_1.sprite, (lever_1.x, lever_1.y))

    pygame.draw.rect(screen, platform_3.colour, platform_3)

    screen.blit(lever_2.sprite, (lever_2.x, lever_2.y))

    pygame.draw.rect(screen, platform_4.colour, platform_4)

    pygame.draw.rect(screen, platform_5.colour, platform_5)

    screen.blit(lever_3.sprite, (lever_3.x, lever_3.y))

    pygame.draw.rect(screen, platform_6.colour, platform_6)
    pygame.draw.rect(screen, platform_6_extension.colour, platform_6_extension)

    pygame.draw.rect(screen, plate_2.colour, plate_2)

    pygame.draw.rect(screen, wall_4.colour, wall_4)

    screen.blit(lever_4.sprite, (lever_4.x, lever_4.y))

    pygame.draw.rect(screen, platform_7.colour, platform_7)

    pygame.draw.rect(screen, platform_8.colour, platform_8)

    screen.blit(lever_5.sprite, (lever_5.x, lever_5.y))

    screen.blit(lever_6.sprite, (lever_6.x, lever_6.y))

    pygame.draw.rect(screen, plate_3.colour, plate_3)

    pygame.draw.rect(screen, platform_9.colour, platform_9)

    pygame.draw.rect(screen, wall_5_upper_part.colour, wall_5_upper_part)
    pygame.draw.rect(screen, wall_5_under_part.colour, wall_5_under_part)

    pygame.draw.rect(screen, plate_4.colour, plate_4)

    pygame.draw.rect(screen, wall_6.colour, wall_6)

    pygame.draw.rect(screen, platform_10.colour, platform_10.rect)
    
    pygame.draw.rect(screen, plate_5.colour, plate_5)

    pygame.draw.rect(screen, platform_11.colour, platform_11.rect)

    screen.blit(lever_8.sprite, (lever_8.x, lever_8.y))

    screen.blit(lever_9.sprite, (lever_9.x, lever_9.y))

    pygame.draw.rect(screen, wall_7.colour, wall_7.rect)

    pygame.draw.rect(screen, platform_12.colour, platform_12.rect)

    screen.blit(lever_10.sprite, (lever_10.x, lever_10.y))

    pygame.draw.rect(screen, exit_roof.colour, exit_roof)

    pygame.draw.rect(screen, plate_6.colour, plate_6)

    #screen.blit(lever_11.sprite, (lever_11.x, lever_11.y))

##############################################
    pygame.draw.rect(screen, floor.colour, floor)
    pygame.draw.rect(screen, grass.colour, grass)
    pygame.draw.rect(screen, roof.colour, roof.rect)
####################################################

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
                if player_2.on_something: player_2.jump = True


        #setting player_1 direction to None if they are holding down e for a non toggleable lever so they cant move during that period
        for lever_ in levers:
            if lever_.on == True and lever_.toggleable != True:
                player_1.direction = None

        ########


        if event.type == pygame.QUIT:
            pygame.quit()
            exit()