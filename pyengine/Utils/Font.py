import pygame

__all__ = ["Font"]


class Font:
    def __init__(self, name: str = "Arial", size: int = 15, bold: bool = False, italic: bool = False):
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

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.size == other.size and\
               self.bold == other.bold and self.italic == other.italic

    def __repr__(self) -> str:
        return str([self.name, self.size, self.bold, self.italic])

    def rendered_size(self, texte):
        rect = self.render().render(texte, 1, (0, 0, 0)).get_rect()
        return rect.width, rect.height

    def render(self) -> pygame.font:
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
