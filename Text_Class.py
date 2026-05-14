import pygame

class text:
    def __init__(self, x, y, text, font_size, colour):
        self.x = x
        self.y = y

        self.font = pygame.font.Font("Assets\Font\Grand9K Pixel.ttf", font_size)

        self.text = self.font.render(text, True, colour)

    def display_text(self, screen):
        screen.blit(self.text, (self.x, self.y))

