import pygame
from pyengine.Utils import Vec2

__all__ = ["Widget"]


class Widget(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Widget, self).__init__()

        if not isinstance(position, Vec2):
            raise TypeError("Position must be a Vec2")

        self.identity = -1
        self.__position = position
        self.__system = None
        self.parent = None
        self.isshow = True

        self.rect = None  # Respect PEP8
        self.image = None  # Respect PEP8

    @property
    def identity(self):
        return self.__identity

    @identity.setter
    def identity(self, identity):
        self.__identity = identity

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, Vec2):
            raise TypeError("Position must be a Vec2")

        self.__position = position
        self.update_rect()

    def focusin(self):
        pass

    def focusout(self):
        pass

    def is_show(self):
        return self.isshow

    def show(self):
        self.isshow = True

    def hide(self):
        self.isshow = False

    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def mousepress(self, evt):
        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y +\
                self.rect.height:
            return True
