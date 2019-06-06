from enum import Enum

__all__ = ["Color", "Colors"]


class Color:
    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b

    def get(self):
        return self.r, self.g, self.b

    def set(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        self.r = color.r
        self.g = color.g
        self.b = color.b
        return self

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
        r = self.r + other.r
        b = self.b + other.b
        g = self.g + other.g
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        return Color(r, g, b)

    def __sub__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Color can only be add with Color")
        r = self.r - other.r
        b = self.b - other.b
        g = self.g - other.g
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        return Color(r, g, b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b


class Colors(Enum):
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)


