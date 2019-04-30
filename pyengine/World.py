from pyengine.Systems import EntitySystem, MusicSystem, UISystem
from pyengine.Enums import WorldCallbacks

__all__ = ["World"]


class World:
    def __init__(self):
        self.state = None
        self.systems = [EntitySystem(self), MusicSystem(self), UISystem(self)]
        self.callbacks = {
            WorldCallbacks.FALL: None
        }

    def set_callback(self, callback, function):
        if type(callback) == WorldCallbacks:
            self.callbacks[callback] = function
        else:
            raise TypeError("Callback must be a WorldCallback (from WorldCallbacks Enum)")

    def call(self, callback, *param):
        if type(callback) == WorldCallbacks:
            if self.callbacks[callback] is not None:
                self.callbacks[callback](*param)
        else:
            raise TypeError("Callback must be a WorldCallback (from WorldCallbacks Enum)")

    def get_system(self, classe):
        for i in self.systems:
            if type(i) == classe:
                return i

    def has_system(self, classe):
        for i in self.systems:
            if type(i) == classe:
                return True
        return False

    def set_state(self, state):
        self.state = state

    def update(self):
        for i in self.systems:
            try:
                i.update()
            except AttributeError:
                pass

    def keypress(self, evt):
        for i in self.systems:
            try:
                i.keypress(evt)
            except AttributeError:
                pass

    def keyup(self, evt):
        for i in self.systems:
            try:
                i.keyup(evt)
            except AttributeError:
                pass

    def mousepress(self, evt):
        for i in self.systems:
            try:
                i.mousepress(evt)
            except AttributeError:
                pass

    def event(self, evt):
        if evt.type == self.systems[1].ENDSOUND:
            self.systems[1].next_song()

    def show(self, screen):
        for i in self.systems:
            try:
                i.show(screen)
            except AttributeError:
                pass

    def show_debug(self, screen):
        for i in self.systems:
            try:
                i.show_debug(screen)
            except AttributeError:
                pass
