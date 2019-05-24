from pyengine.Exceptions import NoObjectError
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent
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
        self.goto = (-1, -1)
        self.jumping = False
        self.controles = {
            Controls.UPJUMP: const.K_UP,
            Controls.LEFT: const.K_LEFT,
            Controls.RIGHT: const.K_RIGHT,
            Controls.DOWN: const.K_DOWN
        }

    def set_control(self, name, key):
        if not type(name) == Controls:
            raise TypeError("Name must be a Controls type")
        try:
            self.controles[name] = key
        except KeyError:
            raise ValueError("Control unknown : "+name)

    def get_control(self, name):
        if not type(name) == Controls:
            raise TypeError("Name must be a Controls type")
        try:
            return self.controles[name]
        except KeyError:
            raise ValueError("Control unknown : "+name)

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_entity(self, entity):
        self.entity = entity

    def update(self):
        if self.controltype == ControlType.CLICKFOLLOW and self.goto != (-1, -1):
            if not self.entity.has_component(PositionComponent):
                raise NoObjectError("Entity must have PositionComponent.")
            position = self.entity.get_component(PositionComponent)
            if position.x-10 < self.goto[0] < position.x+10 and position.y-10 < self.goto[1] < position.y+10:
                self.goto = (-1, -1)
            else:
                pos = [position.x, position.y]
                if position.x-10 > self.goto[0]:
                    pos[0] = position.x - self.speed
                elif position.x+10 < self.goto[0]:
                    pos[0] = position.x + self.speed
                if position.y-10 > self.goto[1]:
                    pos[1] = position.y - self.speed
                elif position.y+10 < self.goto[1]:
                    pos[1] = position.y + self.speed

                cango = True
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos)
                if cango:
                    self.entity.get_component(PositionComponent).set_position(pos)

    def mousepress(self, evt):
        if self.controltype == ControlType.CLICKFOLLOW and evt.button == MouseButton.LEFTCLICK.value:
            self.goto = evt.pos

    def keyup(self, evt):
        eventkey = evt.key
        if self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.CLASSICJUMP:
            if eventkey == self.controles[Controls.UPJUMP]:
                self.jumping = False

    def keypress(self, evt):
        eventkey = evt.key
        if not self.entity.has_component(PositionComponent):
            raise NoObjectError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        pos = position.get_position()
        cango = True
        if eventkey == self.controles[Controls.LEFT]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                    or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                pos = [position.x - self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.LEFTCONTROL)
        if eventkey == self.controles[Controls.RIGHT]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                    or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                pos = [position.x + self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.RIGHTCONTROL)
        if eventkey == self.controles[Controls.UPJUMP]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                pos = [position.x, position.y - self.speed]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.UPCONTROL)
            elif self.controltype == ControlType.CLASSICJUMP:
                if not self.entity.has_component(PhysicsComponent):
                    raise NoObjectError("Entity must have PhysicsComponent")
                phys = self.entity.get_component(PhysicsComponent)
                if phys.grounded and not self.jumping:
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity_force = -phys.max_gravity_force
            elif self.controltype == ControlType.DOUBLEJUMP:
                if not self.entity.has_component(PhysicsComponent):
                    raise NoObjectError("Entity must have PhysicsComponent")
                phys = self.entity.get_component(PhysicsComponent)
                if (phys.grounded or phys.doublejump) and not self.jumping:
                    if not phys.grounded:
                        phys.doublejump = False
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity_force = -phys.max_gravity_force
        if eventkey ==  self.controles[Controls.DOWN]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                pos = [position.x, position.y + self.speed]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.DOWNCONTROL)

        if cango:
            self.entity.get_component(PositionComponent).set_position(pos)
