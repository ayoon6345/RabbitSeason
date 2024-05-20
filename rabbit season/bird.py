# -*- coding: utf-8 -*-
import os
import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, position,*rectangles):
        super().__init__(*rectangles)
        self.rectWidth = 56
        self.rectHeight = 49
        #load image
        self.sheet = pygame.image.load("spritesheet/gameImages/bird.png").convert_alpha()
        
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(125,240,self.rectWidth,self.rectHeight))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        #position image in the screen surface
        self.rect.topleft = position
        self.pos = position
        #variable for looping the frame sequence
        self.frame = 0
        #change the subtraction to change how far up the bird goes
        self.top = self.rect.y-200
        self.bottom = self.rect.y
        self.goingUp = True
        
        self.move_states = { 
            0: (125, 240, self.rectWidth,self.rectHeight), 
            1: (191,245, self.rectWidth,self.rectHeight), 
            2: (257,248, self.rectWidth,self.rectHeight), 
            3: (324,241, self.rectWidth,self.rectHeight)
            }       

        self.interval = 80
        self.last_update = 0

    def get_frame(self, frame_set):
        if pygame.time.get_ticks() - self.last_update > self.interval:
            self.frame += 1
            if((self.rect.y > self.top) or (self.goingUp == False)):
                if(self.goingUp == True):
                    self.rect.y -= 15
                else:
                    if(self.rect.y < self.bottom):
                        self.rect.y += 15
                    else:
                        self.goingUp = True
            else:
                self.goingUp = False
            
            self.last_update = pygame.time.get_ticks()
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self):
        self.clip(self.move_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
