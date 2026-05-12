import pygame

class coin:
    def __init__(self, x, y, sprite):
    
        self.x = x
        self.y = y


        self.current_sprite = sprite

        self.rect = sprite.get_rect()
        

        self.frame_number = 1

        self.change_anim_after_ms = None

        self.ms = 0

        self.frames = []

    def get_coin_animation(self, spritesheet, frames):
        for frame in range(frames):
            frame = spritesheet.subsurface(((frame*16, 0, 16, 16)))
            frame = pygame.transform.scale(frame, (50,50))
            self.frames.append(frame)   

        
    def animate(self, screen):
        self.rect.x = self.x; self.rect.y = self.y

        self.change_anim_after_ms = 120//len(self.frames)

        self.current_sprite = self.frames[self.frame_number]

        screen.blit(self.current_sprite, (self.x, self.y))


        if self.change_anim_after_ms == self.ms:
            self.frame_number += 1
            self.ms = 0

            if len(self.frames) == self.frame_number:
                self.frame_number = 0

        self.ms += 1
        
    



        


    