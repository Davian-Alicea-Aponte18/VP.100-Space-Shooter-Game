import pygame

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

pygame.init()

screen_width=700
screen_height=300

shipImg = pygame.image.load('galaga-ship.png')
x1 = 450
y1 = 50

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Bootleg Galaga")

#screen.fill((0, 0, 0))

clock = pygame.time.Clock()

keep_playing=True

while keep_playing==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_playing = False

screen.blit(shipImg, (x1,y1))         

pygame.display.update()
clock.tick(60)

pygame.quit()
quit()