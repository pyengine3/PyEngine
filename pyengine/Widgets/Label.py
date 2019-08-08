from typing import Union

from pyengine.Utils.Color import Colors, Color
from pyengine.Utils.Font import Font
from pyengine.Utils.Logger import loggers
from pyengine.Utils.Vec2 import Vec2
from pyengine.Widgets.Widget import Widget

__all__ = ["Label"]


class Label(Widget):
    def __init__(self, position: Vec2, text: str, color: Color = Colors.WHITE.value,
                 font: Font = Font(), background: Union[None, Color] = None):
        super(Label, self).__init__(position)

        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        if not isinstance(background, Color) and background is not None:
            raise TypeError("Background must be a Color")

        if "\n" in text:
            loggers.get_logger("PyEngine").warning("Line break doesn't work with Label. Use MultilineLabel")
            text = text.replace("\n", "")

        self.__color = color
        self.__font = font
        self.__background = background
        self.text = text
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
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
        self.update_render()

    def update_render(self):
        self.font.background = self.background
        self.font.color = self.color
        self.image = self.font.render(self.text)
        self.update_rect()
        if self.parent:
            self.parent.update_render()

