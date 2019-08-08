from typing import Union, Type

import pygame

from pyengine.Components import *
from pyengine.Utils.Logger import loggers

cunion = Union[PositionComponent, SpriteComponent, ControlComponent,
               PhysicsComponent, TextComponent, LifeComponent, MoveComponent, AnimComponent]
ctypes = Union[Type[PositionComponent], Type[SpriteComponent], Type[ControlComponent],
               Type[PhysicsComponent], Type[TextComponent], Type[LifeComponent], Type[MoveComponent],
               Type[AnimComponent]]

__all__ = ["Entity"]


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.identity = -1
        self.components = []
        self.attachedentities = []
        self.__system = None
        self.image = None

    @property
    def identity(self):
        return self.__identity

    @identity.setter
    def identity(self, identity):
        self.__identity = identity

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        if self.has_component(PhysicsComponent) and self.has_component(PositionComponent):
            self.get_component(PhysicsComponent).update_pos(self.get_component(PositionComponent).position.coords)

    def attach_entity(self, entity):
        self.attachedentities.append(entity)

    def add_component(self, component: cunion) -> cunion:
        if isinstance(component, (PositionComponent, SpriteComponent, ControlComponent, PhysicsComponent,
                                  TextComponent, LifeComponent, MoveComponent, AnimComponent)):
            if isinstance(component, tuple([type(c) for c in self.components])):
                raise TypeError("Entity already have " + str(component) + " as component.")
            component.entity = self
            self.components.append(component)
            return component
        else:
            raise TypeError("Entity can't have "+str(component)+" as component.")

    def remove_component(self, component: ctypes) -> None:
        for i in [i for i in self.components if isinstance(i, component)]:
            loggers.get_logger("PyEngine").debug("Deleting "+str(component))
            del self.components[self.components.index(i)]
        loggers.get_logger("PyEngine").info("Deleting component can be dangerous.")

    def has_component(self, component: ctypes) -> bool:
        if len([c for c in self.components if isinstance(c, component)]):
            return True
        return False

    def get_component(self, component: ctypes) -> cunion:
        liste = [i for i in self.components if isinstance(i, component)]
        if len(liste):
            return liste[0]
        loggers.get_logger("PyEngine").warning("Try to get "+str(component)+" but Entity don't have it")

    def update(self):
        if self.has_component(PhysicsComponent):
            self.get_component(PhysicsComponent).update()

        if self.has_component(ControlComponent):
            self.get_component(ControlComponent).update()

        if self.has_component(MoveComponent):
            self.get_component(MoveComponent).update()

        if self.has_component(AnimComponent):
            self.get_component(AnimComponent).update()
