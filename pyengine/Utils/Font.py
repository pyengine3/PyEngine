import pygame

from pyengine.Utils.Color import Color, Colors

__all__ = ["Font"]


class Font:
    def __init__(self, name: str = "arial", size: int = 15, bold: bool = False, italic: bool = False,
                 underline: bool = False, color: Color = Colors.WHITE.value, background: Color = None,
                 antialias: bool = True):
        pygame.font.init()
        try:
            self.font = pygame.font.Font(name, size)
        except FileNotFoundError:
            self.font = pygame.font.SysFont(name, size)
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.color = color
        self.background = background
        self.antialias = antialias
        self.parent = None

    def get_ascent(self):
        return self.font.get_ascent()

    def get_bold(self):
        return self.font.get_bold()

    def get_descent(self):
        return self.font.get_descent()

    def get_height(self):
        return self.font.get_height()

    def get_italic(self):
        return self.font.get_italic()

    def get_linesize(self):
        return self.font.get_linesize()

    def get_underline(self):
        return self.font.get_underline()

    def get_antialias(self):
        return self.__antialias

    def get_color(self):
        return self.__color

    def get_background(self):
        return self.__background

    def metrics(self, text):
        return self.font.get_metrics(text)

    def render(self, text):
        return self.font.render(text, self.antialias, self.color.get(), self.background)

    def set_bold(self, boldbool):
        self.font.set_bold(boldbool)

    def set_italic(self, italicbool):
        self.font.set_italic(italicbool)

    def set_underline(self, underlinebool):
        self.font.set_underline(underlinebool)

    def set_antialias(self, antialiasebool):
        self.__antialias = antialiasebool

    def set_color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color must be a color")
        self.__color = color

    def set_background(self, background):
        if not isinstance(background, Color) and background is not None:
            raise TypeError("Background must be a color")
        self.__background = background

    def rendered_size(self, text):
        return self.font.size(text)

    bold = property(get_bold, set_bold)
    italic = property(get_italic, set_italic)
    underline = property(get_underline, set_underline)
    antialias = property(get_antialias, set_antialias)
    color = property(get_color, set_color)
    background = property(get_background, set_background)

    def __eq__(self, other):
        print(isinstance(other, Font) and self.name == other.name and self.color == other.color and
                self.background == other.background and self.bold == other.bold and self.italic == other.italic and
                self.underline == other.underline and self.antialias == other.antialias)
        return (isinstance(other, Font) and self.name == other.name and self.color == other.color and
                self.background == other.background and self.bold == other.bold and self.italic == other.italic and
                self.underline == other.underline and self.antialias == other.antialias)
