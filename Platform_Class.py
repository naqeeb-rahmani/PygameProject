import pygame


class platform: 
    def __init__(self, width, height, x, y, colour):

        self.width = width; self.height = height

        self.start_position_y = y

        self.x = x; self.y = y

        self.colour = colour

        self.rect = pygame.Rect(self.x,self.y, self.width,self.height)



    
            

        
