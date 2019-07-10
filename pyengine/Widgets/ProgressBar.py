from pyengine.Widgets.Widget import Widget
from pyengine.Utils import Vec2, clamp
from typing import Tuple

import pygame

__all__ = ["ProgressBar"]


class ProgressBar(Widget):
    def __init__(self, pos: Vec2, size: Vec2 = Vec2(150, 10), sprites: Tuple[str, str] = None):
        super(ProgressBar, self).__init__(pos)

        self.__value = 0
        self.__size = size

        self.sprites = sprites

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = clamp(val, 0, 100)
        self.create_image()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val: Vec2):
        self.__size = val
        self.create_image()

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, val: Tuple[str, str]):
        self.__sprites = val
        self.create_image()

    def create_image(self):
        if self.sprites is None:
            self.image = pygame.Surface(self.size.coords)
            self.image.fill((50, 50, 50))
            iiwhite = pygame.Surface([self.size.x - 2, self.size.y - 2])
            iiwhite.fill((255, 255, 255))
            self.image.blit(iiwhite, (self.image.get_width() / 2 - iiwhite.get_width() / 2,
                                      self.image.get_height() / 2 - iiwhite.get_height() / 2))
            iigreen = pygame.Surface([int((self.size.x - 4) * (self.value / 100)), int(self.size.y - 4)])
            iigreen.fill((0, 255, 0))
            self.image.blit(iigreen, (2, self.image.get_height() / 2 - iigreen.get_height() / 2))
        else:
            self.image = pygame.image.load(self.sprites[0])
            self.image = pygame.transform.scale(self.image, self.size.coords)
            barre = pygame.image.load(self.sprites[1])
            barre = pygame.transform.scale(barre, [int((self.size.x - 4) * (self.value / 100)), int(self.size.y - 4)])
            self.image.blit(barre, (2, self.image.get_height() / 2 - barre.get_height() / 2))

        self.update_rect()
