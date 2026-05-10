import pygame


class pressure_plate:
    def __init__(self, x, y):
        self.y_unactivated = y
        self.x = x
        self.y = y

        self.activated = False

        self.colour = (255,0,0)

        self.rect = pygame.Rect(x, y, 50, 10)
    