import pygame
from pyengine.Exceptions import NoWorldError
from pyengine.World import World
from pygame import locals as const

__all__ = ["Window"]


class Window:
    def __init__(self, width, height):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.world = None
        self.launch = True

        pygame.key.set_repeat(1, 1)

    def get_size(self):
        return [self.width, self.height]

    def set_world(self, world):
        if type(world) != World:
            raise TypeError("Argument is not a World")
        self.world = world
        self.world.set_window(self)

    def get_world(self):
        return self.world

    def process_event(self, evt):
        if evt.type == const.QUIT:
            self.launch = False
        if evt.type == const.KEYDOWN:
            self.world.keypress(evt.key)

    def run(self):
        if self.world is None:
            raise NoWorldError("Window have no world")
        while self.launch:
            for event in pygame.event.get():
                self.process_event(event)

            self.screen.fill((0, 0, 0))
            self.clock.tick(60)

            self.world.update()
            self.world.show(self.screen)

            pygame.display.update()
        pygame.quit()
