import pygame
from Player_Class import *
from Platform_Class import *
from Coin_Class import *
from Lever_Class import *
from Pressure_Plates_Class import *

class Game:
    def __init__(self):
        self.on = True

        self.mode = "game: running"

        self.modes = ["game: running", "game: experiment failed", "game: end", "menu"]



    def create_and_update_objects(self, MAP_WIDTH, SCREEN_HEIGHT, coin_spritesheet, small_lever_off_sprite, small_lever_on_sprite, big_lever_off_sprite, big_lever_on_sprite):


        ##################


        self.floor = platform(MAP_WIDTH + 2000, 270, 0, 450, (150,75,0))
        self.grass = platform(MAP_WIDTH + 2000, SCREEN_HEIGHT - 710, 0, 450, (0,100,0))
        self.roof = platform(MAP_WIDTH, 5, 0,0, (0,0,0))

        self.wall_left = platform(20, SCREEN_HEIGHT + 100, 0, -100, (10,10,10))

        ###############3

        self.platform_1 = platform(200, 20, 0, 320, (0,0,0))

        self.platform_2 = platform(300, 22.5, 340, 150, (0,0,0))

        self.platform_2_plate = pressure_plate(400, 140)

        self.coin_1 = coin(500, 100, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.wall_under_platform_2 = platform(20, 300, 620, 150, (0,0,0)) #wall_1
        self.wall_above_platform_2 = platform(20, 300, 620, -150, (0,0,0)) #wall_2

        ###############

        self.wall_3_below = platform(20, 320, 850, 130, (0,0,0))
        self.wall_3_above = platform(20, 130, 850, 0, (0,0,0))

        self.lever_1 = lever(740, 395, small_lever_off_sprite, small_lever_on_sprite,"lever_1", True)

        self.platform_3 = platform(90, 20, 760, 320, (0,0,0))
        self.platform_4 = platform(80, 10, 620, 220, (0,0,0))
        self.platform_5 = platform(90,20, 760, 130, (0,0,0))

        self.lever_2 = lever(780, 265, small_lever_off_sprite, small_lever_on_sprite,"lever_2", True)

        self.coin_2 = coin(650, 170, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.lever_3 = lever(780, 65, big_lever_off_sprite, big_lever_on_sprite,"lever_3", False)

        ###########

        self.platform_6 = platform(100, 20, 870, 200, (0,0,0))
        self.platform_6_extension = platform(100, 20, 870, 200, (0,0,0))

        self.plate_2 = pressure_plate(900,440)

        self.coin_3 = coin(900, 220, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.wall_4 = platform(20, 250, 970, 200, (0,0,0))

        self.lever_4 = lever(1100, 385, big_lever_off_sprite, big_lever_on_sprite,"lever_4", False)

        self.platform_7 = platform(200, 20, 1200, 300, (0,0,0))

        self.platform_8 = platform(200, 20, 1200, 100, (0,0,0))

        self.lever_5 = lever(1220, 45, small_lever_off_sprite, small_lever_on_sprite,"lever_5", True)

        self.lever_6 = lever(1330, 45, small_lever_off_sprite, small_lever_on_sprite,"lever_6", True)

        self.coin_4 = coin(1270, 250, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.platform_9 = platform(250, 20, 1700, 200, (0,0,0))

        self.plate_3 = pressure_plate(1800, 190)

        self.coin_5 = coin(1800, 220, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.coin_6 = coin(1800, 20, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.wall_5_upper_part = platform(20, 200, 1950, 0, (0,0,0))
        self.wall_5_under_part = platform(20, 250, 1950, 200, (0,0,0))

        ###################
        self.plate_4 = pressure_plate(2050, 440)

        self.wall_6 = platform(20, 450, 3000, 0, (0,0,0))

        self.platform_10 = platform(200, 20, 1950, 200, (0,0,0))

        self.lever_7 = lever(2000, 150, small_lever_off_sprite, small_lever_on_sprite,"lever_7", True)

        self.platform_11 = platform(150, 20, 2400, 300, (0,0,0))

        self.plate_5 = pressure_plate(2455, 290)

        self.coin_7 = coin(2450, 100, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.coin_8 = coin(2900, 50, pygame.transform.scale(coin_spritesheet.subsurface(0,0,16,16), (50,50)))

        self.lever_8 = lever(2035, 145, small_lever_off_sprite, small_lever_on_sprite,"lever_8", True)

        self.lever_9 = lever(2450, 385, big_lever_off_sprite, big_lever_on_sprite,"lever_9", False)

        self.wall_7 = platform(20, 100, 2850, 0, (0,0,0))

        self.platform_12 = platform(150, 20, 2850, 100, (0,0,0))

        self.lever_10 = lever(2850, 395, small_lever_off_sprite, small_lever_on_sprite,"lever_10", True)

        self.plate_6 = pressure_plate(3100, 440)

        self.wall_right = platform(20, 720, 5000, 0, (0,0,0))

        ###############33

        self.exit_roof = platform(2000, 300, 3000, 0, (0,0,0))



        self.platforms = [self.floor.rect, self.grass.rect, self.roof.rect ,self.wall_left.rect, self.platform_1.rect, self.platform_2.rect, self.platform_2_plate.rect, self.wall_under_platform_2.rect, self.wall_above_platform_2.rect,
        self.wall_3_below.rect, self.wall_3_above.rect, self.platform_3.rect, self.platform_4.rect, self.platform_5.rect, self.platform_6.rect, self.platform_6_extension.rect, self.plate_2.rect, self.wall_4.rect, self.platform_7.rect, self.platform_8.rect, self.platform_9.rect, 
        self.wall_5_upper_part.rect, self.wall_5_under_part.rect, self.plate_3.rect, self.wall_6.rect, self.plate_4.rect, self.platform_10.rect, self.platform_11.rect, self.plate_5.rect, self.wall_7.rect, self.platform_12.rect, self.exit_roof.rect, self.plate_6.rect, self.wall_right.rect]
        
        self.horizontally_moving_platforms = [self.platform_6_extension, self.platform_12]

        self.platforms_for_drawing = [self.floor, self.grass, self.roof, self.wall_left, self.platform_1, self.platform_2, self.wall_under_platform_2, self.wall_above_platform_2,
        self.wall_3_below, self.wall_3_above, self.platform_3, self.platform_4, self.platform_5, self.platform_6, self.platform_6_extension, self.wall_4, self.platform_7, self.platform_8, self.platform_9, 
        self.wall_5_upper_part, self.wall_5_under_part, self.wall_6, self.platform_10, self.platform_11, self.wall_7, self.platform_12, self.exit_roof, self.wall_right]

        self.horizontally_moving_platforms = [self.platform_6_extension, self.platform_12]

        self.pressure_plates = [self.platform_2_plate, self.plate_2, self.plate_3, self.plate_4, self.plate_5, self.plate_6]

        self.non_collideable_objects = [self.lever_1, self.coin_1, self.lever_2, self.coin_2, self.lever_3, self.coin_3, self.lever_4, self.lever_5, self.lever_6, self.coin_4, self.coin_5, self.coin_6, self.coin_7, self.coin_8, self.lever_8, self.lever_9, self.lever_10]

        self.levers = [self.lever_1, self.lever_2, self.lever_3, self.lever_4, self.lever_5, self.lever_6, self.lever_7, self.lever_8, self.lever_9, self.lever_10]
        self.coins = [self.coin_1, self.coin_2, self.coin_3, self.coin_4, self.coin_5, self.coin_6, self.coin_7, self.coin_8]

        self.total_coins = len(self.coins)
