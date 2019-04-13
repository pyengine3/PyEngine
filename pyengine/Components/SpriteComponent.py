import pygame
from pyengine.Exceptions import ComponentIntializedError
from pyengine.Components.PositionComponent import PositionComponent

__all__ = ["SpriteComponent"]


class SpriteComponent:
    name = "SpriteComponent"

    def __init__(self):
        self.entity = None
        self.initialized = False

    def initialize(self, entity, image):
        if self.initialized:
            raise ComponentAlreadyIntialized("SpriteComponent already initialized")
        self.entity = entity
        self.entity.sprite = image
        self.entity.image = pygame.image.load(image)
        if self.entity.has_component(PositionComponent):
            self.entity.rect = self.entity.image.get_rect()
            self.entity.rect.x = self.entity.x
            self.entity.rect.y = self.entity.y

    def update_position(self):
        self.entity.rect.x = self.entity.x
        self.entity.rect.y = self.entity.y
