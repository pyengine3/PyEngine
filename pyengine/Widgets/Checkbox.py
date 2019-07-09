from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label
from pyengine.Utils import Vec2

import pygame

__all__ = ["Checkbox"]


class Checkbox(Widget):
    def __init__(self, position: Vec2, text: str, checked: bool = False, scale: float = 1):
        super(Checkbox, self).__init__(position)

        self.__checked = checked
        self.__scale = scale

        self.label = Label(position, text)
        self.label.parent = self

        self.create_image()

    def update_render(self):
        self.update_rect()
        self.label.position = Vec2(self.rect.x + 20 * self.scale + 5,
                                   self.rect.y + self.rect.height / 2 - self.label.rect.height / 2)

    def create_image(self):
        if self.checked:
            self.image = pygame.Surface([20 * self.scale, 20 * self.scale])
            self.image.fill((50, 50, 50))
            iiwhite = pygame.Surface([16 * self.scale, 16 * self.scale])
            iiwhite.fill((255, 255, 255))
            self.image.blit(iiwhite, (self.image.get_width() / 2 - iiwhite.get_width() / 2,
                                      self.image.get_height() / 2 - iiwhite.get_height() / 2))
            iiblack = pygame.Surface([14 * self.scale, 14 * self.scale])
            iiblack.fill((0, 0, 0))
            self.image.blit(iiblack, (self.image.get_width() / 2 - iiblack.get_width() / 2,
                                      self.image.get_height() / 2 - iiblack.get_height() / 2))
        else:
            self.image = pygame.Surface([20 * self.scale, 20 * self.scale])
            self.image.fill((50, 50, 50))
            iiwhite = pygame.Surface([16 * self.scale, 16 * self.scale])
            iiwhite.fill((255, 255, 255))
            self.image.blit(iiwhite, (self.image.get_width() / 2 - iiwhite.get_width() / 2,
                                      self.image.get_height() / 2 - iiwhite.get_height() / 2))
        self.update_render()

    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, val: bool):
        self.__checked = val
        self.create_image()

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val: float):
        self.__scale = val
        self.create_image()

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        system.add_widget(self.label)

    def mousepress(self, evt):
        from pyengine import MouseButton  # Avoid import error

        if ((self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y +
                self.rect.height) or self.label.mousepress(evt)) and evt.button == MouseButton.LEFTCLICK.value:
            self.checked = not self.checked
            self.create_image()
            return True

