import pygame

import os

class Player:
    def __init__(self, shiprect, image, bullets):
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

    def set_bullets(self, bullets):
        self._bullets=bullets
    def get_bullets(self):
        return self._bullets

    def draw_player(self, screen, x1, y1):
        screen.blit(self._image, (self._shiprect.x + x1,self._shiprect.y + y1))

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self._shiprect.x = self._shiprect.x - 2
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self._shiprect.x = self._shiprect.x + 2
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self._shiprect.y = self._shiprect.y - 2
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self._shiprect.y = self._shiprect.y + 2

    #def shoot(self, screen, bullet_num):
        #bullet_list=self._bullets[bullet_num-1]
        #pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_SPACE]:
            #bullet=bullet_list.create_bullet(screen)
            #self._bullets.append(bullet)
            

class Bullet:
    def __init__(self, x, y, color):
        self._x=x
        self._y=y
        self._bulletrect = pygame.Rect(self._x, self._y, 15, 30)
        self._color=color

    def set_x(self, x):
        self._x=x
    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y=y
    def get_y(self):
        return self._y

    def set_color(self, color):
        self._color=color
    def get_color(self):
        return self._color

    def draw_bullet(self, screen):
        pygame.draw.rect(screen, self._color, self._bulletrect)

    def update_bullet(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            while self._bulletrect.y > 0:
                self._bulletrect.y = self._bulletrect.y - 2
                self._bulletrect.move(self._bulletrect.x, self._bulletrect.y)


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

pygame.init()

screen_width=1400
screen_height=700

WHITE = (255, 255, 255)

shipImg = pygame.image.load('../Images/galaga-ship.png')
ship_rect = shipImg.get_rect()
shipImg_width = ship_rect.width
shipImg_height = ship_rect.height
ship=Player(ship_rect, shipImg, [])
x1 = 700
y1 = 640
player_bullet=Bullet(x1, y1, WHITE)
ship.set_bullets([player_bullet])

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Bootleg Galaga")

screen.fill((0, 0, 0))

clock = pygame.time.Clock()

keep_playing=True

while keep_playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_playing = False

    screen.fill((0, 0, 0))
    ship.set_image(pygame.transform.scale(shipImg, (shipImg_width*0.1, shipImg_height*0.1)))
    ship.draw_player(screen, x1, y1)
    ship.move()
    #ship.shoot(screen, 1)
    player_bullet.draw_bullet(screen)
    player_bullet.update_bullet()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()