import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
            # create rect
            # draw the rect
            snake_rect = pygame.Rect()

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_number)
        # draw the rectangle
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)




pygame.init()
cell_size = 40
cell_number = 20
width = cell_number * cell_size
height = cell_number * cell_size

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption('SNAKE')
bg = (234, 218, 184)

clock = pygame.time.Clock()
FPS = 60




fruit = FRUIT()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    screen.fill(bg)
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(FPS)

