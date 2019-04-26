from pyengine.Exceptions import ComponentIntializedError

__all__ = ["PositionComponent"]


class PositionComponent:
    name = "PositionComponent"

    def __init__(self):
        self.entity = None
        self.x = 0
        self.y = 0
        self.offset = [0, 0]
        self.initialized = False

    def initialize(self, entity, position, offset=None):
        if offset is None:
            offset = [0, 0]

        if self.initialized:
            raise ComponentIntializedError("PositionComponent already initialized")
        self.entity = entity
        self.x = position[0] + offset[0]
        self.y = position[1] + offset[1]
        self.offset = offset
        self.update_dependances()

    def set_position(self, position):
        self.x = position[0]+self.offset[0]
        self.y = position[1]+self.offset[1]
        self.update_dependances()

    def update_dependances(self):
        from pyengine.Components.SpriteComponent import SpriteComponent  # Avoid import cycle

        if self.entity.has_component(SpriteComponent):
            self.entity.get_component(SpriteComponent).update_position()

        for i in self.entity.attachedentities:
            if i.has_component(PositionComponent):
                i.get_component(PositionComponent).set_position(self.get_position())

    def get_position(self):
        return [self.x, self.y]
