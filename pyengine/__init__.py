try:
    from pyengine.Window import Window, WindowCallbacks
    from pyengine.World import World
    from pyengine.Components.ControlComponent import ControlType, Controls, MouseButton
    from pygame import locals as const
except ModuleNotFoundError:
    pass

__version__ = "1.5.1"
