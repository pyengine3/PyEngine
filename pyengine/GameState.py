from enum import Enum

__all__ = ["GameState", "StateCallbacks"]


class StateCallbacks(Enum):
    OUTOFWINDOW = 1


# StateCallbacks doit être défini avec les imports
from pyengine.Exceptions import NoObjectError
from pyengine.Systems import EntitySystem, MusicSystem, UISystem


class GameState:
    def __init__(self, name):
        self.name = name

        self.window = None
        self.systems = [EntitySystem(self), MusicSystem(self), UISystem(self)]
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
        for i in self.systems:
            if type(i) == classe:
                return i

    def has_system(self, classe):
        for i in self.systems:
            if type(i) == classe:
                return True
        return False

    def set_window(self, window):
        self.window = window

    def run(self):
        if self.window is None:
            raise NoObjectError("GameState is attached to any Window.")
        for i in self.systems:
            try:
                i.update()
            except AttributeError:
                pass

            try:
                i.show(self.window.screen)
            except AttributeError:
                pass

            if self.window.debug:
                try:
                    i.show_debug(self.window.screen)
                except AttributeError:
                    pass

    def keypress(self, evt):
        for i in self.systems:
            try:
                i.keypress(evt)
            except AttributeError:
                pass

    def mousepress(self, evt):
        for i in self.systems:
            try:
                i.mousepress(evt)
            except AttributeError:
                pass

    def keyup(self, evt):
        for i in self.systems:
            try:
                i.keyup(evt)
            except AttributeError:
                pass

    def event(self, evt):
        if evt.type == self.systems[1].ENDSOUND:
            self.systems[1].next_song()
        for i in self.systems:
            try:
                i.event(evt)
            except AttributeError:
                pass
