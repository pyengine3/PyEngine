from pyengine.Exceptions import CompatibilityError
from pyengine.Utils import Font, Color, Colors

__all__ = ["TextComponent"]


class TextComponent:
    def __init__(self, text, color=Colors.WHITE.value, font=Font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")

        self.entity = None
        self.text = text
        self.font = font
        self.color = color

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")

        self.__color = color

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.__font = font

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):

        from pyengine.Components.SpriteComponent import SpriteComponent

        if entity.has_component(SpriteComponent):
            raise CompatibilityError("TextComponent is not compatible with SpriteComponent")

        self.__entity = entity

    def render(self):
        return self.font.render().render(self.text, 1, self.color.get())
