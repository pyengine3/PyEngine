from enum import Enum

__all__ = ["GameState", "StateCallbacks"]


class StateCallbacks(Enum):
    OUTOFWINDOW = 1


# StateCallbacks doit être défini avant les imports
from pyengine.Exceptions import NoObjectError
from pyengine.Systems import EntitySystem, MusicSystem, UISystem


class GameState:
    def __init__(self, name):
        self.name = name

        self.window = None
        self.systems = {
            "Entity": EntitySystem(self),
            "Music": MusicSystem(self),
            "UI" : UISystem(self)
        }
        self.callbacks = {
            StateCallbacks.OUTOFWINDOW: None
        }

    def set_callback(self, callback, function):
        if type(callback) == StateCallbacks:
            self.callbacks[callback] = function
        else:
            raise TypeError("Callback must be a StateCallback (from StateCallbacks Enum)")

    def call(self, callback, *param):
        if type(callback) == StateCallbacks:
            if self.callbacks[callback] is not None:
                self.callbacks[callback](*param)
        else:
            raise TypeError("Callback must be a StateCallback (from StateCallbacks Enum)")

    def get_system(self, classe):
        for i in self.systems.values():
            if type(i) == classe:
                return i

    def has_system(self, classe):
        for i in self.systems.values():
            if type(i) == classe:
                return True
        return False

    def set_window(self, window):
        self.window = window

    def run(self):
        if self.window is None:
            raise NoObjectError("GameState is attached to any Window.")

        self.systems["UI"].update()
        self.systems["UI"].show(self.window.screen)
        self.systems["Entity"].update()
        self.systems["Entity"].show(self.window.screen)
        self.systems["Entity"].show_debug(self.window.screen)

    def keypress(self, evt):
        self.systems["UI"].keypress(evt)
        self.systems["Entity"].keypress(evt)

    def mousepress(self, evt):
        self.systems["UI"].mousepress(evt)
        self.systems["Entity"].mousepress(evt)

    def keyup(self, evt):
        self.systems["UI"].keyup(evt)
        self.systems["Entity"].keyup(evt)

    def event(self, evt):
        if evt.type == self.systems["Music"].ENDSOUND:
            self.systems["Music"].next_song()
