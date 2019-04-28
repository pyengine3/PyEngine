import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["Label"]


class Label(Widget):
    def __init__(self, position, text, color=None, font=None):
        super(Label, self).__init__(position)
        if font is None:
            font = ["arial", 15, False, False]
        if color is None:
            color = (255, 255, 255)

        if len(font) == 1:
            font.append(15)
        if len(font) == 2:
            font.append(False)
        if len(font) == 3:
            font.append(False)

        self.color = color
        self.font = pygame.font.SysFont(font[0], font[1], font[2], font[3])
        self.text = text
        self.image = self.font.render(text, 1, color)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
