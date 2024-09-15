import pygame
import math
import gameobject

class Bullet(gameobject.GameObject):
    def __init__(self, x, y, speed_y):
        self._image = pygame.image.load('imagem/bullet.png')
        self._x = x
        self._y = y
        self._speed_y = speed_y
        self._state = "ready"

    # GT pra imagem da bala
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
    def speed_y(self):
        return self._speed_y

    @speed_y.setter
    def speed_y(self, value):
        self._speed_y = value

   
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    
    def fire(self, x):
        self.state = "fire"
        self.x = x

    
    def move(self):
        if self.state == "fire":
            self._y -= self._speed_y
        if self._y <= 0:
            self.state = "ready"
            self._y = 480

    
    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self._image, (self._x + 2, self._y + 2))

    
    def is_collision(self, enemy):
        distance = math.sqrt(math.pow(enemy.x - self._x, 2) + math.pow(enemy.y - self._y, 2))
        return distance < 27