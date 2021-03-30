import pygame, sys
pygame.init()

width = 500
height = 600

screen = pygame.display.set_mode((width,height))
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

