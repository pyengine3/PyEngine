from pyengine.Utils import Vec2

__all__ = ["PositionComponent"]


class PositionComponent:
    def __init__(self, position, offset=Vec2()):
        self.__entity = None

        if not isinstance(position, Vec2):
            raise TypeError("Position must be a Vec2")
        if not isinstance(offset, Vec2):
            raise TypeError("Offset must be a Vec2")

        self.offset = offset
        self.__position = position + offset

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity
        self.update_dependances()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, Vec2):
            raise TypeError("Position must be a Vec2")

        self.__position = position + self.offset
        self.update_dependances()

    def update_dependances(self):
        from pyengine.Components.SpriteComponent import SpriteComponent  # Avoid import cycle

        if self.entity.has_component(SpriteComponent):
            self.entity.get_component(SpriteComponent).update_position()

        for i in self.entity.attachedentities:
            if i.has_component(PositionComponent):
                i.get_component(PositionComponent).position = self.position
