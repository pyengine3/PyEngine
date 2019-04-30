from pyengine.Exceptions import NoObjectError
from pyengine.Enums import ControlType, MouseButton, CollisionCauses
from pyengine.Components.PositionComponent import PositionComponent
from pyengine.Components.PhysicsComponent import PhysicsComponent
from pygame import locals as const

__all__ = ["ControlComponent"]


class ControlComponent:
    name = "ControlComponent"

    def __init__(self, controltype, speed=5):
        self.entity = None
        self.controltype = controltype
        self.speed = speed
        self.goto = (-1, -1)
        self.jumping = False

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
            if eventkey == const.K_UP:
                self.jumping = False

    def keypress(self, evt):
        eventkey = evt.key
        if not self.entity.has_component(PositionComponent):
            raise NoObjectError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        if self.controltype == ControlType.FOURDIRECTION:
            pos = position.get_position()
            cango = True
            if eventkey == const.K_LEFT:
                pos = [position.x - self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.LEFTCONTROL)
            if eventkey == const.K_RIGHT:
                pos = [position.x + self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.RIGHTCONTROL)
            if eventkey == const.K_UP:
                pos = [position.x, position.y - self.speed]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.UPCONTROL)
            if eventkey == const.K_DOWN:
                pos = [position.x, position.y + self.speed]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.DOWNCONTROL)

            if cango:
                self.entity.get_component(PositionComponent).set_position(pos)
        elif self.controltype == ControlType.CLASSICJUMP or self.controltype == ControlType.DOUBLEJUMP:
            if not self.entity.has_component(PhysicsComponent):
                raise NoObjectError("Entity must have PhysicsComponent")
            phys = self.entity.get_component(PhysicsComponent)
            pos = position.get_position()
            cango = True
            if eventkey == const.K_LEFT:
                pos = [position.x - self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.LEFTCONTROL)
            if eventkey == const.K_RIGHT:
                pos = [position.x + self.speed, position.y]
                if self.entity.has_component(PhysicsComponent):
                    cango = self.entity.get_component(PhysicsComponent).can_go(pos, CollisionCauses.RIGHTCONTROL)

            if self.entity.has_component(PhysicsComponent):
                cango = self.entity.get_component(PhysicsComponent).can_go(pos)
            if cango:
                self.entity.get_component(PositionComponent).set_position(pos)

            if self.controltype == ControlType.CLASSICJUMP:
                if eventkey == const.K_UP and phys.grounded and not self.jumping:
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity_force = -phys.max_gravity_force
            elif self.controltype == ControlType.DOUBLEJUMP:
                if eventkey == const.K_UP and (phys.grounded or phys.doublejump) and not self.jumping:
                    if not phys.grounded:
                        phys.doublejump = False
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity_force = -phys.max_gravity_force


