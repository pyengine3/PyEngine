from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2
import pygame
from enum import Enum

__all__ = ["PhysicsComponent", "CollisionCauses"]


class CollisionCauses(Enum):
    UNKNOWN = 1
    GRAVITY = 2
    LEFTCONTROL = 3
    RIGHTCONTROL = 4
    UPCONTROL = 5
    DOWNCONTROL = 6
    MOVECOMPONENT = 7
    MOUSECLICK = 8
    MOUSEFOLLOW = 9


class CollisionInfos:
    def __init__(self, cause: CollisionCauses, cote: str):
        self.cause = cause
        self.cote = cote


class PhysicsComponent:
    def __init__(self, affectbygravity: bool = True, callback=None, gravity_force: int = 5):
        self.entity = None
        self.affectbygravity = affectbygravity
        self.gravity = gravity_force
        self.max_gravity_force = gravity_force
        self.timegravity = 5
        self.grounded = False
        self.doublejump = True
        self.callback = callback

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        self.__gravity = gravity

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    @property
    def callback(self):
        return self.__callback

    @callback.setter
    def callback(self, function):
        self.__callback = function

    def can_go(self, position: Vec2, createdby: CollisionCauses = CollisionCauses.UNKNOWN,
               makecallback: bool = True) -> bool:
        gosprite = pygame.sprite.Sprite()
        gosprite.rect = pygame.rect.Rect(position.x, position.y, self.entity.image.get_width(),
                                         self.entity.image.get_height())
        collision = pygame.sprite.spritecollide(gosprite, self.entity.system.entities, False, None)
        for i in collision:
            if i.has_component(PhysicsComponent) and i.identity != self.entity.identity:
                if self.callback is not None and makecallback:
                    entitypos = self.entity.get_component(PositionComponent).position
                    ipos = i.get_component(PositionComponent).position
                    if ipos.x - self.entity.image.get_width() < entitypos.x < ipos.x + i.image.get_width():
                        if entitypos.y + self.entity.image.get_height() <= ipos.y:
                            cinfos = CollisionInfos(createdby, "haut")
                        else:
                            cinfos = CollisionInfos(createdby, "bas")
                    elif entitypos.x + self.entity.image.get_width() <= ipos.x:
                        cinfos = CollisionInfos(createdby, "gauche")
                    else:
                        cinfos = CollisionInfos(createdby, "droite")
                    self.callback(i, cinfos)
                return False
        return True

    def update_gravity(self):
        if self.affectbygravity:
            if self.entity.has_component(PositionComponent):
                position = self.entity.get_component(PositionComponent)
                if self.can_go(Vec2(position.position.x, position.position.y + self.gravity), CollisionCauses.GRAVITY):
                    self.grounded = False
                    position.position = Vec2(position.position.x, position.position.y + self.gravity)
                elif self.gravity > 0:
                    self.grounded = True
                    self.doublejump = True
                    self.gravity = 2

                if self.timegravity <= 0 and self.gravity < self.max_gravity_force and not self.grounded:
                    self.gravity += 1
                    self.timegravity = 5
                self.timegravity -= 1
