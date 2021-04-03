import pygame
import sys

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ONLINE CLIENT")
clock = pygame.time.Clock()


class BOX:
    def __init__(self):
        self.r_width = 60
        self.r_height = 60
        self.x = width/2 - self.r_width/2
        self.y = height/2 - self.r_height/2
        self.vel = 1

    def move_rect(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y + self.vel > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.vel + self.r_height < height:
            self.y += self.vel
            print("Pressed Down")
        if keys[pygame.K_RIGHT] and self.x + self.vel + self.r_width < width:
            self.x += self.vel
            print("Pressed RIGHT")
        if keys[pygame.K_LEFT] and self.x + self.vel > 0:
            self.x -= self.vel
            print("Pressed LEFT")

    def draw_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.r_width, self.r_height)
        pygame.draw.rect(screen, (20,255,0), self.rect)



main = BOX()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()



    screen.fill((255,255,255))
    main.move_rect()
    main.draw_rect()
    pygame.display.update()




