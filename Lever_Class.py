import pygame

class lever:
    def __init__(self, x, y, sprite_off, sprite_on, name, T_or_F):

        self.name = name

        self.x = x
        self.y = y

        self.on = False

        self.button_pressed = False # to avoid fast toggling 
        
        self.sprite_off = sprite_off
        self.sprite_on = sprite_on

        lever.toggleable = T_or_F #if True - the lever is slightly smaller and can be left toggled. If False - the lever is slightly bigger and can not be left toggled.

        self.sprite = sprite_off

    
        
        self.rect = self.sprite.get_rect()
        self.rect.x = self.x; self.rect.y = self.y
        #self.rect = pygame.Rect(x, y, 20, 20)

    def update_lever_sprite_based_on_state(self):
        if self.on != True:
            self.sprite = self.sprite_off
        elif self.on == True:
            self.sprite = self.sprite_on

        