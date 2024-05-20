# -*- coding: utf-8 -*-
import os
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        self.sheet = pygame.image.load(os.path.join("spritesheet", "gameImages","bunny-Sheet.png"))
        
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(331, 500, 93, 90))
        self.frontalRect = pygame.Rect(380, 100, 20, 50)#535
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        #position image in the screen surface
        self.rect.topleft = position
        
        #variable for looping the frame sequence
        self.frame = 0

        #jump variables
        self.jump_power_setting = 19
        self.jump_power = self.jump_power_setting
        self.onGround = False
        self.gravity = 1
        self.is_jumping = False
        self.frame_delay = 20
        self.yvel = 19
        self.prevY = self.rect.y
        self.level_number = 0
        
        self.rectWidth = 93
        self.rectHeight = 90
        #variables for falling
        self.is_falling = False
        #variables for dying
        self.dead = False
        self.has_won = False
        #Animation clips from Caveman Sprite sheet - will change
        self.down_states = { 0: (0, 0, self.rectWidth,  self.rectHeight), 1: (126, 0, self.rectWidth,  self.rectHeight), 2: (252, 0, self.rectWidth,  self.rectHeight), 3:(378, 0, self.rectWidth,  self.rectHeight) }      
          
         
        self.up_states = (336, 350, self.rectWidth,self.rectHeight)

        self.right_states = { 0: (331, 500, self.rectWidth,  self.rectHeight), 1: (224, 500, self.rectWidth, self.rectHeight), 2: (338, 349, self.rectWidth,self.rectHeight), 3: (225, 349, self.rectWidth,self.rectHeight), 4: (118, 353, self.rectWidth, self.rectHeight), 5: (6, 353, self.rectWidth, self.rectHeight) }
        self.dead_state = (225, 201, 95, 90)

        
    def get_frame(self, frame_set):
        #looping the sprite sequences.
        self.frame += 1
        
        #if loop index is higher that the size of the frame return to the first frame 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        #print(frame_set[self.frame])
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def calcYVelocity(self):
        self.yvel = self.jump_power
        print("YVel : " + str(self.yvel))
    def update(self, direction):
        
        if not (self.dead)and not(self.is_jumping):
            self.clip(self.right_states)
        if (self.dead):
            self.clip(self.dead_state)
            
        if self.is_jumping:
            print("Changed Power")
            self.clip(self.up_states)
            self.rect.y -= self.jump_power
            self.frontalRect.y -= self.jump_power
            self.jump_power -= self.gravity
        if self.onGround:
            self.is_jumping = False
            self.is_falling = False
            self.jump_power = self.jump_power_setting
        if not(self.onGround) and not(self.is_jumping):
            self.is_falling = True
        if self.is_falling:
            self.rect.y += 10
            self.frontalRect.y +=10
        #if self.dead:
            
        #Attempt to slow down framerate of animation - needs work

        

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    #Recives on ground notification from main, updates boolean
    def get_onGround(self,  state):
        self.onGround = state

    #Now this really just controls jump
    #need to add in jump animation
    def handle_event(self, event):
        self.update('right')
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and not self.is_jumping:
                self.jump_power=self.jump_power_setting
                self.update('up')
                self.is_jumping = True

            