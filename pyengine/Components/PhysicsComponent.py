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


class PhysicsComponent:
    def __init__(self, affectbygravity: bool = True, gravity_force: int = 5):
        self.entity = None
        self.affectbygravity = affectbygravity
        self.gravity = gravity_force
        self.max_gravity_force = gravity_force
        self.timegravity = 5
        self.grounded = False
        self.doublejump = True
        self.callback = None

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

    def can_go(self, position: Vec2, createdby: CollisionCauses = CollisionCauses.UNKNOWN) -> bool:
        gosprite = pygame.sprite.Sprite()
        gosprite.rect = pygame.rect.Rect(position.x, position.y, self.entity.image.get_width(),
                                         self.entity.image.get_height())
        collision = pygame.sprite.spritecollide(gosprite, self.entity.system.entities, False, None)
        for i in collision:
            if i.has_component(PhysicsComponent) and i.identity != self.entity.identity:
                if self.callback is not None:
                    self.callback(i, createdby)
                return False
        return True

    def update_gravity(self):
        if self.entity.has_component(PositionComponent):
            position = self.entity.get_component(PositionComponent)
            if self.affectbygravity:
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
