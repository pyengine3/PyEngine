__all__ = ["LifeComponent"]


class LifeComponent:
    def __init__(self, maxlife: int = 100):
        self.entity = None
        self.maxlife = maxlife
        self.life = maxlife

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
        if life < 0:
            self.__life = 0
        elif life > self.maxlife:
            self.__life = self.maxlife
        else:
            self.__life = life

    @property
    def maxlife(self):
        return self.__maxlife

    @maxlife.setter
    def maxlife(self, maxi):
        self.__maxlife = maxi
