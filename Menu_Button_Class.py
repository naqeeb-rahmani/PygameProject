import pygame

import pygame

class menu_button:
    def __init__(self, x, y, sprite, sprite_pressed):
        self.x = x
        self.y = y

        self.pressed = False

        self.current_sprite = sprite
        self.sprite_when_not_pressed = sprite
        self.sprite_when_pressed = sprite_pressed


        self.activated = False

        self.rect = pygame.Rect(x, y+40, 180, 70)

    def update_sprite_menu(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.current_sprite = self.sprite_when_pressed
       
    def update_sprite_and_state_menu(self):       
        self.current_sprite = self.sprite_when_not_pressed
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if self.activated != True:
                self.activated = True
            else:
                self.activated = False
        
            