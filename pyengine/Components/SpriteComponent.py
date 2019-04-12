import pygame
from pyengine.Exceptions import ComponentAlreadyIntialized

__all__ = ["SpriteComponent"]


class SpriteComponent:
    def __init__(self):
        self.image = None
        self.entity = None
        self.initialized = False

    def initialize(self, image, entity):
        if self.initialized:
            raise ComponentAlreadyIntialized("SpriteComponent already initialized")
        self.image = image
        self.entity = entity
