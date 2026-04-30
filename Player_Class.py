import pygame

class player: 
    def __init__(self, player_sprite,x,y):
        self.speed = 2
        self.sprite = player_sprite
        self.rect = pygame.Rect(x,y, 40,50)