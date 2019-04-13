from pyengine.Exceptions import ComponentIntializedError, NoComponentError
from pyengine.Enums import ControlType
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent
from pygame import locals as const

__all__ = ["ControlComponent"]


class ControlComponent:
    name = "ControlComponent"

    def __init__(self):
        self.entity = None
        self.controltype = None
        self.speed = 0
        self.initialized = False

    def initialize(self, entity, controltype, speed=5):
        if self.initialized:
            raise ComponentIntializedError("ControlComponent already initialized")
        if controltype != ControlType.FOURDIRECTION:
            raise NotImplementedError("Only FOURDIRECTION Controltype is implemented")
        self.entity = entity
        self.controltype = controltype
        self.speed = speed

    def keypress(self, eventkey):
        if not self.entity.has_component(PositionComponent):
            raise NoComponentError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        if self.controltype == ControlType.FOURDIRECTION:
            pos = position.get_position()
            if eventkey == const.K_LEFT:
                pos = [position.x - self.speed, position.y]
            if eventkey == const.K_RIGHT:
                pos = [position.x + self.speed, position.y]
            if eventkey == const.K_UP:
                pos = [position.x, position.y - self.speed]
            if eventkey == const.K_DOWN:
                pos = [position.x, position.y + self.speed]

            cango = True
            if self.entity.has_component(PhysicsComponent):
                cango = self.entity.get_component(PhysicsComponent).can_go(pos)
            if cango:
                self.entity.get_component(PositionComponent).set_position(pos)

