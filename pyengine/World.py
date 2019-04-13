import pygame
from pyengine.Entity import Entity

__all__ = ["World"]


class World:
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.window = None

    def set_window(self, window):
        self.window = window

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
        entity.set_world(self)
        self.entities.add(entity)

    def update(self):
        for i in self.entities:
            i.update()

    def keypress(self, key):
        for i in self.entities:
            if i.has_component(ControlComponent):
                i.get_component(ControlComponent).keypress(key)

    def show(self, screen):
        self.entities.draw(screen)
