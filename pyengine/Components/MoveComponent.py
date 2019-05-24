from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent, CollisionCauses
from pyengine.Exceptions import NoObjectError

__all__ = ["MoveComponent"]


class MoveComponent:
    def __init__(self, direction, speed=5):
        self.entity = None
        self.direction = direction
        self.speed = speed

    def set_entity(self, entity):
        self.entity = entity

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def update(self):
        if not self.entity.has_component(PositionComponent):
            raise NoObjectError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        pos = position.get_position()
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
            self.entity.get_component(PositionComponent).set_position(pos)

