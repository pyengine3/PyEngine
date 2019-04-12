from pyengine.Exceptions import ComponentAlreadyIntialized

__all__ = ["PositionComponent"]


class PositionComponent:
    name = "PositionComponent"

    def __init__(self):
        self.entity = None
        self.initialized = False

    def initialize(self, entity, position, offset=None):
        if offset is None:
            offset = [0, 0]

        if self.initialized:
            raise ComponentAlreadyIntialized("SpriteComponent already initialized")
        self.entity = entity
        self.entity.x = position[0] + offset[0]
        self.entity.y = position[1] + offset[1]
        self.entity.offset = offset

    def set_position(self, position):
        self.entity.x = position[0]+self.entity.offset[0]
        self.entity.y = position[1]+self.entity.offset[0]

        from pyengine.Components.SpriteComponent import SpriteComponent  # Avoid import cycle

        if self.entity.has_component(SpriteComponent):
            self.entity.get_component(SpriteComponent).update_position()

        for i in self.entity.attachedentities:
            if i.has_component(PositionComponent):
                i.get_component(PositionComponent).set_position(position)

    def get_position(self):
        return [self.entity.x, self.entity.y]
