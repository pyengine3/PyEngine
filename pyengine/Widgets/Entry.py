import pygame
from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label
from pyengine.Utils import Vec2
from pygame import locals as const

__all__ = ["Entry"]


class Entry(Widget):
    def __init__(self, position, width=200, image=None):
        super(Entry, self).__init__(position)

        self.width = width

        if image is not None:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, [self.width, 35])
            self.hasimage = True
        else:
            self.image = pygame.Surface([self.width, 35])
            self.image.fill((50, 50, 50))
            self.iiwhite = pygame.Surface([self.width-8, 28])
            self.iiwhite.fill((255, 255, 255))
            self.image.blit(self.iiwhite, (4, 4))
            self.hasimage = False
        self.label = Label([position.x+5, position.y+5], "", (0, 0, 0), ["arial", 17])
        self.label.parent = self
        self.cursortimer = 20
        self.cursor = False
        self.typing = False
        self.update_render()

    @property
    def text(self):
        if self.cursor:
            return self.label.text[:-1]
        return self.label.text

    @text.setter
    def text(self, text):
        if self.cursor:
            self.label.text = text+"I"
        else:
            self.label.text = text

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        system.add_widget(self.label)

    def focusout(self):
        if self.cursor:
            self.label.text = self.label.text[:-1]
        self.cursor = False
        self.typing = False

    def keyup(self, evt):
        self.typing = False

    def keypress(self, evt):
        if evt.key == const.K_BACKSPACE and not self.typing:
            if len(self.label.text):
                if self.cursor:
                    self.label.text = self.label.text[:-2]+"I"
                else:
                    self.label.text = self.label.text[:-1]
        elif evt.unicode and not self.typing:
            if self.cursor:
                if self.label.rect.width + 10 < self.rect.width:
                    self.label.text = self.label.text[:-1]+evt.unicode+"I"
            else:
                if self.label.rect.width + 10 < self.rect.width:
                    self.label.text = self.label.text + evt.unicode
        self.typing = True

    def update_render(self):
        self.update_rect()
        if self.hasimage:
            self.label.position = Vec2(self.label.position.x,
                                       self.rect.y + self.image.get_rect().height / 2 - self.label.rect.height / 2)
        else:
            self.label.position = Vec2(self.label.position.x,
                                       self.rect.y + 4 + self.iiwhite.get_rect().height / 2 -
                                       self.label.rect.height / 2)

    def update(self):
        if self.cursortimer <= 0:
            if self.cursor:
                self.label.text = self.label.text[:-1]
            else:
                self.label.text = self.label.text+"I"
            self.cursor = not self.cursor
            self.cursortimer = 20
        self.cursortimer -= 1

