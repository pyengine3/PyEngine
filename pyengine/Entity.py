import pygame
from pyengine.Components import *
from typing import Union, Type
from pyengine.Utils import loggers

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
        self.system = None
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

    def attach_entity(self, entity):
        self.attachedentities.append(entity)

    def add_component(self, component: cunion) -> cunion:
        found = False
        for i in [PositionComponent, SpriteComponent, ControlComponent, PhysicsComponent,
                  TextComponent, LifeComponent, MoveComponent, AnimComponent]:
            if isinstance(component, i):
                found = True
                break
        if not found:
            raise TypeError("Entity can't have "+str(component)+" as component.")
        if component in [type(c) for c in self.components]:
            raise TypeError("Entity already have "+str(component)+" as component.")
        component.entity = self
        self.components.append(component)
        return component

    def remove_component(self, component: ctypes) -> None:
        for i in self.components:
            if isinstance(i, component):
                loggers.get_logger("PyEngine").debug("Deleting "+str(component))
                del self.components[self.components.index(i)]
        loggers.get_logger("PyEngine").info("Deleting component can be dangerous.")

    def has_component(self, component: ctypes) -> bool:
        for i in self.components:
            if isinstance(i, component):
                return True
        return False

    def get_component(self, component: ctypes) -> cunion:
        for i in self.components:
            if isinstance(i, component):
                return i
        loggers.get_logger("PyEngine").warning("Try to get "+str(component)+" but Entity don't have it")

    def update(self):
        if self.has_component(PhysicsComponent):
            self.get_component(PhysicsComponent).update_gravity()

        if self.has_component(PositionComponent):
            from pyengine import WindowCallbacks
            # Verify if entity is not out of window
            position = self.get_component(PositionComponent)
            if position.position.y >= self.system.world.window.height - self.image.get_rect().height:
                self.system.world.window.call(WindowCallbacks.OUTOFWINDOW, self, position.position)
            elif position.position.y < 0:
                self.system.world.window.call(WindowCallbacks.OUTOFWINDOW, self, position.position)
            if position.position.x >= self.system.world.window.width - self.image.get_rect().width:
                self.system.world.window.call(WindowCallbacks.OUTOFWINDOW, self, position.position)
            elif position.position.x < 0:
                self.system.world.window.call(WindowCallbacks.OUTOFWINDOW, self, position.position)

        if self.has_component(ControlComponent):
            self.get_component(ControlComponent).update()

        if self.has_component(MoveComponent):
            self.get_component(MoveComponent).update()

        if self.has_component(AnimComponent):
            self.get_component(AnimComponent).update()
