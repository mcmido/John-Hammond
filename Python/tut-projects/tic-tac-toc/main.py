import pygame, sys
pygame.init()

screen = pygame.display.set_mode((400, 400))




run = True
while run == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			sys.exit()


screen.update()