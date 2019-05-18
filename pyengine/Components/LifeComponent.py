from pyengine.Components import PositionComponent, SpriteComponent

__all__ = ["LifeComponent"]


class LifeComponent:
    def __init__(self, maxlife=100):
        self.entity = None
        self.life = maxlife
        self.maxlife = maxlife

    def set_entity(self, entity):
        self.entity = entity

    def get_life(self):
        return self.life

    def get_maxlife(self):
        return self.maxlife

    def update_life(self, life):
        if life < 0:
            self.life = 0
        else:
            self.life = life
