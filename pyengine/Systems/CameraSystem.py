from pyengine.Systems import EntitySystem
from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2

__all__ = ["CameraSystem"]


class CameraSystem:
    def __init__(self, world):
        self.world = world
        self.__position = Vec2()
        self.offset = Vec2()
        self.entity_follow = None

    @property
    def entity_follow(self):
        return self.__ef

    @entity_follow.setter
    def entity_follow(self, entity):
        self.__ef = entity
        if entity is not None:
            if entity.rect:
                self.offset = Vec2(
                    self.world.window.size[0] / 2 - entity.rect.width / 2,
                    self.world.window.size[1] / 2 - entity.rect.height / 2
                )
            else:
                self.offset = Vec2(
                    self.world.window.size[0] / 2,
                    self.world.window.size[1] / 2
                )

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, Vec2):
            raise TypeError("Position must be a Vec2")

        self.__position = position
        for i in self.world.get_system(EntitySystem).entities:
            pos = i.get_component(PositionComponent)
        for i in self.world.get_system(EntitySystem).texts:
            pos = i.get_component(PositionComponent)
            pos.position = [pos.position.x - self.position.x + self.offset.x,
                            pos.position.y - self.position.y + self.offset.y]

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    def update(self):
        if self.entity_follow is not None:
            if self.entity_follow.has_component(PositionComponent):
                self.position = self.entity_follow.get_component(PositionComponent).position
