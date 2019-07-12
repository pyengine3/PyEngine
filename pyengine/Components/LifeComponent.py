from pyengine.Utils import clamp

__all__ = ["LifeComponent"]


class LifeComponent:
    def __init__(self, maxlife: int = 100, callback=None):
        self.entity = None
        self.maxlife = maxlife
        self.life = maxlife
        self.callback = callback

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life):
        self.__life = clamp(life, 0, self.maxlife)
        if self.__life == 0 and self.callback is not None:
            self.callback()

    @property
    def maxlife(self):
        return self.__maxlife

    @maxlife.setter
    def maxlife(self, maxi):
        self.__maxlife = maxi
