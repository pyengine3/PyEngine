from pyengine.Exceptions import CompatibilityError
from pyengine.Utils import Font, Color, Colors
import pygame
from typing import Union

__all__ = ["TextComponent"]


class TextComponent:
    def __init__(self, text: str, color: Color = Colors.WHITE.value, font: Font = Font(),
                 background: Union[None, Color] = None, scale: int = 1):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        if not isinstance(background, Color) and background is not None:
            raise TypeError("Background must be a Color")

        self.__entity = None
        self.text = text
        self.font = font
        self.scale = scale
        self.color = color
        self.background = background

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val):
        self.__scale = val

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, color):
        if not isinstance(color, Color) and color is not None:
            raise TypeError("Background must be a Color")

        self.__background = color

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
        self.__entity.image = self.render()

    @property
    def rendered_size(self):
        return self.render().get_rect().width, self.render().get_rect().height

    def render(self) -> pygame.Surface:
        if self.background is None:
            image = self.font.render().render(self.text, 1, self.color.get())
        else:
            renderer = self.font.render().render(self.text, 1, self.color.get())
            image = pygame.Surface([renderer.get_rect().width, renderer.get_rect().height])
            image.fill(self.background.get())
            image.blit(renderer, [0, 0])
        image = pygame.transform.scale(image, (self.scale*image.get_rect().width, self.scale*image.get_rect().height))
        return image
