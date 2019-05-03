import pygame
from pyengine.Exceptions import WrongObjectError
from pyengine.Components import *
from pyengine.Enums import WorldCallbacks

__all__ = ["Entity"]


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.id = -1
        self.components = []
        self.attachedentities = []
        self.system = None
        self.image = None

    def set_id(self, identity):
        self.id = identity

    def get_id(self):
        return self.id

    def set_system(self, system):
        self.system = system

    def attach_entity(self, entity):
        self.attachedentities.append(entity)

    def add_component(self, component):
        if type(component) not in [PositionComponent, SpriteComponent, ControlComponent, PhysicsComponent,
                                   TextComponent, LifeBarComponent, MoveComponent]:
            raise WrongObjectError("Entity can't have "+str(component)+" as component.")
        component.set_entity(self)
        self.components.append(component)
        return component

    def has_component(self, component):
        for i in self.components:
            if type(i) == component:
                return True
        return False

    def get_component(self, component):
        for i in self.components:
            if type(i) == component:
                return i

    def update(self):
        if self.has_component(PhysicsComponent):
            self.get_component(PhysicsComponent).update_gravity()
        if self.has_component(PositionComponent):
            position = self.get_component(PositionComponent)
            if position.y >= self.system.world.state.window.height:
                self.system.world.call(WorldCallbacks.FALL, self)
        if self.has_component(ControlComponent):
            self.get_component(ControlComponent).update()
        if self.has_component(MoveComponent):
            self.get_component(MoveComponent).update()
