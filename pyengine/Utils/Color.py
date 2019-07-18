from enum import Enum
from typing import Tuple
from pyengine.Utils import clamp
import pygame

__all__ = ["Color", "Colors"]


class Color(pygame.Color):
    def __init__(self, r: int = 255, g: int = 255, b: int = 255, a: int = 255):
        super(Color, self).__init__(r, g, b, a)

    def get(self) -> Tuple[int, int, int, int]:
        return self.r, self.g, self.b, self.a

    def set(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        self.r = color.r
        self.g = color.g
        self.b = color.b
        self.a = color.a
        return self

    def to_hex(self):
        return ("#"+hex(self.r)[2:]+hex(self.g)[2:]+hex(self.b)[2:]+hex(self.a)[2:]).upper()

    def from_hex(self, hexa: str):
        if len(hexa) == 7:
            self.r = int(hexa[1:3], 16)
            self.g = int(hexa[3:5], 16)
            self.b = int(hexa[5:7], 16)
            self.a = 255
        elif len(hexa) == 9:
            self.r = int(hexa[1:3], 16)
            self.g = int(hexa[3:5], 16)
            self.b = int(hexa[5:7], 16)
            self.a = int(hexa[7:9], 16)
        else:
            raise ValueError("Hexa must be a 7 or 9 lenght string (#RRGGBBAA)")

    def darker(self, nb=1):
        nb = clamp(nb, 1)
        r = clamp(self.r - 10*nb, 0, 255)
        b = clamp(self.b - 10*nb, 0, 255)
        g = clamp(self.g - 10*nb, 0, 255)
        return Color(r, g, b, self.a)

    def lighter(self, nb=1):
        nb = clamp(nb, 1)
        r = clamp(self.r + 10*nb, 0, 255)
        b = clamp(self.b + 10*nb, 0, 255)
        g = clamp(self.g + 10*nb, 0, 255)
        return Color(r, g, b, self.a)

    def __repr__(self) -> str:
        return str(self.get())


class Colors(Enum):
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    FUCHSIA = Color(255, 0, 255)
    GRAY = Color(128, 128, 128)
    LIME = Color(0, 128, 0)
    MAROON = Color(128, 0, 0)
    NAVYBLUE = Color(0, 0, 128)
    OLIVE = Color(128, 128, 0)
    PURPLE = Color(128, 0, 128)
    SILVER = Color(192, 192, 192)
    TEAL = Color(0, 128, 128)
    YELLOW = Color(255, 255, 0)
    ORANGE = Color(255, 128, 0)
    CYAN = Color(0, 255, 255)
