import pygame
from pyengine.Widgets.Widget import Widget
from pyengine.Utils import Vec2
from typing import Union, Tuple

__all__ = ["Image"]


class Image(Widget):
    def __init__(self, position: Vec2, sprite: str, size: Union[None, Tuple[int, int]] = None):
        super(Image, self).__init__(position)

        self.sprite = sprite
        self.image = pygame.image.load(sprite)

        if size is not None:
            self.size = size

    @property
    def size(self):
        return [self.rect.width, self.rect.height]

    @size.setter
    def size(self, size):
        self.image = pygame.transform.scale(self.image, size)
        self.update_rect()

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite
        self.image = pygame.image.load(sprite)
        self.update_rect()
