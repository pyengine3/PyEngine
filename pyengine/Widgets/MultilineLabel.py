from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label
from pyengine.Utils import Font, Color, Colors, Vec2, loggers
from typing import Union
import pygame

__all__ = ["MultilineLabel"]


class MultilineLabel(Widget):
    def __init__(self, position: Vec2, text: str, color: Color = Colors.WHITE.value,
                 font: Font = Font(), background: Union[None, Color] = None):
        super(MultilineLabel, self).__init__(position)

        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        if not isinstance(background, Color) and background is not None:
            raise TypeError("Background must be a Color")

        if "\n" not in text:
            loggers.get_logger("PyEngine").info("MultilineLabel without Line break is useless. Use Label.")

        self.__text = text
        self.labels = [Label(Vec2(self.position.x, self.position.y + 20*(k+1)), v)
                       for k, v in enumerate(text.split("\n"))]

        self.__color = color
        self.__font = font
        self.__background = background
        self.update_render()

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, color):
        if not isinstance(color, Color) and color is not None:
            raise TypeError("Background must be a Color")

        self.__background = color
        self.update_render()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")

        self.__color = color
        self.update_render()

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.__font = font
        self.update_render()

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        [system.add_widget(i) for i in self.labels if i != self]

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if len(self.labels):
            [self.system.remove_widget(i) for i in self.labels]
        if "\n" not in text:
            loggers.get_logger("PyEngine").info("MultilineLabel without Line break is useless. Use Label.")

        self.__text = text
        self.labels = [Label(Vec2(self.position.x, self.position.y + 20 * (k + 1)), v)
                       for k, v in enumerate(text.split("\n"))]
        [self.system.add_widget(i) for i in self.labels]
        self.update_render()

    def update_render(self):
        for i in self.labels:
            self.font.color = self.color
            self.font.background = self.background
            i.image = self.font.render(i.text)
            i.update_rect()
        if self.parent:
            self.parent.update_render()

