from pyengine.Widgets.Widget import Widget
from pyengine.Utils import Font, Color, Colors
import pygame

__all__ = ["Label"]


class Label(Widget):
    def __init__(self, position, text, color=Colors.WHITE.value, font=Font(), background=None):
        super(Label, self).__init__(position)

        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")
        if not isinstance(background, Color) and background is not None:
            raise TypeError("Background must be a Color")

        self.__color = color
        self.__font = font
        self.__background = background
        self.text = text
        self.update_render()

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, color):
        if not isinstance(color, Color) and color is not None:
            raise TypeError("Background must be a Color")

        self.__background = color
        self.update_render()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Color have not a Color type")

        self.__color = color
        self.update_render()

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, font):
        if not isinstance(font, Font):
            raise TypeError("Font have not a Font type")

        self.__font = font
        self.update_render()

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
        self.update_render()

    def update_render(self):
        if self.background is None:
            self.image = self.font.render().render(self.text, 1, self.color.get())
        else:
            renderer = self.font.render().render(self.text, 1, self.color.get())
            self.image = pygame.Surface([renderer.get_rect().width, renderer.get_rect().height])
            self.image.fill(self.background.get())
            self.image.blit(renderer, [0, 0])
        self.update_rect()
        if self.parent:
            self.parent.update_render()

