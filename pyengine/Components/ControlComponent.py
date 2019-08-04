from pyengine.Exceptions import NoObjectError
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent
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
    MOUSEFOLLOW = 7


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
    def __init__(self, controltype: ControlType, speed: int = 5):
        self.entity = None
        self.controltype = controltype
        self.speed = speed
        self.goto = Vec2(-1, -1)
        self.jumping = False
        self.keypressed = []
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

    def set_control(self, name: Controls, key: const) -> None:
        if not isinstance(name, Controls):
            raise TypeError("Name must be a Controls type")
        self.controles[name] = key

    def get_control(self, name: Controls) -> const:
        if not isinstance(name, Controls):
            raise TypeError("Name must be a Controls type")
        return self.controles[name]

    def update(self):
        if (self.controltype == ControlType.CLICKFOLLOW or self.controltype == ControlType.MOUSEFOLLOW) \
                and self.goto.coords != (-1, -1):
            self.movebymouse()
        else:
            for i in self.keypressed:
                self.movebykey(i)

    def mousepress(self, evt):
        if self.controltype == ControlType.CLICKFOLLOW and evt.button == MouseButton.LEFTCLICK.value:
            self.goto = Vec2(evt.pos[0], evt.pos[1])

    def mousemotion(self, evt):
        if self.controltype == ControlType.MOUSEFOLLOW:
            self.goto = Vec2(evt.pos[0], evt.pos[1])

    def keyup(self, evt):
        if evt.key in self.keypressed:
            self.keypressed.remove(evt.key)
        if self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.CLASSICJUMP:
            if evt.key == self.controles[Controls.UPJUMP]:
                self.jumping = False

    def keypress(self, evt):
        if evt.key not in self.keypressed:
            self.keypressed.append(evt.key)

    def movebymouse(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent).position
            if position.x - 10 < self.goto.x < position.x + 10 and position.y - 10 < self.goto.y < position.y + 10:
                self.goto = Vec2(-1, -1)
            else:
                pos = Vec2()
                if position.x - 10 > self.goto.x:
                    pos.x = position.x - self.speed
                elif position.x + 10 < self.goto.x:
                    pos.x = position.x + self.speed
                else:
                    pos.x = position.x
                if position.y - 10 > self.goto.y:
                    pos.y = position.y - self.speed
                elif position.y + 10 < self.goto.y:
                    pos.y = position.y + self.speed
                else:
                    pos.y = position.y

                self.entity.get_component(PositionComponent).position = pos

    def movebykey(self, eventkey):
        if eventkey == self.controles[Controls.LEFT]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                    or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                if self.entity.has_component(PositionComponent):
                    pos = self.entity.get_component(PositionComponent)
                    pos.position = Vec2(pos.position.x - self.speed, pos.position.y)
                elif self.entity.has_component(PhysicsComponent):
                    self.entity.get_component(PhysicsComponent).body.velocity = [-self.speed, 0]
        elif eventkey == self.controles[Controls.RIGHT]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.CLASSICJUMP \
                    or self.controltype == ControlType.DOUBLEJUMP or self.controltype == ControlType.LEFTRIGHT:
                if self.entity.has_component(PositionComponent):
                    pos = self.entity.get_component(PositionComponent)
                    pos.position = Vec2(pos.position.x + self.speed, pos.position.y)
                elif self.entity.has_component(PhysicsComponent):
                    self.entity.get_component(PhysicsComponent).body.velocity = [self.speed, 0]
        elif eventkey == self.controles[Controls.UPJUMP]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                if self.entity.has_component(PositionComponent):
                    pos = self.entity.get_component(PositionComponent)
                    pos.position = Vec2(pos.position.x, pos.position.y - self.speed)
                elif self.entity.has_component(PhysicsComponent):
                    self.entity.get_component(PhysicsComponent).body.velocity = [0, self.speed]
            elif self.controltype == ControlType.CLASSICJUMP and self.controltype == ControlType.DOUBLEJUMP:
                raise ValueError("Not Implemented.")
        elif eventkey == self.controles[Controls.DOWN]:
            if self.controltype == ControlType.FOURDIRECTION or self.controltype == ControlType.UPDOWN:
                if self.entity.has_component(PositionComponent):
                    pos = self.entity.get_component(PositionComponent)
                    pos.position = Vec2(pos.position.x, pos.position.y + self.speed)
                elif self.entity.has_component(PhysicsComponent):
                    self.entity.get_component(PhysicsComponent).body.velocity = [0, -self.speed]

