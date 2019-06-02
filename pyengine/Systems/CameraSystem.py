from pyengine.Systems import EntitySystem
from pyengine.Components import PositionComponent

__all__ = ["CameraSystem"]


class CameraSystem:
    def __init__(self, world):
        self.world = world
        self.position = [0, 0]

    def set_position(self, position):
        self.position = position
        for i in self.world.get_system(EntitySystem).entities:
            pos = i.get_component(PositionComponent)
            pos.set_position([pos.get_position()[0] - self.position[0], pos.get_position()[1] - self.position[1]])
        for i in self.world.get_system(EntitySystem).texts:
            pos = i.get_component(PositionComponent)
            pos.set_position([pos.get_position()[0] - self.position[0], pos.get_position()[1] - self.position[1]])

    def get_position(self):
        return self.position
