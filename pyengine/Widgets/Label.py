import pygame
from pyengine.Widgets.Widget import Widget
from pyengine.Utils import Font

__all__ = ["Label"]


class Label(Widget):
    def __init__(self, position, text, color=None, font=None):
        super(Label, self).__init__(position)
        if font is None:
            font = Font()
        if color is None:
            color = (255, 255, 255)

        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.color = color
        self.font = font
        self.font.parent = self
        self.text = text
        self.update_render()

    def set_color(self, color):
        self.color = color
        self.update_render()

    def get_color(self):
        return self.color

    def set_font(self, font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.font = font
        self.font.parent = self
        self.update_render()

    def get_font(self):
        return self.font

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        self.update_render()

    def update_render(self):
        self.image = self.font.render().render(self.text, 1, self.color)
        self.update_rect()

