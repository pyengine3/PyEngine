from enum import Enum

__all__ = ["World", "WorldCallbacks"]


class WorldCallbacks(Enum):
    OUTOFWINDOW = 1


# StateCallbacks doit être défini avant les imports
from pyengine.Exceptions import NoObjectError
from pyengine.Systems import EntitySystem, MusicSystem, UISystem, SoundSystem, CameraSystem


class World:
    def __init__(self, window):
        from pyengine import Window  # Define Window only on create world

        if not isinstance(window, Window):
            raise TypeError("Window have not Window as type")

        self.window = window
        self.systems = {
            "Entity": EntitySystem(self),
            "Music": MusicSystem(),
            "UI": UISystem(self),
            "Sound": SoundSystem(),
            "Camera": CameraSystem(self)
        }
        self.callbacks = {
            WorldCallbacks.OUTOFWINDOW: None
        }

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, val):
        self.__window = val

    def set_callback(self, callback, function):
        if type(callback) == WorldCallbacks:
            self.callbacks[callback] = function
        else:
            raise TypeError("Callback must be a StateCallback (from StateCallbacks Enum)")

    def call(self, callback, *param):
        if type(callback) == WorldCallbacks:
            if self.callbacks[callback] is not None:
                self.callbacks[callback](*param)  # Call function which is represented by the callback
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

        self.systems["Entity"].update()
        self.systems["UI"].update()
        self.systems["Camera"].update()
        self.systems["Entity"].show(self.window.screen)
        self.systems["UI"].show(self.window.screen)
        if self.window.debug:
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

    def event(self, evt):
        if evt.type == self.systems["Music"].ENDSOUND:
            self.systems["Music"].next_song()
