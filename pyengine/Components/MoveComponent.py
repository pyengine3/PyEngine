import pygame

from pyengine.Components.PhysicsComponent import PhysicsComponent
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Utils.Vec2 import Vec2

__all__ = ["MoveComponent"]


class MoveComponent:
    def __init__(self, direction: Vec2):
        self.entity = None
        self.direction = direction

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if not isinstance(direction, pygame.Vector2):
            raise TypeError("Direction must be a Vec2")

        self.__direction = direction

    def update(self):
        if self.entity.has_component(PhysicsComponent):
            self.entity.get_component(PhysicsComponent).body.velocity = self.direction

        elif self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            pos = position.position

            self.entity.get_component(PositionComponent).position += self.direction
