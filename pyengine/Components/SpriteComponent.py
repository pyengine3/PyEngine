import pygame
from pyengine.Exceptions import CompatibilityError
from pyengine.Components.PositionComponent import PositionComponent

__all__ = ["SpriteComponent"]


class SpriteComponent:
    def __init__(self, image, scale=1, rotation=0):
        self.entity = None
        self.sprite = image
        self.scale = scale
        self.rotation = rotation
        self.width = 0
        self.height = 0

    def set_entity(self, entity):

        from pyengine.Components.TextComponent import TextComponent

        if entity.has_component(TextComponent):
            raise CompatibilityError("SpriteComponent is not compatible with TextComponent")

        self.entity = entity
        self.entity.image = pygame.image.load(self.sprite)
        self.entity.rect = self.entity.image.get_rect()
        self.width = self.entity.rect.width
        self.height = self.entity.rect.height
        self.set_scale(self.scale)
        self.set_rotation(self.rotation)

    def set_scale(self, scale):
        self.scale = scale
        self.entity.image = pygame.transform.scale(self.entity.image, (self.width*scale, self.height*scale))
        self.entity.rect = self.entity.image.get_rect()
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y

    def set_size(self, size):
        self.width, self.height = size
        self.scale = 1
        self.entity.image = pygame.transform.scale(self.entity.image, size)
        self.entity.rect = self.entity.image.get_rect()
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y

    def set_rotation(self, rotation):
        self.rotation = rotation - self.rotation
        self.entity.image = pygame.transform.rotate(self.entity.image, self.rotation)
        self.entity.rect = self.entity.image.get_rect()
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y

    def set_sprite(self, sprite, scale=1):
        self.sprite = sprite
        self.entity.image = pygame.image.load(sprite)
        self.entity.rect = self.entity.image.get_rect()
        self.width = self.entity.rect.width
        self.height = self.entity.rect.height
        self.set_scale(scale)

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y
