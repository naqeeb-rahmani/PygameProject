import pygame

class player: 
    def __init__(self, player_sprite, x, y):
        self.speed = 3
        self.jump_height = 10
        self.gravity = 1
        self.velocity = 10
        self.sprite = player_sprite
        self.x = x; self.y = y  
        self.rect = pygame.Rect(self.x,self.y, 50,60)
        self.direction = None #True = Right and False = Left


    def move(self):
        if self.direction == "Right":
            self.x += self.speed
            self.rect.x = self.x
        elif self.direction == "Left": 
            self.x -= self.speed
            self.rect.x = self.x
        elif self.direction == "Up":
            self.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity = 

        