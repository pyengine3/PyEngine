__all__ = ["Vec2"]


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, val):
        return Vec2(self.x * val, self.y * val)

    def __truediv__(self, val):
        return Vec2(self.x / val, self.y / val)

    def coords(self):
        return self.x, self.y

    def __repr__(self):
        return str(self.coords())
