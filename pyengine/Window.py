import pygame
from pyengine.Exceptions import NoWorld
from pyengine.World import World
from pygame import locals as const

__all__ = ["Window"]


class Window:
    def __init__(self, width, height):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.world = None
        self.launch = True

    def get_size(self):
        return [self.width, self.height]

    def set_world(self, world):
        if type(world) != World:
            raise TypeError("Argument is not a World")
        self.world = world

    def get_world(self):
        return self.world

    def process_event(self, evt):
        if evt.type == const.QUIT:
            self.launch = False

    def run(self):
        if self.world is None:
            raise NoWorld("Window have no world")
        while self.launch:
            for event in pygame.event.get():
                self.process_event(event)
        pygame.quit()
