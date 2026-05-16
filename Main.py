import pygame
from Player_Class import *
from Platform_Class import *
from Pressure_Plates_Class import *
from Lever_Class import *
from Coin_Class import *
from Game_Class import *
from Text_Class import *
from UI_Button_Class import *

#screen#

SCREEN_WIDTH = 1280
MAP_WIDTH = 3000
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
####################

#game name: Not Alone
#        * But Together

#---------game-variables------------#



game = Game()


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


####map####

### background ###

background = pygame.image.load("Assets\Map\Background\Dungeon_brick_wall_grey.png").convert_alpha()
background = pygame.transform.scale(background, (1280, 450))

background_surface = background; background_surface.set_alpha(200)


## ### ##

#game.create_and_update_objects(MAP_WIDTH, SCREEN_HEIGHT, coin_spritesheet, small_lever_off_sprite, small_lever_on_sprite, big_lever_off_sprite, big_lever_on_sprite)

## functions ##

########################

def update_pressure_plates():
    activated_p_p = None

    for pressure_plate in game.pressure_plates:
        player_pos = pygame.math.Vector2(player_2.rect.center)
        plate_pos = pygame.math.Vector2(pressure_plate.rect.center)

        if ((player_2.rect.bottom == pressure_plate.rect.top) and (player_2.on_something == True)) and (player_pos.distance_to(plate_pos) < 100):
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
    if game.platform_2_plate.activated == True or game.lever_1.on == True:
        if (game.wall_under_platform_2.start_position_y - game.wall_under_platform_2.y) < 150:
            game.wall_under_platform_2.y -= 5; game.wall_under_platform_2.rect.y = game.wall_under_platform_2.y
    else:
        if (game.wall_under_platform_2.start_position_y - game.wall_under_platform_2.y) > 0:
            game.wall_under_platform_2.y += 5; game.wall_under_platform_2.rect.y = game.wall_under_platform_2.y

    if (game.lever_1.on != True and game.lever_2.on != True and game.lever_3.on == True) or game.plate_2.activated == True:
        if (game.wall_3_above.start_position_y - game.wall_3_above.y) > -130:
            game.wall_3_above.y += 5; game.wall_3_above.rect.y = game.wall_3_above.y
    else:
        if (game.wall_3_above.start_position_y - game.wall_3_above.y) < 0:
            game.wall_3_above.y -= 5; game.wall_3_above.rect.y = game.wall_3_above.y
    
    if game.lever_1.on != True and game.lever_2.on == True and game.lever_3.on != True:
        if (game.platform_6_extension.x - game.platform_6_extension.start_position_x) <= 90:
            game.platform_6_extension.x += 5; game.platform_6_extension.rect.x = game.platform_6_extension.x

            if player_2.rect.colliderect(game.platform_6_extension.rect):
                player_2.x += 5
                player_2.rect.x = player_2.x
            
            #its pretty much impossible for player_1 to collide with the platform because of its speed and becauce player_1 is the one that activates it 
            #but i'll still check it just to be safe
            
            if player_1.rect.colliderect(game.platform_6_extension.rect):
                player_1.x += 5
                player_1.rect.x = player_1.x
    else:
        if (game.platform_6_extension.x - game.platform_6_extension.start_position_x) > 0:
            game.platform_6_extension.x -= 5; game.platform_6_extension.rect.x = game.platform_6_extension.x

    if (game.lever_1.on == True and game.lever_2.on == True and  game.lever_3.on == True) or  game.lever_4.on == True:
        if (game.wall_4.start_position_y - game.wall_4.y) < 200:
            game.wall_4.y -= 5; game.wall_4.rect.y = game.wall_4.y
    else:
        if  (game.wall_4.start_position_y -  game.wall_4.y) > 0:
                game.wall_4.y += 5;  game.wall_4.rect.y =  game.wall_4.y

        for player in [player_1, player_2]:
            if player.rect.colliderect(game.wall_4.rect) and player.rect.bottom >  game.wall_4.rect.bottom:
                game.mode = "game: experiment failed"
                
        

    if  game.plate_3.activated == True and  game.lever_5.on != True and  game.lever_6.on == True:
        if ( game.wall_5_upper_part.y -  game.wall_5_upper_part.start_position_y) < 200:
                game.wall_5_upper_part.y += 5;  game.wall_5_upper_part.rect.y =  game.wall_5_upper_part.y
    else:
        if ( game.wall_5_upper_part.y -  game.wall_5_upper_part.start_position_y) > 0:
                game.wall_5_upper_part.y -= 5;  game.wall_5_upper_part.rect.y =  game.wall_5_upper_part.y

    if game.lever_5.on == True and game.lever_6.on != True and game.plate_4.activated == True:
        if (game.wall_5_under_part.start_position_y - game.wall_5_under_part.y) < 200:
            game.wall_5_under_part.y -= 5; game.wall_5_under_part.rect.y =  game.wall_5_under_part.y
    else:
        if (game.wall_5_under_part.start_position_y - game.wall_5_under_part.y) > 0:
            game.wall_5_under_part.y += 5; game.wall_5_under_part.rect.y = game.wall_5_under_part.y

    if game.plate_5.activated == True and game.lever_9.on == True and game.lever_8.on != True:
        if (game.wall_7.start_position_y - game.wall_7.y) < 100:
            game.wall_7.y -= 5; game.wall_7.rect.y = game.wall_7.y
        if (game.platform_12.x - game.platform_12.start_position_x) < 150:
            game.platform_12.x += 7.5; game.platform_12.rect.x = game.platform_12.x

    if ((game.lever_8.on == True) and (game.lever_9.on == True) and (game.lever_10.on == True) and (player_1.coins_collected == len(game.coins)) and (game.plate_5.activated != True) and (game.plate_4.activated != True)) or game.plate_6.activated == True:
        if (game.wall_6.start_position_y - game.wall_6.y) < 150:
            game.wall_6.y -= 5; game.wall_6.rect.y = game.wall_6.y
    else:
        if (game.wall_6.start_position_y - game.wall_6.y) > 0:
            game.wall_6.y += 5; game.wall_6.rect.y = game.wall_6.y

def button_effects():
    if to_menu_button.activated == True:
        game.mode = "menu"

    if info_button.activated == True:
        screen.blit(info_surface, (100, 70))

        screen.blit(player_1_info_page_sprite, (100, 170))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(360, 160, 10, 500))
        screen.blit(player_2_info_page_sprite, (390, 170))

        pygame.draw.rect(screen, (0,0,0), pygame.Rect(710, 70, 10, 620))

        screen.blit(small_lever_off_sprite, (800, 100))

        #pygame.draw.rect(screen, (0,0,0), pygame.Rect(950, 70, 10, 130))

        screen.blit(big_lever_off_sprite, (1000, 92))

        pygame.draw.rect(screen, (0,0,0), pygame.Rect(720, 390, 460, 10))

        

        for text in info_page_text:
            text.display_text(screen)



# experiment failed - player took damage

def failed_or_not():
    if player_1.y > 720 or player_1.y < 0 or player_2.y > 720 or player_2.y < 0:
        game.mode = "game: experiment failed"
    

#camera#

def camera(player_1, player_2, platforms, horizontally_moving_platforms,SCREEN_WIDTH):
    middle_xcor = (player_1.x + player_2.x) /2

    deadzone = 50

    if (middle_xcor > (((SCREEN_WIDTH)/2) + deadzone)) and game.wall_right.rect.x > 1400:
        move = -5
    elif (middle_xcor < (((SCREEN_WIDTH)/2) - deadzone)) and game.wall_left.rect.x < 0:
        move = 5
    else:
        move = 0

    for platform in game.platforms:
        platform.x += move
    for object in game.non_collideable_objects:
        object.x += move; object.rect.x = object.x
    for horizontally_moving_platform in game.horizontally_moving_platforms:
        horizontally_moving_platform.start_position_x += move; horizontally_moving_platform.x += move; horizontally_moving_platform.rect.x = horizontally_moving_platform.x 

    player_1.x += move; player_1.rect.x = player_1.x
    player_2.x += move; player_2.rect.x = player_2.x

###### info/controls #######
info_surface = pygame.Surface((1080, 620)); info_surface.set_alpha(210); info_surface.fill((0,0,0))

player_1_info_page_sprite = player_1.animations["idle"]["frames"]["right"][0]

player_2_info_page_sprite = player_2.animations["idle"]["frames"]["left"][0]

#player1 info/controls

info_page_text_1 = text(110, 70, "INFORMATION/CONTROLS:", 30, (255,255,255))

info_page_text_2 = text(130, 150, "Player 1", 25, (150,20,150))

info_page_text_3 = text(120, 300, "Stats:", 25, (150,20,150))

info_page_text_4 = text(120, 350, "Speed: 6/10", 15, (150,20,150))

info_page_text_5 = text(120, 380, "Strength: 10/10", 15, (150,20,150))

info_page_text_6 = text(120, 410, "Weight Class: Light", 15, (150,20,150))

info_page_text_7 = text(120, 440, "Can Activate Levers?: Yes", 15, (150,20,150))

info_page_text_8 = text(120, 470, "Controls:", 25, (150,20,150))

info_page_text_9 = text(120, 520, "W - Jump", 15, (150,20,150))

info_page_text_10 = text(120, 550, "A - Left", 15, (150,20,150))

info_page_text_11 = text(120, 580, "D - Right", 15, (150,20,150))

info_page_text_12 = text(120, 610, "E - Interact", 15, (150,20,150))
#################################

#player2#
info_page_text_13 = text(410, 150, "Player 2", 25, (100,170,50))

info_page_text_14 = text(400, 300, "Stats:", 25, (100,170,50))

info_page_text_15 = text(400, 350, "Speed: 10/10", 15, (100,170,50))

info_page_text_16 = text(400, 380, "Strength: 5/10", 15, (100,170,50))

info_page_text_17 = text(400, 410, "Weight Class: Heavy", 15, (100,170,50))

info_page_text_18 = text(400, 440, "Can Activate Pressure Plates?: Yes", 15, (100,170,50))

info_page_text_19 = text(400, 470, "Controls:", 25, (100,170,50))

info_page_text_20 = text(400, 520, "Up Arrow - Jump", 15, (100,170,50))

info_page_text_21 = text(400, 550, "Left Arrow - Left", 15, (100,170,50))

info_page_text_22 = text(400, 580, "Right Arrow - Right", 15, (100,170,50))


#levers#
info_page_text_23 = text(750, 70, "Levers:", 25, (150,20,150))

info_page_text_24 = text(760, 170, "- Toggleable", 15, (150,20,150))

info_page_text_25 = text(970, 170, "- Non Toggleable", 15, (150,20,150))

info_page_text_26 = text(820, 200, "Can only be activated by Player 1", 15, (150,20,150))

#pressure plates and coins#

info_page_text_27 = text(750, 250, "Pressure Plates And Coins:", 25, (100,170,50))

info_page_text_28 = text(750, 300, "Can only be activated or collected by Player 2", 15, (100,170,50))

info_page_text_29 = text(750, 330, "For Pressure Plates:", 20, (100,170,50))

info_page_text_30 = text(750, 360, "Red means not activated and blue means activated", 15, (100,170,50))

#######
#info about passages#

info_page_text_31 = text(750, 400, "How To Open Passages?", 25, (255,255,255))

info_page_text_32 = text(750, 440, "By:", 20, (255,255,255))

info_page_text_33 = text(780, 470, "- Activating certain levers", 15, (255,255,255))

info_page_text_34 = text(780, 500, "- Activating certain levers + a pressure plate", 15, (255,255,255))

info_page_text_35 = text(780, 530, "- Activating certain levers + having collected", 15, (255,255,255))
info_page_text_36 = text(790, 550, " a certain amount of coins", 15, (255,255,255))
#####
info_page_text = [info_page_text_1, info_page_text_2, info_page_text_3, info_page_text_4, info_page_text_5, info_page_text_5, info_page_text_6, info_page_text_7, info_page_text_8, info_page_text_9,
info_page_text_10, info_page_text_11, info_page_text_12, info_page_text_13, info_page_text_14, info_page_text_15, info_page_text_16, info_page_text_17, info_page_text_18, info_page_text_19,
info_page_text_20, info_page_text_21, info_page_text_22, info_page_text_23, info_page_text_24, info_page_text_25, info_page_text_26, info_page_text_27, info_page_text_28, info_page_text_29,
info_page_text_30, info_page_text_31, info_page_text_32, info_page_text_33, info_page_text_34, info_page_text_35, info_page_text_36]




###### ending ###########

#good ending
good_ending_surface_alpha = 0
good_ending_surface = pygame.Surface((1280, 720)); info_surface.set_alpha(200); info_surface.fill((0,0,0))

good_ending_text_1 = text(325, 250, "EXPERIMENT SUCCESFUL", 50, (0,255,0))

#############

bad_ending_text_1 = text(500, 150, "0x0000009C", 40, (255,0,0))
bad_ending_text_2 = text(385, 250, "EXPERIMENT FAILED", 50, (255,0,0))

alarm_sound = pygame.mixer.Sound(r"Assets\Audio\freesound_community-emergency-alarm-69780.mp3")
alarm_on = False

###########################
#button sprites#

to_menu = pygame.image.load(r"Assets\User_Interface\ToMenu 16x16.png").convert_alpha()
to_menu = pygame.transform.scale(to_menu, (55, 55))

to_menu_pressed = pygame.image.load(r"Assets\User_Interface\ToMenuPressed 16x16.png").convert_alpha()
to_menu_pressed = pygame.transform.scale(to_menu_pressed, (55, 55))

info = pygame.image.load(r"Assets\User_Interface\Information 16x16.png").convert_alpha()
info = pygame.transform.scale(info, (55, 55))

info_pressed = pygame.image.load(r"Assets\User_Interface\InformationPressed 16x16.png").convert_alpha()
info_pressed = pygame.transform.scale(info_pressed, (55, 55))

##########################3

to_menu_button = ui_button(10, 10, to_menu, to_menu_pressed)

info_button = ui_button(80, 10, info, info_pressed)

ui_buttons_while_game = [to_menu_button, info_button]
ui_buttons_while_game_end = [to_menu_button]
ui_buttons_while_menu = []

################################################################

while game.on == True:

    #resetting alpha for ending screen#
    ending_surface_alpha = 0


    # resetting sounds #
    pygame.mixer.Sound.stop(alarm_sound)
    alarm_on = False

    ####################
    # resetting buttons #

    to_menu_button.activated = False
    info_button.activated = False



    ########################

    game.create_and_update_objects(MAP_WIDTH, SCREEN_HEIGHT, coin_spritesheet, small_lever_off_sprite, small_lever_on_sprite, big_lever_off_sprite, big_lever_on_sprite)
    for coins in game.coins:
        coins.get_coin_animation(coin_spritesheet, 14)
        


    ###################################################################################

    while game.mode == "menu":

        screen.fill((255,255,255))


        pygame.display.update()
        clock.tick(120)


        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                exit()




    while game.mode == "game: running":

        screen.fill((255,255,255))

        screen.blit(background_surface, (0,0))

            ###################################

        #setting player_1 direction to None if they are holding down e for a non toggleable lever so they can't move during that period
        for lever_ in game.levers:
            if lever_.on == True and lever_.toggleable != True:
                player_1.direction = None

        #################################

        player_1.movemenet_collision_gravity(game.platforms)
        player_1.animation(screen)


        for l in game.levers:
            screen.blit(l.sprite, (l.x, l.y))


        player_2.animation(screen)
        player_2.movemenet_collision_gravity(game.platforms)

        failed_or_not()

        update_pressure_plates()

        pressure_plate_and_lever_effects()

        camera(player_1, player_2, game.platforms, game.horizontally_moving_platforms,SCREEN_WIDTH)

        ##################################

        for p_p in game.pressure_plates:
            pygame.draw.rect(screen, p_p.colour, p_p)

        for p in game.platforms_for_drawing:
            pygame.draw.rect(screen, p.colour, p)

        if player_1.rect.colliderect(game.rect_for_checking_completion):
            player_1.collided_with_completion_rect = True
        if player_2.rect.colliderect(game.rect_for_checking_completion):
            player_2.collided_with_completion_rect = True

        print(f"{player_1.collided_with_completion_rect} and {player_2.collided_with_completion_rect}")


    ##############################################
        pygame.draw.rect(screen, game.floor.colour, game.floor)
        pygame.draw.rect(screen, game.grass.colour, game.grass)
        pygame.draw.rect(screen, game.roof.colour, game.roof.rect)
    ####################################################

        for coin in game.coins:
            coin.animate(screen)
            
        player_2.collect_coins(game.coins)

        display_number_of_coins = display_number_of_coins_font.render(f"Coins: {player_2.coins_collected} / {game.total_coins}", True, (0,0,0))
        screen.blit(display_number_of_coins, (5, 650))


        ##################################
        #buttons#

        for b in ui_buttons_while_game:
            screen.blit(b.current_sprite, (b.x, b.y))
            
        button_effects()

                #ending fade#
        if player_1.collided_with_completion_rect == True and player_2.collided_with_completion_rect == True:
            good_ending_surface.set_alpha(ending_surface_alpha)
            screen.blit(good_ending_surface, (0,0))
            ending_surface_alpha += 5
            if ending_surface_alpha == 255:
                game.mode = "game: end"



        #################################

        pygame.display.update()
        clock.tick(120)
        for event in pygame.event.get():


            if event.type == pygame.KEYDOWN:
                #move#
                if event.key == pygame.K_d: player_1.direction = "Right"
                if event.key == pygame.K_a: player_1.direction = "Left"

                #interact#
                if event.key == pygame.K_e:
                    for lever in game.levers:
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
                    for lever in game.levers:
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




            ######## #ui buttons # ###########

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for b in ui_buttons_while_game:
                        b.update_sprite()
            
            if event.type == pygame.MOUSEBUTTONUP:
                #if pygame.mouse.get_pressed()[0]:
                for b in ui_buttons_while_game:
                    b.update_sprite_and_state()



            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    while game.mode == "game: end":

        screen.fill((0,0,0))

        good_ending_text_1.display_text(screen)


        for b in ui_buttons_while_game_end:
            screen.blit(b.current_sprite, (b.x, b.y))

        button_effects()


        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for b in ui_buttons_while_game_end:
                        b.update_sprite()
            
            if event.type == pygame.MOUSEBUTTONUP:
                #if pygame.mouse.get_pressed()[0]:
                for b in ui_buttons_while_game_end:
                    b.update_sprite_and_state()


            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    while game.mode == "game: experiment failed":


        screen.fill((0,0,0))

        for b in ui_buttons_while_game_end:
            screen.blit(b.current_sprite, (b.x, b.y))
        

        bad_ending_text_1.display_text(screen)
        bad_ending_text_2.display_text(screen)

        button_effects()

        if alarm_on == False:
            pygame.mixer.Sound.play(alarm_sound)
            alarm_on = True

        pygame.display.update()
        clock.tick(120)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for b in ui_buttons_while_game_end:
                        b.update_sprite()
            
            if event.type == pygame.MOUSEBUTTONUP:
                #if pygame.mouse.get_pressed()[0]:
                for b in ui_buttons_while_game_end:
                    b.update_sprite_and_state()


            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
