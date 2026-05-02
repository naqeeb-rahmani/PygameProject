import pygame

class player: 
    def __init__(self, player_sprite, x, y):

        self.ms = 0 #for animations because each animation runs 60/second

        self.speed = 3

        self.jump = False
        self.jump_height = 100
        self.jump_speed = 5
        self.jump_start_saved = False
        self.jump_start = None


        self.animations = {
            "idle": {
                "frames": [],
                "number of frames": 10
                },

            "walk_right": {
                "frames": [],
                "number of frames": "idk"
            },

            "walk_left": {
                "frames": [],
                "number of frames": "idk"
            },

            "jump/fall": {
                "frames": [],
                "number of frames": "idk"
            }

        }
        
        self.on_something = False

        self.fall_speed = 2
        self.gravity = 0.5
        
        self.sprite = player_sprite
        self.x = x; self.y = y

        self.player_offset_rect_x = 37; self.player_offset_rect_y = 20
    
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

    def get_animations(self, animation_name, number_of_frames, animation_sheet, frames_order):
        if frames_order == "left to right":
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((frame_number*48, 0, 48, 48)); frame = pygame.transform.scale(frame, (144, 144)) 
                self.animations[animation_name]["frames"].append(frame)
        elif frames_order == "right to left":
            width = animation_sheet.get_width()
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((((width -48) -(48*frame_number)), 0, 48, 48));  frame = pygame.transform.scale(frame, (144, 144)) 
                self.animations[animation_name]["frames"].append(frame)



    def animation(self, screen):
        if self.direction == None and self.on_something == True and self.jump == False: #runs 60x per second
            if self.ms == 60:
                self.ms = 0
            if self.ms <= 6:
                screen.blit(self.animations["idle"]["frames"][0], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 12:
                screen.blit(self.animations["idle"]["frames"][1], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 18:
                screen.blit(self.animations["idle"]["frames"][2], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 24:
                screen.blit(self.animations["idle"]["frames"][3], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 30:
                screen.blit(self.animations["idle"]["frames"][4], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 36:
                screen.blit(self.animations["idle"]["frames"][5], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 42:
                screen.blit(self.animations["idle"]["frames"][6], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 48:
                screen.blit(self.animations["idle"]["frames"][7], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 54:
                screen.blit(self.animations["idle"]["frames"][8], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 60:
                screen.blit(self.animations["idle"]["frames"][9], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))

            self.ms += 1
            
'''    def animation(self, screen):
        if self.direction == None and self.on_something == True: #runs 60x per second

            for frame in self.animation["idle"]:
                run_per_second = 60 / self.animations["idle"]["frames"]
                if 
                screen.blit(self.animations["idle"][frame], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))

                self.ms += 1
                if self.ms == run_per_second *'''

