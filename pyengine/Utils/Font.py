import pygame

__all__ = ["Font"]


class Font:
    def __init__(self, name="arial", size=15, bold=False, italic=False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.parent = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return self

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold):
        self.__bold = bold

    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic):
        self.__italic = italic

    def __eq__(self, other):
        return self.name == other.name and self.size == other.size and\
               self.bold == other.bold and self.italic == other.italic

    def __ne__(self, other):
        return not self == other

    def render(self):
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
