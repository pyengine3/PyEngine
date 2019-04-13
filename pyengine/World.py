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
        if not entity.has_component(PositionComponent) and not entity.has_component(SpriteComponent):
            raise NoComponentError("Entity must have PositionComponent and SpriteComponent to be add in a world.")
        entity.set_id(len(self.entities))
        self.entities.add(entity)

    def show(self, screen):
        self.entities.draw(screen)
