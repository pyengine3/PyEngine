from pyengine.Exceptions import ComponentIntializedError, CompatibilityError
import pygame

__all__ = ["TextComponent"]


class TextComponent:
    name = "TextComponent"

    def __init__(self):
        self.entity = None
        self.texte = ""
        self.font = None
        self.color = None
        self.initialized = False

    def initialize(self, entity, texte, color=None, font=None):
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

        if self.initialized:
            raise ComponentIntializedError("ControlComponent already initialized")

        from pyengine.Components.SpriteComponent import SpriteComponent

        if entity.has_component(SpriteComponent):
            raise CompatibilityError("TextComponent is not compatible with SpriteComponent")

        self.initialized = True
        self.entity = entity
        self.texte = texte
        self.font = pygame.font.SysFont(font[0], font[1], font[2], font[3])
        self.color = color

    def render(self):
        return self.font.render(self.texte, 1, self.color)
