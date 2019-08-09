import pygame

from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Exceptions import CompatibilityError

__all__ = ["SpriteComponent"]


class SpriteComponent:
    def __init__(self, image: str, scale: int = 1, rotation: int = 0, flipx: bool = False, flipy: bool = False):
        self.__entity = None
        self.__sprite = image
        self.__scale = scale
        self.__rotation = rotation
        self.__flipx = flipx
        self.__flipy = flipy
        self.origin_image = None
        self.width = 0
        self.height = 0

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        from pyengine.Components.TextComponent import TextComponent

        if entity.has_component(TextComponent):
            raise CompatibilityError("SpriteComponent is not compatible with TextComponent")

        self.__entity = entity
        self.__entity.image = pygame.image.load(self.sprite)
        self.__entity.rect = self.entity.image.get_rect()
        self.width = self.entity.rect.width
        self.height = self.entity.rect.height
        self.scale = self.scale
        self.origin_image = self.__entity.image
        self.rotation = self.rotation
        self.flipx = self.flipx
        self.flipy = self.flipy

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        self.__scale = scale
        self.entity.image = pygame.transform.scale(self.entity.image, (round(self.width * scale),
                                                                       round(self.height * scale)))
        self.origin_image = self.__entity.image
        self.update_position()

    @property
    def size(self):
        return [self.width, self.height]

    @size.setter
    def size(self, size):
        if not isinstance(size, pygame.Vector2):
            raise TypeError("Size must be a Vec2")
        self.width, self.height = size.coords
        self.entity.image = pygame.transform.scale(self.entity.image, size.coords)
        self.scale = 1

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        center = self.entity.rect.center
        self.entity.image = pygame.transform.rotate(self.origin_image, rotation)
        self.__rotation = rotation
        self.entity.rect = self.entity.image.get_rect(center=center)
        self.update_position()

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite
        self.entity.image = pygame.image.load(sprite)
        self.width = self.entity.rect.width
        self.height = self.entity.rect.height
        self.entity.image = pygame.transform.scale(self.entity.image, (round(self.width * self.scale),
                                                                       round(self.height * self.scale)))
        self.origin_image = self.entity.image
        self.update_position()

    @property
    def flipx(self):
        return self.__flipx

    @flipx.setter
    def flipx(self, val):
        self.entity.image = pygame.transform.flip(self.origin_image, val, 0)
        self.__flipx = val

    @property
    def flipy(self):
        return self.__flipy

    @flipy.setter
    def flipy(self, val):
        self.entity.image = pygame.transform.flip(self.origin_image, 0, val)
        self.__flipy = val

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect = self.entity.image.get_rect(center=position.position + position.offset)
