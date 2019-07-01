from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent, CollisionCauses
from pyengine.Utils import Vec2

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
        if not isinstance(direction, Vec2):
            raise TypeError("Direction must be a Vec2")

        self.__direction = direction

    def update(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            pos = position.position

            if self.entity.has_component(PhysicsComponent):
                if self.entity.get_component(PhysicsComponent).can_go(pos + self.direction,
                                                                      CollisionCauses.MOVECOMPONENT):
                    self.entity.get_component(PositionComponent).position += self.direction
                elif self.entity.get_component(PhysicsComponent).can_go(pos + Vec2(0, self.direction.y),
                                                                        CollisionCauses.MOVECOMPONENT):
                    self.entity.get_component(PositionComponent).position += self.direction
                elif self.entity.get_component(PhysicsComponent).can_go(pos + Vec2(self.direction.x, 0),
                                                                        CollisionCauses.MOVECOMPONENT):
                    self.entity.get_component(PositionComponent).position += self.direction
            else:
                self.entity.get_component(PositionComponent).position += self.direction
