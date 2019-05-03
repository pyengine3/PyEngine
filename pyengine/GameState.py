from pyengine.World import World
from pyengine.Exceptions import NoObjectError

__all__ = ["GameState"]


class GameState:
    def __init__(self, name):
        self.world = World()
        self.world.set_state(self)
        self.name = name
        self.window = None

    def set_world(self, world):
        if not isinstance(world, World):
            raise TypeError("Argument is not type of "+str(World)+" but "+str(type(world))+".")
        self.world = world
        world.set_state(self)

    def get_world(self):
        return self.world

    def set_window(self, window):
        self.window = window

    def run(self):
        if self.window is None:
            raise NoObjectError("GameState is attached to any Window.")
        self.world.update()
        self.world.show(self.window.screen)
        if self.window.debug:
            self.world.show_debug(self.window.screen)

    def keypress(self, evt):
        if self.world is not None:
            self.world.keypress(evt)

    def mousepress(self, evt):
        if self.world is not None:
            self.world.mousepress(evt)

    def keyup(self, evt):
        if self.world is not None:
            self.world.keyup(evt)

    def event(self, evt):
        if self.world is not None:
            self.world.event(evt)
