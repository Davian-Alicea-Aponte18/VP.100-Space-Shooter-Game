import pygame

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

pygame.init()

screen_width=1400
screen_height=700

shipImg = pygame.image.load('../Images/galaga-ship.png')
shipImg_width = shipImg.get_rect().width
shipImg_height = shipImg.get_rect().height
x1 = 699
y1 = 640

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Bootleg Galaga")

screen.fill((0, 0, 0))

clock = pygame.time.Clock()

keep_playing=True

while keep_playing==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_playing = False

    shipImg = pygame.transform.scale(shipImg, (shipImg_width*0.1, shipImg_height*0.1))
    screen.blit(shipImg, (x1,y1))         

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()