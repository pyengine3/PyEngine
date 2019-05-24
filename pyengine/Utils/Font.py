import pygame

__all__ = ["Font"]


class Font:
    def __init__(self, name="arial", size=15, bold=False, italic=False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.parent = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_bold(self, bold):
        self.bold = bold

    def is_bold(self):
        return self.bold

    def set_italic(self, italic):
        self.italic = italic

    def is_italic(self):
        return self.italic

    def render(self):
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
