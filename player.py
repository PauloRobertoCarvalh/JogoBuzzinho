import pygame
import gameobject


class Player(gameobject.GameObject):
    def __init__(self, x, y, image_path):
        self._image = pygame.image.load(image_path)
        self._x = x
        self._y = y
        self._x_change = 0
        self._special_power_ready = True  

    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = max(0, min(value, 736))  


    @property
    def y(self):
        return self._y


    @property
    def image(self):
        return self._image

    
    @property
    def x_change(self):
        return self._x_change

    @x_change.setter
    def x_change(self, change):
        self._x_change = change

    
    @property
    def special_power_ready(self):
        return self._special_power_ready

    @special_power_ready.setter
    def special_power_ready(self, ready):
        self._special_power_ready = ready

    #Método mexer jogador
    def move(self):
        self.x += self._x_change 

    
    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))

    
    def set_x_change(self, change):
        self.x_change = change