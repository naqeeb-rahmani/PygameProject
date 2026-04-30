import pygame

class player: 
    def __init__(self, player_sprite, x, y):
        self.speed = 3

        self.jump = False
        self.jump_height = 30
        self.jump_speed = 2.5
        self.jump_start = None
        
        self.fall_speed = 2
        self.gravity = 0.2
        
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

    def jump_function(self):
        if self.jump != True:
            self.jump_start = self.y 
        elif self.jump == True:
            self.y -= self.jump_speed; self.rect.y = self.y
            if (self.jump_start - self.y) > self.jump_height:
                self.jump_start = None; self.jump = False

        
    def gravity_function(self):
        self.fall_speed += self.gravity
        self.y += self.fall_speed; self.rect.y = self.y


''' def jump_function(self):
        if self.jump == True:
            self.y -= self.jump_speed; self.rect.y = self.y #self.rect.y for now because i dont have a sprite yet
            self.jump_speed -= self.gravity
            if self.jump_speed < self.jump_height:
                self.jump = False
                self.jump_speed = self.jump_height'''