import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["Image"]


class Image(Widget):
    def __init__(self, position, image, size=None):
        super(Image, self).__init__(position)

        self.istr = image
        self.image = pygame.image.load(image)

        if size is not None:
            self.size = size

    @property
    def size(self):
        return [self.rect.width, self.rect.height]

    @size.setter
    def size(self, size):
        self.image = pygame.transform.scale(self.image, size)
        self.update_rect()

    def get_image(self):
        return self.istr

    def set_image(self, image):
        self.istr = image
        self.image = pygame.image.load(image)
        self.update_rect()
