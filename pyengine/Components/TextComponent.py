from typing import Union

import pygame

from pyengine.Components import PositionComponent
from pyengine.Exceptions import CompatibilityError
from pyengine.Utils.Font import Font
from pyengine.Utils.Color import Color, Colors

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
        self.__text = text
        self.__font = font
        self.__scale = scale
        self.__color = color
        self.__background = background
        self.image = None

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val):
        self.__scale = val
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
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
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
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):

        from pyengine.Components.SpriteComponent import SpriteComponent

        if entity.has_component(SpriteComponent):
            raise CompatibilityError("TextComponent is not compatible with SpriteComponent")

        self.__entity = entity
        self.update_render()

    @property
    def size(self):
        return self.image.get_rect().width, self.image.get_rect().height

    def update_render(self):
        self.font.color = self.color
        self.font.background = self.background
        self.image = self.font.render(self.text)
        self.image = pygame.transform.scale(self.image, (self.scale*self.image.get_rect().width,
                                                         self.scale*self.image.get_rect().height))

        if self.entity is not None:
            self.entity.image = self.image
            self.entity.rect = self.image.get_rect()
            self.update_position()

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.position.x + position.offset.x
            self.entity.rect.y = position.position.y + position.offset.y
