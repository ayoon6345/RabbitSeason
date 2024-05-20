# -*- coding: utf-8 -*-

import pygame
import player

pygame.init()

screen_width    = 800
screen_height   = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Midterm - Spritesheet character animation")

#set up refresh rate
clock = pygame.time.Clock()

#character position
player = player.Character((400, 200))

#game loop boolean
game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    player.handle_event(event)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
