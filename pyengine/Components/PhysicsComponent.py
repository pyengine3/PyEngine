from pyengine.Exceptions import NoObjectError
from pyengine.Components import SpriteComponent, PositionComponent
from pyengine.Enums import CollisionCauses
import pygame

__all__ = ["PhysicsComponent"]


class PhysicsComponent:
    name = "PhysicsComponent"

    def __init__(self, affectbygravity=True, gravity_force=5):
        self.entity = None
        self.affectbygravity = affectbygravity
        self.gravity_force = gravity_force
        self.max_gravity_force = gravity_force
        self.timegravity = 5
        self.grounded = False
        self.doublejump = True
        self.callback = None

    def set_entity(self, entity):
        self.entity = entity

    def set_callback(self, function):
        self.callback = function

    def can_go(self, position, createdby=CollisionCauses.UNKNOWN):
        if not self.entity.has_component(SpriteComponent):
            raise NoObjectError("Entity must have SpriteComponent.")
        gosprite = pygame.sprite.Sprite()
        gosprite.rect = pygame.rect.Rect(position[0], position[1], self.entity.image.get_width(),
                                         self.entity.image.get_height())
        collision = pygame.sprite.spritecollide(gosprite, self.entity.system.entities, False, None)
        for i in collision:
            if i.has_component(PhysicsComponent) and i.id != self.entity.id:
                if self.callback is not None:
                    self.callback(i, createdby)
                return False
        return True

    def update_gravity(self):
        if not self.entity.has_component(PositionComponent):
            raise NoObjectError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        if self.affectbygravity:
            if self.can_go([position.x, position.y + self.gravity_force], CollisionCauses.GRAVITY):
                self.grounded = False
                position.set_position([position.x, position.y + self.gravity_force])
            elif self.gravity_force > 0:
                self.grounded = True
                self.doublejump = True
                self.gravity_force = 2

            if self.timegravity <= 0 and self.gravity_force < self.max_gravity_force and not self.grounded:
                self.gravity_force += 1
                self.timegravity = 5
            self.timegravity -= 1
