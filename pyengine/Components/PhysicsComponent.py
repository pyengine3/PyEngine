from pyengine.Exceptions import ComponentIntializedError, NoComponentError
from pyengine.Components.SpriteComponent import SpriteComponent
from pyengine.Components.PositionComponent import PositionComponent
import pygame

__all__ = ["PhysicsComponent"]


class PhysicsComponent:
    name = "PhysicsComponent"

    def __init__(self):
        self.entity = None
        self.affectbygravity = True
        self.gravity_force = 0
        self.max_gravity_force = 0
        self.timegravity = 5
        self.grounded = False
        self.initialized = False
        self.callback = None

    def initialize(self, entity, affectbygravity=True, gravity_force=5):
        if self.initialized:
            raise ComponentIntializedError("PhysicsComponent already initialized")
        self.initialized = True
        self.entity = entity
        self.affectbygravity = affectbygravity
        self.gravity_force = gravity_force
        self.max_gravity_force = gravity_force

    def set_callback(self, function):
        self.callback = function

    def can_go(self, position, make_callback=True):
        if not self.entity.has_component(SpriteComponent):
            raise NoComponentError("Entity must have SpriteComponent.")
        gosprite = pygame.sprite.Sprite()
        gosprite.rect = pygame.rect.Rect(position[0], position[1], self.entity.image.get_width(),
                                         self.entity.image.get_height())
        collision = pygame.sprite.spritecollide(gosprite, self.entity.system.entities, False, None)
        for i in collision:
            if i.has_component(PhysicsComponent) and i.id != self.entity.id:
                if self.callback is not None and make_callback:
                    self.callback(self.entity.id, i.id)
                return False
        return True

    def update_gravity(self):
        if not self.entity.has_component(PositionComponent):
            raise NoComponentError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        if self.can_go([position.x, position.y + self.gravity_force], False) and self.affectbygravity:
            self.grounded = False
            position.set_position([position.x, position.y + self.gravity_force])
        else:
            self.grounded = True
            self.gravity_force = 2

        if self.timegravity <= 0 and self.gravity_force < self.max_gravity_force and not self.grounded:
            self.gravity_force += 1
            self.timegravity = 5
        self.timegravity -= 1
