import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["Label"]


class Label(Widget):
    def __init__(self, position, text, color=None, font=None):
        super(Label, self).__init__(position)
        if font is None:
            font = ["arial", 15, False, False]
        if color is None:
            color = (255, 255, 255)

        if len(font) == 1:
            font.append(15)
        if len(font) == 2:
            font.append(False)
        if len(font) == 3:
            font.append(False)

        self.color = color
        self.font_infos = font
        self.font = pygame.font.SysFont(font[0], font[1], font[2], font[3])
        self.text = text
        self.image = self.font.render(text, 1, color)
        self.update_rect()

    def set_color(self, color):
        self.color = color
        self.image = self.font.render(self.text, 1, color)
        self.update_rect()

    def get_color(self):
        return self.color

    def set_font(self, font):
        if len(font) == 1:
            font.append(15)
        if len(font) == 2:
            font.append(False)
        if len(font) == 3:
            font.append(False)
        self.font_infos = font
        self.font = pygame.font.SysFont(font[0], font[1], font[2], font[3])
        self.image = self.font.render(self.text, 1, self.color)
        self.update_rect()

    def get_font(self):
        return self.font_infos

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(text, 1, self.color)
        self.update_rect()

