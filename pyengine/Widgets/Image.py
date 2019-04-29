import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["Image"]


class Image(Widget):
    def __init__(self, position, image, size=None):
        super(Image, self).__init__(position)

        self.istr = image
        self.image = pygame.image.load(image)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.update_rect()

    def get_image(self):
        return self.istr

    def set_image(self, image, size=None):
        self.istr = image
        self.image = pygame.image.load(image)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.update_rect()

    def get_size(self):
        return [self.rect.width, self.rect.height]

    def set_size(self, size):
        self.image = pygame.transform.scale(self.image, size)
        self.update_rect()
