import pygame

__all__ = ["Font"]


class Font:
    def __init__(self, name="arial", size=15, bold=False, italic=False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.parent = None

    def update(self):
        if self.parent:
            self.parent.update()

    def set_name(self, name):
        self.name = name
        self.update()

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size
        self.update()

    def get_size(self):
        return self.size

    def set_bold(self, bold):
        self.bold = bold
        self.update()

    def is_bold(self):
        return self.bold

    def set_italic(self, italic):
        self.italic = italic
        self.update()

    def is_italic(self):
        return self.italic

    def render(self):
        return pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
