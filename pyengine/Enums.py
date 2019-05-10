from enum import Enum

__all__ = ["ControlType", "MouseButton", "CollisionCauses", "WorldCallbacks", "Controls"]


class ControlType(Enum):
    FOURDIRECTION = 1
    CLASSICJUMP = 2
    DOUBLEJUMP = 3
    CLICKFOLLOW = 4
    LEFTRIGHT = 5
    UPDOWN = 6


class Controls(Enum):
    UPJUMP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


class MouseButton(Enum):
    LEFTCLICK = 1
    MIDDLECLICK = 2
    RIGHTCLICK = 3


class CollisionCauses(Enum):
    UNKNOWN = 1
    GRAVITY = 2
    LEFTCONTROL = 3
    RIGHTCONTROL = 4
    UPCONTROL = 5
    DOWNCONTROL = 6
    MOVECOMPONENT = 7


class WorldCallbacks(Enum):
    OUTOFWINDOW = 1
