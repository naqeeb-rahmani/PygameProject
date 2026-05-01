import pygame

class player: 
    def __init__(self, player_sprite, x, y):
        self.speed = 3

        self.jump = False
        self.jump_height = 55
        self.jump_speed = 5
        self.jump_start = None
        
        self.on_something = False

        self.fall_speed = 0
        self.gravity = 0.5
        
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
        if self.jump != True and self.on_something != True:
            self.jump_start = self.y 
        elif self.jump == True and self.on_something == True:
            self.y -= self.jump_speed; self.rect.y = self.y
            if (self.jump_start - self.y) > self.jump_height:
                self.on_something = False; self.jump = False
        
    def gravity_and_collision(self, platform):
        for object in platform:
            if self.rect.colliderect(object):
                self.on_something = True
                self.fall_speed = 0
                return
        self.fall_speed += self.gravity
        self.y += self.fall_speed; self.rect.y = self.y
        self.fall_speed = 2

    def animation(self):
        #if self.direction != 
        pass

