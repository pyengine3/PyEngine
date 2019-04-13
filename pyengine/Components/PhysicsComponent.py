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
        self.initialized = False

    def initialize(self, entity, affectbygravity=True, gravity_force=5):
        if self.initialized:
            raise ComponentIntializedError("PhysicsComponent already initialized")
        self.entity = entity
        self.affectbygravity = affectbygravity
        self.gravity_force = gravity_force

    def can_go(self, position):
        if not self.entity.has_component(SpriteComponent):
            raise NoComponentError("Entity must have SpriteComponent.")
        gosprite = pygame.sprite.Sprite()
        gosprite.rect = pygame.rect.Rect(position[0], position[1], self.entity.image.get_width(),
                                         self.entity.image.get_height())
        collision = pygame.sprite.spritecollide(gosprite, self.entity.world.entities, False, None)
        for i in collision:
            if i.has_component(PhysicsComponent) and i.id != self.entity.id:
                return False
        return True

    def update_gravity(self):
        if not self.entity.has_component(PositionComponent):
            raise NoComponentError("Entity must have PositionComponent.")
        position = self.entity.get_component(PositionComponent)
        if self.can_go([position.x, position.y + self.gravity_force]) and self.affectbygravity:
            position.set_position([position.x, position.y + self.gravity_force])
