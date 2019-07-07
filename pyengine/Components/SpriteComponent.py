import pygame
from pyengine.Exceptions import CompatibilityError
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Utils import Vec2

__all__ = ["SpriteComponent"]


class SpriteComponent:
    def __init__(self, image: str, scale: int = 1, rotation: int = 0):
        self.__entity = None
        self.__sprite = image
        self.__scale = scale
        self.firstrotation = rotation
        self.__rotation = 0
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
        self.rotation = self.firstrotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        self.__scale = scale
        self.width = int(self.width*scale)
        self.height = int(self.height*scale)
        self.entity.image = pygame.transform.scale(self.entity.image, (self.width, self.height))
        self.update_entity()

    @property
    def size(self):
        return [self.width, self.height]

    @size.setter
    def size(self, size):
        if not isinstance(size, Vec2):
            raise TypeError("Size must be a Vec2")
        self.width, self.height = size.coords
        self.entity.image = pygame.transform.scale(self.entity.image, size.coords)
        self.scale = 1

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        temp = self.__rotation
        self.__rotation = rotation
        self.entity.image = pygame.transform.rotate(self.entity.image, self.__rotation - temp)
        self.update_entity()

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite
        self.entity.image = pygame.image.load(sprite)
        self.width = int(self.width*self.scale)
        self.height = int(self.height*self.scale)
        self.entity.image = pygame.transform.scale(self.entity.image, (self.width, self.height))
        self.update_entity()

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.position.x
            self.entity.rect.y = position.position.y

    def update_entity(self):
        self.entity.rect = self.entity.image.get_rect()
        self.update_position()
