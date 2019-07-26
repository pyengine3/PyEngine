from pyengine.Widgets import Image
from pyengine.Utils import Vec2, loggers
from typing import List, Tuple

__all__ = ["AnimatedImage"]


class AnimatedImage(Image):
    def __init__(self, position: Vec2, sprites: List, timer: int = 20, size: Vec2 = None):
        if not isinstance(sprites, (list, tuple)) and len(sprites) == 0:
            raise ValueError("Sprites must be a List with minimum one sprite")
        elif len(sprites) == 1:
            loggers.get_logger("PyEngine").info("AnimatedImage is useless with only one sprite. Use Image.")
        super(AnimatedImage, self).__init__(position, sprites[0], size)
        self.__sprites = sprites
        self.timer = timer - 1
        self.current_sprite = 0
        self.play = True

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.__timer = timer
        self.timerinterne = timer

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, sprites: List):
        if not (isinstance(sprites, list) or isinstance(sprites, tuple)) and len(sprites) == 0:
            raise ValueError("Sprites must be a List with minimum one sprite")
        elif len(sprites) == 1:
            loggers.get_logger("PyEngine").info("AnimatedImage is useless with only one sprite. Use Image.")
        self.__sprites = sprites
        self.sprite = sprites[0]
        self.current_sprite = 0

    def update(self):
        if self.play:
            if self.timerinterne <= 0:
                if self.current_sprite + 1 < len(self.sprites):
                    self.current_sprite += 1
                else:
                    self.current_sprite = 0
                self.sprite = self.sprites[self.current_sprite]
                self.timerinterne = self.timer
            self.timerinterne -= 1
