import pygame, sys
from pygame.math import Vector2
class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)


    def draw_fruit(self):
        # create a rectangle
        # draw the rectangle




pygame.init()
cell_size = 40
cell_number = 20
width = 500
height = 600
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * ce ll_size))
pygame.display.set_caption('SNAKE')
bg = (234, 218, 184)

clock = pygame.time.Clock()
FPS = 60






run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    screen.fill(bg)
    pygame.display.update()
    clock.tick(FPS)

