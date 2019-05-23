from pyengine.Exceptions import CompatibilityError
from pyengine.Utils import Font

__all__ = ["TextComponent"]


class TextComponent:
    def __init__(self, texte, color=None, font=None):
        if font is None:
            font = Font()
        if color is None:
            color = (255, 255, 255)

        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.entity = None
        self.texte = texte
        self.font = font
        self.color = color

    def set_entity(self, entity):

        from pyengine.Components.SpriteComponent import SpriteComponent

        if entity.has_component(SpriteComponent):
            raise CompatibilityError("TextComponent is not compatible with SpriteComponent")

        self.entity = entity

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_font(self, font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.font = font

    def get_font(self):
        return self.font

    def render(self):
        return self.font.render().render(self.texte, 1, self.color)
