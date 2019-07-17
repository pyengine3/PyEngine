import pygame
import string
from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label
from pyengine.Utils import Vec2, Colors, Font, Color, loggers
from pygame import locals as const
from typing import Union

__all__ = ["Entry"]


class Entry(Widget):
    def __init__(self, position: Vec2, width: int = 200, image: Union[None, str] = None,
                 color: Union[None, Color] = Colors.BLACK.value, font: Union[None, Font] = Font()):
        super(Entry, self).__init__(position)

        self.__width = width

        self.sprite = image
        self.label = Label(Vec2(position.x+5, position.y+5), "", color, font)
        self.label.parent = self
        self.cursortimer = 20
        self.cursor = False
        self.accepted = "éèàçù€ "
        self.accepted += string.digits + string.ascii_letters + string.punctuation
        self.update_render()

    def hide(self):
        super(Entry, self).hide()
        self.label.hide()

    def show(self):
        super(Entry, self).show()
        self.label.show()

    @property
    def sprite(self):
        return self.__imagestr

    @sprite.setter
    def sprite(self, val):
        self.__imagestr = val
        if val is None:
            self.image = pygame.Surface([self.width, 35])
            self.image.fill((50, 50, 50))
            self.iiwhite = pygame.Surface([self.width - 8, 28])
            self.iiwhite.fill((255, 255, 255))
            self.image.blit(self.iiwhite, (4, 4))
            self.hasimage = False
        else:
            self.image = pygame.image.load(val)
            self.image = pygame.transform.scale(self.image, [self.width, 35])
            self.hasimage = True

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = val
        if self.hasimage:
            self.image = pygame.transform.scale(self.image, [self.width, 35])
        else:
            self.image = pygame.Surface([self.width, 35])
            self.image.fill((50, 50, 50))
            self.iiwhite = pygame.Surface([self.width - 8, 28])
            self.iiwhite.fill((255, 255, 255))
            self.image.blit(self.iiwhite, (4, 4))
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

    def keypress(self, evt):
        if evt.key == const.K_BACKSPACE:
            if len(self.label.text):
                if self.cursor:
                    self.label.text = self.label.text[:-2]+"I"
                else:
                    self.label.text = self.label.text[:-1]
        elif evt.key == const.K_v and (evt.mod == const.KMOD_CTRL or evt.mod == const.KMOD_LCTRL):
            clipboard = pygame.scrap.get(const.SCRAP_TEXT)
            if clipboard:
                clipboard = clipboard.decode()[:-1]
                self.add_text(clipboard)
        elif evt.key == const.K_c and (evt.mod == const.KMOD_CTRL or evt.mod == const.KMOD_LCTRL):
            pygame.scrap.put(pygame.SCRAP_TEXT, self.text.encode())
        elif evt.unicode != '' and evt.unicode in self.accepted:
            self.add_text(evt.unicode)

    def update_render(self):
        self.update_rect()
        if self.hasimage:
            self.label.position = Vec2(self.label.position.x,
                                       self.rect.y + self.image.get_rect().height / 2 - self.label.rect.height / 2)
        else:
            self.label.position = Vec2(self.label.position.x,
                                       self.rect.y + 4 + self.iiwhite.get_rect().height / 2 -
                                       self.label.rect.height / 2)

    def add_text(self, texte):
        if self.cursor:
            text = self.label.text[:-1] + texte + "I"
        else:
            text = self.label.text + texte
        if self.label.font.rendered_size(text)[0] < self.rect.width - 10:
            self.label.text = text
        else:
            loggers.get_logger("PyEngine").info("Text are too long to be be added to Entry (Text : "+texte+")")

    def update(self):
        if self.cursortimer <= 0:
            if self.cursor:
                self.label.text = self.label.text[:-1]
            else:
                self.label.text = self.label.text+"I"
            self.cursor = not self.cursor
            self.cursortimer = 20
        self.cursortimer -= 1
