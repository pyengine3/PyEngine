from pyengine.Components.SpriteComponent import SpriteComponent
from pyengine.Exceptions import NoObjectError

__all__ = ["AnimComponent"]


class AnimComponent:
    def __init__(self, timer: int, *images):
        self.__entity = None
        self.time = timer
        self.images = images
        self.current_sprite = 0
        self.play: bool = True

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):

        if not entity.has_component(SpriteComponent):
            raise NoObjectError("AnimComponent require SpriteComponent")

        self.__entity = entity
        self.images = self.images  # Trigger setter of images

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self, val):
        self.__images = val

        self.current_sprite = 0
        self.timer = self.time
        if self.entity is not None:
            self.entity.get_component(SpriteComponent).sprite = self.__images[0]

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, val):
        if val < 0:
            raise ValueError("Time of AnimComponent can be lower than 0")
        else:
            self.__time = val
            self.timer = val

    def update(self):
        if self.play:
            if self.timer <= 0:
                if self.current_sprite + 1 == len(self.images):
                    self.current_sprite = 0
                else:
                    self.current_sprite += 1
                self.entity.get_component(SpriteComponent).sprite = self.images[self.current_sprite]
                self.timer = self.time

            self.timer -= 1
