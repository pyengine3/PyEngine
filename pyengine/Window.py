from pyengine.World import World
from pyengine.Utils import Color, Colors, loggers

import pygame
import os
import logging
from pygame import locals as const
from typing import Union, Any
from enum import Enum

__all__ = ["Window", "WindowCallbacks"]


class WindowCallbacks(Enum):
    OUTOFWINDOW = 1
    STOPWINDOW = 2
    CHANGEWORLD = 3


class Window:
    def __init__(self, width: int, height: int, color: Color = Colors.BLACK.value,
                 title: str = "PyEngine", icon: Union[None, str] = None,
                 update_rate: int = 60, debug: bool = False):
        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(title)

        self.screen = pygame.display.set_mode((width, height))
        pygame.scrap.init()
        pygame.time.set_timer(const.USEREVENT, 500)

        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.update_rate= update_rate
        self.__world = World(self)
        self.is_running = False
        self.debug = debug
        self.color = color
        self.debugfont = pygame.font.SysFont("arial", 15)

        self.callbacks = {
            WindowCallbacks.OUTOFWINDOW: None,
            WindowCallbacks.STOPWINDOW: None,
            WindowCallbacks.CHANGEWORLD: None
        }

    @property
    def title(self):
        return pygame.display.get_caption()[0]

    @title.setter
    def title(self, title):
        pygame.display.set_caption(title)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        self.__color = color

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, size):
        self.width, self.height = size
        pygame.display.set_mode(size)

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug):
        self.__debug = debug

        if debug:
            os.environ['SDL_DEBUG'] = '1'
            for n, l in loggers.get_all():
                l.setLevel(logging.DEBUG)
        else:
            try:
                del os.environ['SDL_DEBUG']
            except KeyError:
                pass
            for n, l in loggers.get_all():
                l.setLevel(logging.INFO)

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, world):
        self.__world.stop_world()
        self.call(WindowCallbacks.CHANGEWORLD, self.__world, world)
        self.__world = world
        self.__world.start_world()

    def __process_event(self, evt):
        if evt.type == const.QUIT:
            self.stop()
        elif evt.type == const.KEYDOWN:
            self.world.keypress(evt)
        elif evt.type == const.MOUSEBUTTONDOWN:
            self.world.mousepress(evt)
        elif evt.type == const.KEYUP:
            self.world.keyup(evt)
        elif evt.type == const.MOUSEMOTION:
            self.world.mousemotion(evt)
        else:
            self.world.event(evt)

    def set_callback(self, callback: WindowCallbacks, function: Any) -> None:
        if type(callback) == WindowCallbacks:
            self.callbacks[callback] = function
        else:
            raise TypeError("Callback must be a WindowCallback (from WindowCallback Enum)")

    def call(self, callback: WindowCallbacks, *param) -> None:
        if type(callback) == WindowCallbacks:
            if self.callbacks[callback] is not None:
                self.callbacks[callback](*param)  # Call function which is represented by the callback
        else:
            raise TypeError("Callback must be a WindowCallback (from WindowCallback Enum)")

    def stop(self) -> None:
        self.is_running = False
        self.call(WindowCallbacks.STOPWINDOW)

    def run(self) -> None:
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == const.USEREVENT:
                    if self.debug:
                        print("FPS : {}".format(int(self.clock.get_fps())))
                self.__process_event(event)

            self.screen.fill(self.color.get())

            self.world.run()

            self.clock.tick(self.update_rate)
            pygame.display.update()
        pygame.quit()
