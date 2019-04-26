import pygame
from pyengine.Exceptions import WrongComponentError, NoComponentError
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

    def add_components(self, component, *param):
        if component not in [PositionComponent, SpriteComponent, ControlComponent, PhysicsComponent,
                             TextComponent, LifeBarComponent]:
            raise WrongComponentError("Entity can't have "+str(component)+" as component.")
        component = eval(component.name+"()")
        if param is not None:
            component.initialize(self, *param)
        else:
            component.initialize(self)
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
        raise NoComponentError("Entity have no "+str(component)+" as component.")

    def update(self):
        if self.has_component(PhysicsComponent):
            self.get_component(PhysicsComponent).update_gravity()
        if self.has_component(PositionComponent):
            position = self.get_component(PositionComponent)
            if position.y >= self.system.world.window.height:
                self.system.world.call(WorldCallbacks.FALL, self)
        if self.has_component(ControlComponent):
            self.get_component(ControlComponent).update()
