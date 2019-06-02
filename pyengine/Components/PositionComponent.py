__all__ = ["PositionComponent"]


class PositionComponent:
    def __init__(self, position, offset=None):
        self.__entity = None
        if offset is None:
            offset = [0, 0]
        self.offset = offset
        self.x = position[0]+self.offset[0]
        self.y = position[1]+self.offset[1]

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity
        self.update_dependances()

    @property
    def position(self):
        return [self.x, self.y]

    @position.setter
    def position(self, position):
        self.x = position[0]+self.offset[0]
        self.y = position[1]+self.offset[1]
        self.update_dependances()

    def update_dependances(self):
        from pyengine.Components.SpriteComponent import SpriteComponent  # Avoid import cycle

        if self.entity.has_component(SpriteComponent):
            self.entity.get_component(SpriteComponent).update_position()

        for i in self.entity.attachedentities:
            if i.has_component(PositionComponent):
                i.get_component(PositionComponent).position = self.position
