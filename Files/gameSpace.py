import pygame
import random
import os

class GameObject():
    def __init__(self, objectrect, image, bullets):
      self._objectrect=objectrect
      self._image=image
      self._bullets=bullets

    def set_objectrect(self, objectrect):
        self._objectrect=objectrect
    def get_objectrect(self):
        return self._objectrect

    def set_image(self, image):
        self._image=image
    def get_image(self):
        return self._image

    def set_bullets(self, bullets):
        self._bullets=bullets
    def get_bullets(self):
        return self._bullets

    def draw_object(self, screen):
        screen.blit(self._image, (self._objectrect.x,self._objectrect.y))

class Player(GameObject):
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self._objectrect.x = self._objectrect.x - 2
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self._objectrect.x = self._objectrect.x + 2
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self._objectrect.y = self._objectrect.y - 2
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self._objectrect.y = self._objectrect.y + 2

    def shoot(self, screen, color):
        player_bullet=Bullet(self._objectrect.x + 15, self._objectrect.y, color)
        self._bullets.append(player_bullet)

class Enemy(GameObject):
    pass

class Bullet:
    def __init__(self, x, y, color):
        self._x=x
        self._y=y
        self._bulletrect = pygame.Rect(self._x, self._y, 10, 30)
        self._color=color

    def set_x(self, x):
        self._x=x
    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y=y
    def get_y(self):
        return self._y

    def set_bulletrect(self, x, y):
        self._bulletrect = pygame.Rect(x, y, 10, 30)
    def get_bulletrect(self):
        return self._bulletrect

    def set_color(self, color):
        self._color=color
    def get_color(self):
        return self._color

    def draw_bullet(self, screen):
        pygame.draw.rect(screen, self._color, self._bulletrect)

    def update_bullet(self):
        self._bulletrect.y = self._bulletrect.y - 2
        self._bulletrect.move(self._bulletrect.x, self._bulletrect.y)

def spawn_enemies(enemies, ex, enemyImg_width, enemyImg_height):
    enemyship=Enemy(pygame.Rect(ex, 0, enemyImg_width, enemyImg_height), enemyImg,[])
    enemyship.set_image(pygame.transform.scale(enemyImg, (enemyImg_width*0.03 , enemyImg_height*0.03)))
    enemies.append(enemyship)
    for enemy in enemies:
        enemy.draw_object(screen)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

pygame.init()

screen_width=1395
screen_height=720

WHITE = (255, 255, 255)

shipImg = pygame.image.load('../Images/galaga-ship.png')
enemyImg = pygame.image.load('../Images/galaga-enemy-ship.png')
ship_rect = shipImg.get_rect()
enemyship_rect = enemyImg.get_rect()
shipImg_width = ship_rect.width
shipImg_height = ship_rect.height
enemyImg_width = enemyship_rect.width - 1
enemyImg_height = enemyship_rect.height - 1
enemies = []
x1 = 675
y1 = 640
ex = 45
ship=Player(pygame.Rect(x1, y1, shipImg_width, shipImg_height), shipImg, [])

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Bootleg Galaga")

screen.fill((0, 0, 0))

clock = pygame.time.Clock()

keep_playing=True

while keep_playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_playing = False
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                ship.shoot(screen, WHITE)
                           
    screen.fill((0, 0, 0))
    ship.set_image(pygame.transform.scale(shipImg, (shipImg_width*0.1, shipImg_height*0.1)))
    ship.draw_object(screen)
    if len(enemies) <= 15:
        spawn_enemies(enemies, ex, enemyImg_width, enemyImg_height)
        if ex < screen_width - 45:
            ex+=90
        else:
            ex=45 
    else:
        for enemy in enemies:
            enemy.draw_object(screen)
    ship.move()
    for bullet in ship.get_bullets():
        bullet.update_bullet()
        bullet.draw_bullet(screen)
        if bullet.get_bulletrect().y < bullet.get_bulletrect().height * -1:
            ship.get_bullets().remove(bullet)
    for enemy in enemies:
        enemy.get_objectrect().y = enemy.get_objectrect().y + 2
        enemy.get_objectrect().move(enemy.get_objectrect().x, enemy.get_objectrect().y)
        enemy.draw_object(screen)
        if enemy.get_objectrect().y > enemy.get_objectrect().height + screen_height:
            enemies.remove(enemy)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()