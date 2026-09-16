import pygame

import os

class Player:
    def __init__(self, shiprect, image):
      self._shiprect=shiprect
      self._image=image

    def set_shiprect(self, shiprect):
        self._shiprect=shiprect
    def get_shiprect(self):
        return self._shiprect

    def set_image(self, image):
        self._image=image
    def get_image(self):
        return self._image

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self._shiprect.x = self._shiprect.x - 2
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self._shiprect.x = self._shiprect.x + 2

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

pygame.init()

screen_width=1400
screen_height=700

shipImg = pygame.image.load('../Images/galaga-ship.png')
ship_rect = shipImg.get_rect()
shipImg_width = ship_rect.width
shipImg_height = ship_rect.height
ship=Player(ship_rect, shipImg)
x1 = 700
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

    screen.fill((0, 0, 0))
    ship.set_image(pygame.transform.scale(shipImg, (shipImg_width*0.1, shipImg_height*0.1)))
    screen.blit(ship.get_image(), (x1,y1))
    ship.move()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()