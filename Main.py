import pygame, sys, random
from Player_Class import *
#screen#

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
####################

#---------game-variables------------#

game = True


#-----------players-----------#

'''class player: 
    def __init__(self, player_sprite,x,y):
        self.speed = 2
        self.sprite = player_sprite
        self.rect = pygame.Rect(x,y, 40,50)'''


pygame.init()

player_1 = player(None,400,400)


#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))

while game == True:

    #level 1

    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0,450, SCREEN_WIDTH + 0, SCREEN_HEIGHT-450))
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(0,450, SCREEN_WIDTH + 0, SCREEN_HEIGHT-710))
    pygame.draw.rect(screen, (0,0,0), player_1.rect)
    
    ###################################
 

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()