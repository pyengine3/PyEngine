from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent, CollisionCauses
from pyengine.Utils import Vec2

__all__ = ["MoveComponent"]


class MoveComponent:
    def __init__(self, direction, speed=5):
        self.entity = None
        self.direction = direction
        self.speed = speed

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        if not isinstance(direction, Vec2):
            raise TypeError("Direction must be a Vec2")

        self.__direction = direction

    def update(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            pos = position.position
            if self.direction[0] == 1:
                pos[0] += self.speed
            elif self.direction[0] == -1:
                pos[0] -= self.speed
            if self.direction[1] == 1:
                pos[1] += self.speed
            elif self.direction[1] == -1:
                pos[1] -= self.speed
            cango = True
            if self.entity.has_component(PhysicsComponent):
                cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.MOVECOMPONENT)
            if cango:
                self.entity.get_component(PositionComponent).position = pos

