from pyengine.World import World
from pyengine.Exceptions import NoWorldError, GameStateIntializedError

__all__ = ["GameState"]


class GameState:
    def __init__(self, name):
        self.world = None
        self.name = name
        self.window = None

    def set_world(self, world):
        if type(world) != World:
            raise TypeError("Argument is not a World")
        self.world = world
        world.set_state(self)

    def get_world(self):
        return self.world

    def set_window(self, window):
        self.window = window

    def run(self):
        if self.window is None:
            raise GameStateIntializedError("GameState is not initilized.")
        if self.world is None:
            raise NoWorldError("GameState have no World.")
        self.world.update()
        self.world.show(self.window.screen)
        if self.window.debug:
            self.world.show_debug(self.window.screen)

    def keypress(self, key):
        if self.world is not None:
            self.world.keypress(key)

    def mousepress(self, button, pos):
        if self.world is not None:
            self.world.mousepress(button, pos)

    def keyup(self, key):
        if self.world is not None:
            self.world.keyup(key)

    def event(self, evt):
        if self.world is not None:
            self.world.event(evt)
