import pygame, os
pygame.init()


width, height = 1400, 800
screen = pygame.display.set_mode((width, height))
f_width = 60
f_height = 60
pygame.display.set_caption("GAME")
bg = (255, 200, 0)
fps = (60)
clock = pygame.time.Clock()
velocity = 5
class FIGHTERS:
    def __init__(self):
        self.red_fighter = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
        self.red_fighter = pygame.transform.scale(self.red_fighter, (f_width, f_height))
        self.red_fighter = pygame.transform.rotate(self.red_fighter, 90)

        self.yellow_fighter = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png")).convert_alpha()
        self.yellow_fighter = pygame.transform.scale(self.yellow_fighter, (f_width, f_height))
        self.yellow_fighter = pygame.transform.rotate(self.yellow_fighter, -90)

        self.red = pygame.Rect(100 - f_width, height/2 - f_height/2, f_width, f_height)
        self.yellow = pygame.Rect(width - 100, height / 2 - f_height / 2, f_width, f_height)


    def draw_red_fighter(self):
        screen.blit(self.red_fighter, self.red)



        # screen.blit(self.red_fighter, (10, 10))
        # pygame.Rect(x,y,w,h) >> creating a rectangle
        # pygame.draw.rect(self.red_fighter,(200,202,200),red)


    def draw_yellow_fighter(self):

        screen.blit(self.yellow_fighter, self.yellow)

    def draw_fighters(self):
        self.draw_red_fighter()
        self.draw_yellow_fighter()


    def move_fighters(self):
        pass
    def draw_block(self):

        screen_splitter = pygame.Rect(width/2 - 10, 0, 20, height)
        pygame.draw.rect(screen, (200, 0, 0), screen_splitter)







fighters = FIGHTERS()

run = True
while run == True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and fighters.red.y - velocity > 0:  # UP
        fighters.red.y -= velocity
    if keys_pressed[pygame.K_s] and fighters.red.y + velocity < height - 60:  # DOWN
        fighters.red.y += velocity
    if keys_pressed[pygame.K_d] :  # RIGHT
        fighters.red.x += velocity
    if keys_pressed[pygame.K_a] :  # LEFT
        fighters.red.x -= velocity

    # keys_pressed[pygame.K_a]
    screen.fill((200, 100, 10))
    fighters.draw_fighters()
    fighters.draw_block()
    pygame.display.update()

