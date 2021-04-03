import pygame, sys
pygame.init()
width = 500
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Online_Game")
clock = pygame.time.Clock()

class RECT:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.r_width = 60
        self.r_height = 60
        self.vel = 5


    def move_rect(self):
        # Neeeds Tweaking
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.r_height < height:
            self.y += self.vel
        if keys[pygame.K_RIGHT] and self.x + self.vel + self.r_width < width:
            self.x += self.vel
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:
            print(self.x)
            self.x -= self.vel


    def draw_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.r_width, self.r_height)
        pygame.draw.rect(screen, (0,255,0), self.rect)






rect = RECT()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()


    screen.fill((255, 255, 255))
    rect.draw_rect()
    rect.move_rect()
    pygame.display.update()