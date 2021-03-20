import pygame
from pygame.locals import *
pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('4th_game')


# define colours
bg = (234, 218, 184)



run = True
while run:
    
    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

