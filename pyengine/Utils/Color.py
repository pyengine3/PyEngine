from enum import Enum
from typing import Tuple
from pyengine.Utils import clamp

__all__ = ["Color", "Colors"]


class Color:
    def __init__(self, r: int = 255, g: int = 255, b: int = 255):
        self.r = r
        self.g = g
        self.b = b

    def get(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    def set(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        self.r = color.r
        self.g = color.g
        self.b = color.b
        return self

    def to_hex(self):
        return ("#"+hex(self.r)[2:]+hex(self.g)[2:]+hex(self.b)[2:]).upper()

    def from_hex(self, hexa: str):
        if len(hexa) != 7:
            raise ValueError("Hexa must be a 7 lenght string (#XXXXXX)")
        self.r = int(hexa[1:3], 16)
        self.g = int(hexa[3:5], 16)
        self.b = int(hexa[5:7], 16)

    def darker(self):
        r = self.r
        b = self.b
        g = self.g
        if self.r >= 10:
            r -= 10
        if self.g >= 10:
            g -= 10
        if self.b >= 10:
            b -= 10
        return Color(r, g, b)

    def lighter(self):
        r = self.r
        b = self.b
        g = self.g
        if self.r <= 245:
            r += 10
        if self.g <= 245:
            g += 10
        if self.b <= 245:
            b += 10
        return Color(r, g, b)

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Color can only be add with Color")
        r = clamp(self.r + other.r, 0, 255)
        b = clamp(self.b + other.b, 0, 255)
        g = clamp(self.g + other.g, 0, 255)
        return Color(r, g, b)

    def __sub__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Color can only be add with Color")
        r = clamp(self.r - other.r, 0, 255)
        b = clamp(self.b - other.b, 0, 255)
        g = clamp(self.g - other.g, 0, 255)
        return Color(r, g, b)

    def __eq__(self, other) -> bool:
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __repr__(self) -> str:
        return str(self.get())


class Colors(Enum):
    WHITE: Color = Color(255, 255, 255)
    BLACK: Color = Color(0, 0, 0)
    RED: Color = Color(255, 0, 0)
    GREEN: Color = Color(0, 255, 0)
    BLUE: Color = Color(0, 0, 255)
    FUCHSIA: Color = Color(255, 0, 255)
    GRAY: Color = Color(128, 128, 128)
    LIME: Color = Color(0, 128, 0)
    MAROON: Color = Color(128, 0, 0)
    NAVYBLUE: Color = Color(0, 0, 128)
    OLIVE: Color = Color(128, 128, 0)
    PURPLE: Color = Color(128, 0, 128)
    SILVER: Color = Color(192, 192, 192)
    TEAL: Color = Color(0, 128, 128)
    YELLOW: Color = Color(255, 255, 0)
    ORANGE: Color = Color(255, 128, 0)
    CYAN: Color = Color(0, 255, 255)
