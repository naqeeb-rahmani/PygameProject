import pygame

class lever:
    def __init__(self, x, y, sprite_off, sprite_on, name):

        self.name = name

        self.x = x
        self.y = y

        self.on = False
        
        self.sprite_off = sprite_off
        self.sprite_on = sprite_on

        self.sprite = sprite_off

    
        
        self.rect = self.sprite.get_rect()
        self.rect.x = self.x; self.rect.y = self.y
        #self.rect = pygame.Rect(x, y, 20, 20)

    def update_lever_sprite_based_on_state(self):
        if self.on != True:
            self.sprite = self.sprite_off
        elif self.on == True:
            self.sprite = self.sprite_on

        