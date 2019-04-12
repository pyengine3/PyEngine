import pygame
from pyengine.Exceptions import WrongComponent, NoComponent
from pyengine.Components import *

__all__ = ["Entity"]


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.id = -1
        self.components = []
    def set_id(self, identity):
        self.id = identity

    def get_id(self):
        return self.id


    def add_components(self, component, *param):
        if component not in [PositionComponent, SpriteComponent]:
            raise WrongComponent("Entity can have "+str(component)+" as component.")
        component = eval(component.name+"()")
        if param is not None:
            component.initialize(self, *param)
        self.components.append(component)

    def has_component(self, component):
        for i in self.components:
            if type(i) == component:
                return True
        return False

    def get_component(self, component):
        for i in self.components:
            if type(i) == component:
                return i
        raise NoComponent("Entity have no "+str(component)+" as component.")
