from pyengine.Components.SpriteComponent import SpriteComponent
from pyengine.Exceptions import NoObjectError

__all__ = ["AnimComponent"]


class AnimComponent:
    def __init__(self, timer: int, *images):
        self.__entity = None
        self.images = images
        self.basetimer = timer
        self.timer = timer
        self.current_sprite = 0

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):

        if not entity.has_component(SpriteComponent):
            raise NoObjectError("AnimComponent require SpriteComponent")

        self.__entity = entity
        self.entity.get_component(SpriteComponent).sprite = self.images[0]

    def update(self):
        if self.timer <= 0:
            if self.current_sprite + 1 == len(self.images):
                self.current_sprite = 0
            else:
                self.current_sprite += 1
            self.entity.get_component(SpriteComponent).sprite = self.images[self.current_sprite]
            self.timer = self.basetimer

        self.timer -= 1
