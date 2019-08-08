from typing import Tuple

import pygame

__all__ = ["Vec2"]


class Vec2(pygame.Vector2):
    def __init__(self, x: int = 0, y: int = 0):
        super(Vec2, self).__init__(x, y)

    @property
    def coords(self) -> Tuple[int, int]:
        return round(self.x), round(self.y)

    @coords.setter
    def coords(self, dic: Tuple[int, int]) -> None:
        self.x = dic[0]
        self.y = dic[1]

    @property
    def fcoords(self) -> Tuple[float, float]:
        return self.x, self.y

    @fcoords.setter
    def fcoords(self, dic: Tuple[float, float]) -> None:
        self.x = dic[0]
        self.y = dic[1]

