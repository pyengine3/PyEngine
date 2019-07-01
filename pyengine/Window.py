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
                 title: str = "PyEngine", icon: Union[None, str] = None, debug: bool = False):
        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(title)

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.__world = World(self)
        self.launch = True
        self.debug = debug
        self.color = color
        self.debugfont = pygame.font.SysFont("arial", 15)

        pygame.key.set_repeat(1, 1)

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
        self.call(WindowCallbacks.CHANGEWORLD, self.__world, world)
        self.__world = world

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
        self.launch = False
        self.call(WindowCallbacks.STOPWINDOW)

    def is_running(self):
        return self.launch

    def run(self) -> None:
        while self.launch:
            for event in pygame.event.get():
                self.__process_event(event)

            self.screen.fill(self.color.get())
            self.clock.tick(60)

            self.world.run()

            pygame.display.update()
        pygame.quit()
