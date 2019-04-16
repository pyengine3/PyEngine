import pygame
from pyengine.Exceptions import ComponentIntializedError, CompatibilityError
from pyengine.Components.PositionComponent import PositionComponent

__all__ = ["SpriteComponent"]


class SpriteComponent:
    name = "SpriteComponent"

    def __init__(self):
        self.entity = None
        self.sprite = ""
        self.scale = 1
        self.width = 0
        self.height = 0
        self.initialized = False

    def initialize(self, entity, image, scale=1):
        if self.initialized:
            raise ComponentIntializedError("SpriteComponent already initialized")

        from pyengine.Components.TextComponent import TextComponent

        if entity.has_component(TextComponent):
            raise CompatibilityError("SpriteComponent is not compatible with TextComponent")

        self.initialized = True
        self.entity = entity
        self.sprite = image
        self.entity.image = pygame.image.load(image)
        self.entity.rect = self.entity.image.get_rect()
        self.width = self.entity.rect.width
        self.height = self.entity.rect.height
        self.set_scale(scale)

    def set_scale(self, scale):
        self.scale = scale
        self.entity.image = pygame.transform.scale(self.entity.image, (self.width*scale, self.height*scale))
        self.entity.rect = self.entity.image.get_rect()
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y
