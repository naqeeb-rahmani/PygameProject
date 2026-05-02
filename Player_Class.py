import pygame

class player: 
    def __init__(self, player_sprite, x, y):
        self.speed = 3

        self.jump = False
        self.jump_height = 100
        self.jump_speed = 5
        self.jump_start_saved = False
        self.jump_start = None

        self.animation = {
            "idle": [],
            "walk_right": [],
            "walk_left": [],
            "jump/fall": []

        }
        
        self.on_something = False

        self.fall_speed = 2
        self.gravity = 0.5
        
        self.sprite = player_sprite
        self.x = x; self.y = y  
        self.rect = pygame.Rect(self.x,self.y, 60,100)
        self.direction = None #True = Right and False = Left


    def move(self):
        if self.direction == "Right":
            self.x += self.speed
            self.rect.x = self.x
        elif self.direction == "Left": 
            self.x -= self.speed
            self.rect.x = self.x

    def jump_function(self):

        if self.jump == True:
            if self.jump_start_saved == False:
                self.jump_start = self.y; self.jump_start_saved = True
    
            self.y -= self.jump_speed; self.rect.y = self.y
            if (self.jump_start - self.y) > self.jump_height:
                self.jump = False; self.jump_start = None; self.jump_start_saved = False
        
    def gravity_and_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform):
                self.on_something = True
                self.fall_speed = 0
                start_falling = False
                return
        if self.jump == False:
            start_falling = True
            self.on_something = False
            self.fall_speed += self.gravity
            self.y += self.fall_speed; self.rect.y = self.y
            if self.on_something != True and start_falling != True: self.fall_speed = 2; start_falling = True

    def get_animation(self, animation_name, number_of_frames, animation_sheet, frames_order):
        if frames_order == "left to right":
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((frame_number*48, 0, 48, 48)); frame = pygame.transform.scale(frame, (144, 144)) 
                self.animation[animation_name].append(frame)
        elif frames_order == "right to left":
            width = animation_sheet.get_width()
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((((width -48) -(48*frame_number)), 0, 48, 48));  frame = pygame.transform.scale(frame, (144, 144)) 
                self.animation[animation_name].append(frame)



    def animation(self):
    #    if self.direction == None and self.jump == False:
        pass

