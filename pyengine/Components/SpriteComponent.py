import pygame
from pyengine.Exceptions import ComponentIntializedError, CompatibilityError
from pyengine.Components.PositionComponent import PositionComponent

__all__ = ["SpriteComponent"]


class SpriteComponent:
    name = "SpriteComponent"

    def __init__(self):
        self.entity = None
        self.sprite = ""
        self.initialized = False

    def initialize(self, entity, image):
        if self.initialized:
            raise ComponentIntializedError("SpriteComponent already initialized")

        from pyengine.Components.TextComponent import TextComponent

        if entity.has_component(TextComponent):
            raise CompatibilityError("SpriteComponent is not compatible with TextComponent")

        self.initialized = True
        self.entity = entity
        self.sprite = image
        self.entity.image = pygame.image.load(image)
        if self.entity.has_component(PositionComponent):
            position = entity.get_component(PositionComponent)
            self.entity.rect = self.entity.image.get_rect()
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y

    def update_position(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            self.entity.rect.x = position.x
            self.entity.rect.y = position.y
