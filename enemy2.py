import pygame
import random
import enemy
from power import Power

class EnemyType2(enemy.Enemy):
    def __init__(self, x, y, speed_x, speed_y, size):
        super().__init__(x, y, speed_x, speed_y)
        self._image = pygame.image.load('Imagem/littlecerto.png')
        self._image = pygame.transform.scale(self._image, size)
        self._power = Power(self._x, self._y, 0.7)  

    
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, size):
        self._image = pygame.image.load('Imagem/littlecerto.png')
        self._image = pygame.transform.scale(self._image, size)

    
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    
    def move(self):
        super().move()
        if self._power.state == "ready" and random.randint(0, 100) < 1:
            self._power.fire(self._x + 16, self._y + 32)

    
    def draw(self, screen):
        super().draw(screen)
        self._power.move()
        self._power.draw(screen)

    #Reseta posição inimigo
    def reset_position(self):
        super().reset_position()
        self._power.state = "ready"