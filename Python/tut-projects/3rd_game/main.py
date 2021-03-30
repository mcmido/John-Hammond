import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

#Defin Colours
bg = (234, 218, 184)

#Block Colours
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)

#paddle colours
paddle_colour = (142, 135, 123)
paddle_outline = (100, 100, 100)


#define game variables

cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
#brick wall calls

class wall():
	def	__init__(self):
		self.width = screen_width // cols
		self.height = 50
	
	def create_wall(self):
		self.blocks = []
		# define an empty list for an individual block
		block_individual = []
		for row in range(rows):
			#reset the block row list
			block_row = []
			# iterate through each column
			for col in range(cols):
				# generate x and y position for each block and create a rectangle from that
				block_x = col * self.width
				block_y = row * self.height
				rect = pygame.Rect(block_x, block_y, self.width, self.height)
				# assign block strength based on row
				if row < 2:
					strength = 3
				elif row < 4:
					strength = 2
				elif row < 6:
					strength = 1
				#create a list at this point to store the rect and color data	
				block_individual = [rect, strength]
				# append that indidivual block to overall block row
				block_row.append(block_individual)
			#append the row to the full list of blocks
			self.blocks.append(block_row)

	
	def draw_wall(self):
		for row in self.blocks:
			for block in row:
				#assign colour based on block strength
				if block[1] == 3:
					block_colour = block_blue
				elif block[1] == 2:
					block_colour = block_green
				elif block[1] == 1:
					block_colour = block_red

				pygame.draw.rect(screen, block_colour, block[0])
				pygame.draw.rect(screen, bg, (block[0]), 2)



#paddle class
class paddle():
	def __init__(self):
		#define paddle variable
		self.height = 20
		self.width = int(screen_width / cols)
		self.x = int((screen_width / 2) - (self.width / 2))
		self.y = screen_height - (self.height * 2)
		self.speed = 10
		self.rect = Rect(self.x, self.y, self.width, self.height)
		self.direction = 0

	def move(self):
		# reset movment direction
		self.direction = 0

		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= self.speed
			self.direction = -1
		if key[pygame.K_RIGHT] and self.rect.right < screen_width:
			self.rect.x += self.speed
			self.direction = 1

	def draw(self):
		pygame.draw.rect(screen, paddle_colour, self.rect)
		pygame.draw.rect(screen, paddle_outline, self.rect, 3)





# create a wall
wall = wall()
wall.create_wall()

# creat paddle
player_paddle = paddle()



run = True
while run:


	clock.tick(fps)
	
	screen.fill(bg)

	#draw wall
	wall.draw_wall()

	#draw paddle
	player_paddle.draw()

	player_paddle.move()

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()		

pygame.quit()