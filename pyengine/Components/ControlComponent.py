from pyengine.Exceptions import NoObjectError
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent, CollisionCauses
from pyengine.Utils import Vec2
from pygame import locals as const
from enum import Enum

__all__ = ["ControlComponent", "Controls", "ControlType", "MouseButton"]


class ControlType(Enum):
    FOURDIRECTION = 1
    CLASSICJUMP = 2
    DOUBLEJUMP = 3
    CLICKFOLLOW = 4
    LEFTRIGHT = 5
    UPDOWN = 6


class Controls(Enum):
    UPJUMP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


class MouseButton(Enum):
    LEFTCLICK = 1
    MIDDLECLICK = 2
    RIGHTCLICK = 3


class ControlComponent:
    def __init__(self, controltype, speed=5):
        self.entity = None
        self.controltype = controltype
        self.speed = speed
        self.goto = Vec2(-1, -1)
        self.jumping = False
        self.controles = {
            Controls.UPJUMP: const.K_UP,
            Controls.LEFT: const.K_LEFT,
            Controls.RIGHT: const.K_RIGHT,
            Controls.DOWN: const.K_DOWN
        }

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

    def set_control(self, name, key):
        if not isinstance(name, Controls):
            raise TypeError("Name must be a Controls type")
        self.controles[name] = key

    def get_control(self, name):
        if not isinstance(name, Controls):
            raise TypeError("Name must be a Controls type")
        return self.controles[name]

    def update(self):
        if self.controltype == ControlType.CLICKFOLLOW and self.goto != (-1, -1):
            if self.entity.has_component(PositionComponent):
                position = self.entity.get_component(PositionComponent)
                if position.x-10 < self.goto.x < position.x+10 and position.y-10 < self.goto.y < position.y+10:
                    self.goto = Vec2(-1, -1)
                else:
                    pos = position.position
                    if position.x-10 > self.goto.x:
                        pos.x = position.x - self.speed
                    elif position.x+10 < self.goto.x:
                        pos.x = position.x + self.speed
                    if position.y-10 > self.goto.y:
                        pos.y = position.y - self.speed
                    elif position.y+10 < self.goto.y:
                        pos.y = position.y + self.speed

                    cango = True
                    if self.entity.has_component(PhysicsComponent):
                        cango = self.entity.get_component(PhysicsComponent).can_go(pos)
                    if cango:
                        self.entity.get_component(PositionComponent).position = pos

    def mousepress(self, evt):
        if self.controltype == ControlType.CLICKFOLLOW and evt.button == MouseButton.LEFTCLICK.value:
            self.goto = Vec2(evt.pos[0], evt.pos[1])

    def keyup(self, evt):
        eventkey = evt.key
        if self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.CLASSICJUMP:
            if eventkey == self.controles[Controls.UPJUMP]:
                self.jumping = False

    def keypress(self, evt):
        eventkey = evt.key
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            pos = position.position
            cango = True
            if eventkey == self.controles[Controls.LEFT]:
                if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                        or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                    pos = Vec2(pos.x - self.speed, pos.y)
                    if self.entity.has_component(PhysicsComponent):
                        cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.LEFTCONTROL)
            if eventkey == self.controles[Controls.RIGHT]:
                if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                        or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                    pos = Vec2(pos.x + self.speed, pos.y)
                    if self.entity.has_component(PhysicsComponent):
                        cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.RIGHTCONTROL)
            if eventkey == self.controles[Controls.UPJUMP]:
                if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                    pos = Vec2(pos.x, pos.y - self.speed)
                    if self.entity.has_component(PhysicsComponent):
                        cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.UPCONTROL)
                elif self.controltype == ControlType.CLASSICJUMP:
                    if not self.entity.has_component(PhysicsComponent):
                        raise NoObjectError("Entity must have PhysicsComponent")
                    phys = self.entity.get_component(PhysicsComponent)
                    if phys.grounded and not self.jumping:
                        phys.grounded = False
                        self.jumping = True
                        phys.gravity = -phys.max_gravity_force
                elif self.controltype == ControlType.DOUBLEJUMP:
                    if not self.entity.has_component(PhysicsComponent):
                        raise NoObjectError("Entity must have PhysicsComponent")
                    phys = self.entity.get_component(PhysicsComponent)
                    if (phys.grounded or phys.doublejump) and not self.jumping:
                        if not phys.grounded:
                            phys.doublejump = False
                        phys.grounded = False
                        self.jumping = True
                        phys.gravity = -phys.max_gravity_force
            if eventkey == self.controles[Controls.DOWN]:
                if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                    pos = Vec2(pos.x, pos.y + self.speed)
                    if self.entity.has_component(PhysicsComponent):
                        cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.DOWNCONTROL)

            if cango:
                self.entity.get_component(PositionComponent).position = pos
