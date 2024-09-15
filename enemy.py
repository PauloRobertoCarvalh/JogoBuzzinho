import pygame
import random
from power_enemy1 import PowerEnemy1
import gameobject


class Enemy(gameobject.GameObject):
    def __init__(self, x, y, speed_x, speed_y):
        self._image = pygame.image.load('Imagem/senhorbatata.png')
        self._x = x
        self._y = y
        self._speed_x = speed_x
        self._speed_y = speed_y
        self._power = PowerEnemy1(self._x, self._y, 1.0) 

    
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def speed_x(self):
        return self._speed_x

    @speed_x.setter
    def speed_x(self, value):
        self._speed_x = value

    @property
    def speed_y(self):
        return self._speed_y

    @speed_y.setter
    def speed_y(self, value):
        self._speed_y = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value


    def move(self):
        self._x += self._speed_x
        if self._x <= 0 or self._x >= 736:
            self._speed_x *= -1
            self._y += self._speed_y

        if self._power.state == "ready" and random.randint(0, 100) < 5: 
            self._power.fire(self._x + 16, self._y + 32)

    
    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))
        self._power.move()
        self._power.draw(screen)

    
    def reset_position(self):
        self._x = random.randint(0, 736)
        self._y = random.randint(50, 150)
        self._power.state = "ready"  

    
    def check_collision_with_player(self, player):
        return self._power.is_collision(player)  