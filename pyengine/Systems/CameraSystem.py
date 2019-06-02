from pyengine.Systems import EntitySystem
from pyengine.Components import PositionComponent

__all__ = ["CameraSystem"]


class CameraSystem:
    def __init__(self, world):
        self.world = world
        self.__position = [0, 0]

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
        for i in self.world.get_system(EntitySystem).entities:
            pos = i.get_component(PositionComponent)
            pos.position = [pos.position[0] - self.position[0], pos.position[1] - self.position[1]]
        for i in self.world.get_system(EntitySystem).texts:
            pos = i.get_component(PositionComponent)
            pos.position = [pos.position[0] - self.position[0], pos.position[1] - self.position[1]]
