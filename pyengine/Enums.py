from enum import Enum

__all__ = ["ControlType", "MouseButton", "CollisionCauses", "WorldCallbacks"]


class ControlType(Enum):
    FOURDIRECTION = 1
    CLASSICJUMP = 2
    DOUBLEJUMP = 3
    CLICKFOLLOW = 4


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
    FALL = 1
