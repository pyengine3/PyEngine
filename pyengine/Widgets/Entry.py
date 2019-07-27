import pygame
import string
from pyengine.Widgets.Widget import Widget
from pyengine.Utils import Vec2, Colors, Font, Color
from pygame import locals as const
from typing import Union

__all__ = ["Entry"]


class Entry(Widget):
    accepted = "éèàçù€ " + string.digits + string.ascii_letters + string.punctuation

    def __init__(self, position: Vec2, width: int = 200, image: Union[None, str] = None,
                 color: Union[None, Color] = Colors.BLACK.value, font: Union[None, Font] = Font()):
        super(Entry, self).__init__(position)

        if image is None:
            self.hasimage = False
        else:
            self.hasimage = True
        self.iiwhite = None  # Respect PEP8

        self.__width = width

        self.color = color
        self.font = font
        self.cursortimer = 20
        self.cursor = False
        self.__text = ""
        self.sprite = image

    def hide(self):
        super(Entry, self).hide()

    def show(self):
        super(Entry, self).show()

    @property
    def sprite(self):
        return self.__imagestr

    @sprite.setter
    def sprite(self, val):
        self.__imagestr = val
        self.update_render()

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
            return self.__text[:-1]
        return self.__text

    @text.setter
    def text(self, text):
        if self.cursor:
            self.__text = text+"I"
        else:
            self.__text = text
        self.update_render()

    def focusout(self):
        if self.cursor:
            self.__text = self.__text[:-1]
        self.cursor = False
        self.update_render()

    def keypress(self, evt):
        if evt.key == const.K_BACKSPACE:
            if len(self.__text):
                if self.cursor:
                    self.__text = self.__text[:-2]+"I"
                else:
                    self.__text = self.__text[:-1]
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
        renderer = self.font.render().render(self.__text, 1, self.color.get())
        x = self.width - renderer.get_rect().width - 10
        if x > 2:
            x = 2
        if self.sprite is None:
            self.image = pygame.Surface([self.width, 35])
            self.image.fill((50, 50, 50))
            self.iiwhite = pygame.Surface([self.width - 8, 28])
            self.iiwhite.fill((255, 255, 255))
            self.iiwhite.blit(renderer, (x, self.iiwhite.get_rect().height / 2 - renderer.get_rect().height/2))
            self.image.blit(self.iiwhite, (4, 4))
            self.hasimage = False
        else:
            self.image = pygame.image.load(self.sprite)
            self.image = pygame.transform.scale(self.image, [self.width, 35])
            self.image.blit(renderer, (x, self.image.get_rect().height / 2 - renderer.get_rect().height/2))
            self.hasimage = True
        self.update_rect()

    def add_text(self, texte):
        if self.cursor:
            text = self.__text[:-1] + texte + "I"
        else:
            text = self.__text + texte
        self.__text = text
        self.update_render()

    def update(self):
        if self.cursortimer <= 0:
            if self.cursor:
                self.__text = self.__text[:-1]
            else:
                self.__text = self.__text+"I"
            self.cursor = not self.cursor
            self.cursortimer = 20
            self.update_render()
        self.cursortimer -= 1
