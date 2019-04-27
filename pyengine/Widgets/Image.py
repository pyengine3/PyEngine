import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["Image"]


class Image(Widget):
    def __init__(self, position, image, size=None):
        super(Image, self).__init__(position)

        self.image = pygame.image.load(image)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]