import pygame
from pyengine.Entity import Entity

__all__ = ["World"]


class World:
    def __init__(self, gravity_force=5):
        self.entities = pygame.sprite.Group()
        self.gravity_force = gravity_force

    def get_entity(self, identity):
        for i in self.entities:
            if i.identity == identity:
                return i

    def add_entity(self, entity):
        if type(entity) != Entity:
            raise TypeError("Argument is not a Entity")
        entity.set_id(len(self.entities))
        self.entities.add(entity)

    def show(self, screen):
        self.entities.draw(screen)
