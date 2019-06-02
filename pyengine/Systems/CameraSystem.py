from pyengine.Systems import EntitySystem
from pyengine.Components import PositionComponent

__all__ = ["CameraSystem"]


class CameraSystem:
    def __init__(self, world):
        self.world = world
        self.__position = [0, 0]
        self.offset = [0, 0]
        self.entity_follow = None

    @property
    def entity_follow(self):
        return self.__ef

    @entity_follow.setter
    def entity_follow(self, entity):
        self.__ef = entity
        if entity is not None:
            if entity.rect:
                self.offset = [
                    self.world.window.size[0] / 2 - entity.rect.x / 2,
                    self.world.window.size[1] / 2 - entity.rect.y / 2
                ]
            else:
                self.offset = [
                    self.world.window.size[0] / 2,
                    self.world.window.size[1] / 2
                ]

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
        for i in self.world.get_system(EntitySystem).entities:
            pos = i.get_component(PositionComponent)
            pos.position = [pos.position[0] - self.position[0] + self.offset[0],
                            pos.position[1] - self.position[1] + self.offset[1]]
        for i in self.world.get_system(EntitySystem).texts:
            pos = i.get_component(PositionComponent)
            pos.position = [pos.position[0] - self.position[0] + self.offset[0],
                            pos.position[1] - self.position[1] + self.offset[1]]

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
