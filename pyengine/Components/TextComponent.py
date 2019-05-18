from pyengine.Exceptions import CompatibilityError
import pygame

__all__ = ["TextComponent"]


class TextComponent:
    def __init__(self, texte, color=None, font=None):
        if font is None:
            font = ["arial", 12, False, False]
        if color is None:
            color = (255, 255, 255)

        if len(font) == 1:
            font.append(12)
        if len(font) == 2:
            font.append(False)
        if len(font) == 3:
            font.append(False)

        self.entity = None
        self.texte = texte
        self.font = pygame.font.SysFont(font[0], font[1], font[2], font[3])
        self.color = color

    def set_entity(self, entity):

        from pyengine.Components.SpriteComponent import SpriteComponent

        if entity.has_component(SpriteComponent):
            raise CompatibilityError("TextComponent is not compatible with SpriteComponent")

        self.entity = entity

    def render(self):
        return self.font.render(self.texte, 1, self.color)
