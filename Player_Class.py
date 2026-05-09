import pygame

class player: 
    def __init__(self, x, y):

        self.ms = 0 #for animations because each animation runs 60/second

        self.speed = 5

        self.jump = False
        self.jump_height = 150
        self.jump_speed = 5
        self.jump_start_saved = False
        self.jump_start = None




        self.animations = {
            "idle": {
                "frames": {
                    "right": [],
                    "left" : []
                },
                "number of frames": 10
                },

            "walk" : {
                "frames": {
                    "right" : [],
                    "left" : []
                },
                "number of frames": 8
            },

            "run" : {
                "frames" : {
                    "right" : [],
                    "left" : []
                },
                "number of frames": 8
            },

            "jump": {
                "frames": {
                    "right" : [],
                    "left" : []
                },
                "number of frames": 6
            }

        }
        
        self.on_something = False

        self.fall_speed = 2
        self.reset_fall_speed = False
        self.gravity = 0.5
    
        self.x = x; self.y = y

        self.player_offset_rect_x = 37; self.player_offset_rect_y = 20
    
        self.rect = pygame.Rect(self.x,self.y, 60,100)

        self.direction = None #True = Right and False = Left
        self.last_direction = "right"


    def movemenet_collision_gravity(self, platforms):
        if self.direction == "Right":
            self.x += self.speed
            self.rect.x = self.x
        elif self.direction == "Left": 
            self.x -= self.speed
            self.rect.x = self.x

        for platform in platforms:
            if self.rect.colliderect(platform):
                
                if self.rect.right >= platform.left and self.direction == "Right":
                    self.rect.right = platform.left
                    self.x = self.rect.x
            
                elif self.rect.left <= platform.right and self.direction == "Left":
                    self.rect.left = platform.right
                    self.x = self.rect.x

            

        if self.jump == True:
            if self.jump_start_saved == False:
                self.jump_start = self.y; self.jump_start_saved = True

            self.y -= self.jump_speed; self.rect.y = self.y
            
            if (self.jump_start - self.y) > self.jump_height:
                self.reset_fall_speed = True
                self.jump = False; self.jump_start = None; self.jump_start_saved = False; self.on_something = False

        for platform in platforms:
            if self.rect.colliderect(platform) == False:
                self.on_something = False

        if self.jump == False and self.on_something == False:
            self.fall_speed += self.gravity
            self.y += self.fall_speed; self.rect.y = self.y
            if self.on_something != True and self.reset_fall_speed == True: self.reset_fall_speed = False; self.fall_speed = 2

        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.rect.top <= platform.bottom and self.jump == True:
                    self.jump = False
                    self.rect.top = platform.bottom
                    self.y = self.rect.y
                    self.jump = False

                elif self.rect.bottom >= platform.top and self.fall_speed > 0:
                    self.on_something = True    
                    self.rect.bottom = platform.top
                    self.y = self.rect.y
                    self.reset_fall_speed = True


    def get_animations(self, animation_name, number_of_frames, direction, animation_sheet):
        if direction == "right": frames_order = "left to right"
        else: frames_order = "right to left"

        if frames_order == "left to right":
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((frame_number*48, 0, 48, 48)); frame = pygame.transform.scale(frame, (144, 144)) 
                self.animations[animation_name]["frames"][direction].append(frame)
        elif frames_order == "right to left":
            width = animation_sheet.get_width()
            for frame_number in range(number_of_frames):
                frame = animation_sheet.subsurface((((width -48) -(48*frame_number)), 0, 48, 48));  frame = pygame.transform.scale(frame, (144, 144)) 
                self.animations[animation_name]["frames"][direction].append(frame)



    def animation(self, screen):
        if self.direction == None: direction = self.last_direction.lower()
        else: direction = self.direction.lower()

        if self.direction == None and self.on_something == True and self.jump == False: #runs 60x per second
            if self.ms <= 12:
                screen.blit(self.animations["idle"]["frames"][direction][0], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 24:
                screen.blit(self.animations["idle"]["frames"][direction][1], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 36:
                screen.blit(self.animations["idle"]["frames"][direction][2], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 48:
                screen.blit(self.animations["idle"]["frames"][direction][3], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 60:
                screen.blit(self.animations["idle"]["frames"][direction][4], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 72:
                screen.blit(self.animations["idle"]["frames"][direction][5], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 84:
                screen.blit(self.animations["idle"]["frames"][direction][6], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 96:
                screen.blit(self.animations["idle"]["frames"][direction][7], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 108:
                screen.blit(self.animations["idle"]["frames"][direction][8], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 120:
                screen.blit(self.animations["idle"]["frames"][direction][9], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
        
        elif self.direction != None and self.on_something == True:
            if self.ms <= 15:
                screen.blit(self.animations["run"]["frames"][direction][0], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 30:
                screen.blit(self.animations["run"]["frames"][direction][1], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 45:
                screen.blit(self.animations["run"]["frames"][direction][2], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 60:
                screen.blit(self.animations["run"]["frames"][direction][3], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 75:
                screen.blit(self.animations["run"]["frames"][direction][4], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 90:
                screen.blit(self.animations["run"]["frames"][direction][5], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 105:
                screen.blit(self.animations["run"]["frames"][direction][6], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
            elif self.ms <= 120:
                screen.blit(self.animations["run"]["frames"][direction][7], (self.x-self.player_offset_rect_x, self.y-self.player_offset_rect_y))
        
           
            if self.ms == 120:
                self.ms = 0
            self.ms += 1

    def animation(self, screen):
            if self.direction == None: direction = self.last_direction.lower()
            else: direction = self.direction.lower()
            




'''    def move(self):
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
            if ((self.jump_start - self.y) > self.jump_height):
                self.reset_fall_speed = True
                self.jump = False; self.jump_start = None; self.jump_start_saved = False; self.on_something = False


    def gravity_and_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform):


                if self.rect.left <= platform.right and self.direction == "Left":
                    self.rect.left = platform.right
                    self.x = self.rect.x
                    self.direction = None

                if self.rect.right >= platform.left and self.direction == "Right":
                    self.rect.right = platform.left
                    self.x = self.rect.x

                if self.rect.bottom >= platform.top and self.fall_speed > 0:
                    self.on_something = True    
                    self.rect.bottom = platform.top
                    self.y = self.rect.y
                    self.reset_fall_speed = True

                if self.rect.top >= platform.bottom and self.jump == True:
                    self.jump = False
                    self.rect.top = platform.bottom
                    self.y = self.rect.y
                    self.jump = False
                    

        if self.jump == False and self.on_something == False:
            self.fall_speed += self.gravity
            self.y += self.fall_speed; self.rect.y = self.y
            if self.on_something != True and self.reset_fall_speed == True: self.reset_fall_speed = False; self.fall_speed = 2'''
'''def gravity_and_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.rect.top 


                elf.on_something = True
                self.fall_speed = 0
                start_falling = False
                return

                
        if self.jump == False:
            start_falling = True
            self.on_something = False
            self.fall_speed += self.gravity
            self.y += self.fall_speed; self.rect.y = self.y
            if self.on_something != True and start_falling != True: self.fall_speed = 2; start_falling = True'''
