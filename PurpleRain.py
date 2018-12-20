import pygame_sdl2
from random import *
pygame_sdl2.import_as_pygame
pygame = pygame_sdl2
pygame.init()
win = pygame.display.set_mode((1080, 1920))
rain = []
for i in range(300):
	temp = []
	temp.append(randint(0, 1077))
	temp.append(randint(-200, -100))
	temp.append(randint(4, 10))
	temp.append(randint(4, 8)/10)
	rain.append(temp)
while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
	win.fill((230, 230, 255))
	for i in rain:
		i[1] += i[2]
		i[2] += i[3]
		if i[1] >= 1920:
			i[0] = randint(0, 1077)
			i[1] = randint(-200, -100)
			i[2] = randint(4, 10)
			i[3]= randint(4, 8)/10
		pygame.draw.rect(win, (110, 35, 255), (i[0],i[1],8,40))
	pygame.display.update()
	pygame.time.Clock().tick(160)