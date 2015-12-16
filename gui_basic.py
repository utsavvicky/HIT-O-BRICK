import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((610,480))

brick_width = 50
brick_height = 15
paddle_width = 160
paddle_height = 10
ball_diameter = 20
ball_radius = ball_diameter/2
paddle_start = (screen.get_rect().width-paddle_width)/2

def init_brick_flags(n,m):
	#bricks = [[[y,x] for x in range(10)] for y in range(12)]
	flags = [0 for x in range(n*m)]
	return flags


def get_rect_number(x,y,n):
	pos = n*((y/brick_height)) + (x/brick_width)
	return pos


def draw_blocks(flags,n,m):
	WHITE = (250,250,250)
	BLACK = (0,0,0)
	RED = (250,0,0)
	GREEN = (0,250,0)
	BLUE = (0,0,250)

	screen.fill(BLACK)

	y = 0
	for i in range(m):
		x = 0
		for j in range(n):
			if flags[(i*n)+j] == 0:
				pygame.draw.rect(screen, RED, (x,y,brick_width,brick_height))
			x += brick_width+1
		y += brick_height+1

	pygame.draw.rect(screen,BLUE,(paddle_start,screen.get_rect().height-paddle_height,paddle_width,paddle_height))

	# TODO update circle position continuously
	pygame.draw.circle(screen,WHITE,(300,460),ball_radius)

	pygame.display.update()


def run():
	#pos = get_rect_number(133,149,12)
	#flags[pos] = 1
	global paddle_start
	flags = init_brick_flags(12,10)

	while True:
		draw_blocks(flags,12,10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
			if event.type == pygame.KEYDOWN:
				f = 0
				while event.key == pygame.K_LEFT and f==0:
					paddle_start-=1
					draw_blocks(flags,12,10)
					for e in pygame.event.get():
						if e.type == pygame.KEYUP:
							f = 1
							break
					
					if paddle_start<0:
						paddle_start=0
						break
				f=0
				while event.key == pygame.K_RIGHT and f==0:
					paddle_start+=1
					draw_blocks(flags,12,10)
					for e in pygame.event.get():
                                                if e.type == pygame.KEYUP:
                                                        f = 1
                                                        break	
					
					if paddle_start>450:
						paddle_start = 450
						break
					



run()

