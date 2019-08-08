from pyengine.Exceptions import NoObjectError
from pyengine.Systems import EntitySystem, MusicSystem, UISystem, SoundSystem, CameraSystem
from pyengine.Components import PhysicsComponent
from typing import Type, Union
from pyengine.Utils import loggers
import pymunk
from pymunk import pygame_util

sunion = Union[EntitySystem, MusicSystem, UISystem, SoundSystem, CameraSystem]
stypes = Union[Type[EntitySystem], Type[MusicSystem], Type[UISystem], Type[SoundSystem], Type[CameraSystem]]

__all__ = ["World"]


class World:
    def __init__(self, window, gravity=None):
        from pyengine import Window  # Define Window only on create world

        if not isinstance(window, Window):
            raise TypeError("Window have not Window as type")

        if gravity is None:
            gravity = [0, -900]

        self.window = window
        self.systems = {
            "Entity": EntitySystem(self),
            "Music": MusicSystem(),
            "UI": UISystem(self),
            "Sound": SoundSystem(),
            "Camera": CameraSystem(self)
        }
        self.space = pymunk.Space()
        self.gravity = gravity
        self.__collision = self.space.add_default_collision_handler()
        self.__collision.pre_solve = self.collision

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, val):
        self.space.gravity = val
        self.__gravity = val

    def collision(self, arb, space, data):
        ret = True
        e = []
        for i in arb.shapes:
            for j in [e for e in self.systems["Entity"].entities if e.has_component(PhysicsComponent)]:
                phys = j.get_component(PhysicsComponent)
                if phys.shape == i:
                    e.append(j)
                    break
        for i in e:
            phys = i.get_component(PhysicsComponent)
            if phys.callback is not None:
                temp = e.copy()
                temp.remove(i)
                phys.callback(i, temp, space, data)
        return ret


    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, val):
        self.__window = val

    def get_system(self, classe: stypes) -> sunion:
        liste = [i for i in self.systems.values() if type(i) == classe]
        if len(liste):
            return liste[0]
        loggers.get_logger("PyEngine").warning("Try to get "+str(classe)+" but World don't have it")

    def update(self):
        if self.window is None:
            raise NoObjectError("World is attached to any Window.")

        self.space.step(1/60)

        self.systems["Entity"].update()
        self.systems["UI"].update()

        if self.systems["Camera"].entity_follow is not None:
            self.systems["Camera"].update()

    def show(self):
        if self.window is None:
            raise NoObjectError("World is attached to any Window.")
        self.systems["Entity"].show(self.window.screen)
        self.systems["UI"].show(self.window.screen)
        if self.window.debug:
            draw_options = pygame_util.DrawOptions(self.window.screen)

            self.space.debug_draw(draw_options)
            self.systems["Entity"].show_debug(self.window.screen)
            self.systems["UI"].show_debug(self.window.screen)

    def keypress(self, evt):
        self.systems["Entity"].keypress(evt)
        self.systems["UI"].keypress(evt)

    def mousepress(self, evt):
        self.systems["Entity"].mousepress(evt)
        self.systems["UI"].mousepress(evt)

    def keyup(self, evt):
        self.systems["Entity"].keyup(evt)
        self.systems["UI"].keyup(evt)

    def mousemotion(self, evt):
        self.systems["UI"].mousemotion(evt)
        self.systems["Entity"].mousemotion(evt)

    def event(self, evt):
        if evt.type == self.systems["Music"].ENDSOUND:
            self.systems["Music"].next_song()

    def stop_world(self):
        self.systems["Entity"].stop_world()

    def start_world(self):
        pass
