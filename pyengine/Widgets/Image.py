import pygame

from pyengine.Utils.Vec2 import Vec2
from pyengine.Widgets.Widget import Widget

__all__ = ["Image"]


class Image(Widget):
    def __init__(self, position: Vec2, sprite: str, size: Vec2 = None):
        super(Image, self).__init__(position)

        self.sprite = sprite
        self.image = pygame.image.load(sprite)

        if size is not None:
            self.size = size

    @property
    def size(self):
        return Vec2(self.rect.width, self.rect.height)

    @size.setter
    def size(self, size):
        if not isinstance(size, Vec2):
            raise TypeError("Position must be a Vec2")

        self.image = pygame.transform.scale(self.image, size.coords)
        self.update_rect()

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite
        self.image = pygame.image.load(sprite)
        self.update_rect()
