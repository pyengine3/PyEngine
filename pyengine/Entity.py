import pygame
from pyengine.Exceptions import WrongComponent, NoComponent

__all__ = ["Entity"]


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.id = -1
        self.components = []

    def add_components(self, component):
        if component not in []:
            raise WrongComponent("Entity can have "+str(type(component))+" as component.")
        component = eval(component+"()")
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
