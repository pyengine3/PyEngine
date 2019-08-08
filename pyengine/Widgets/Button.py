from typing import Union, Callable

import pygame

from pyengine.Utils.Vec2 import Vec2
from pyengine.Widgets import Label
from pyengine.Widgets.Widget import Widget

__all__ = ["Button"]


class Button(Widget):
    def __init__(self, position: Vec2, text: str, command: Union[None, Callable[[], None]] = None,
                 size: Vec2 = Vec2(100, 40), sprite: Union[None, str] = None):
        super(Button, self).__init__(position)

        if sprite is None:
            self.image = pygame.Surface(size.coords)
            self.image.fill((50, 50, 50))
        else:
            image = pygame.image.load(sprite)
            self.image = pygame.transform.scale(image, size.coords)

        self.label = Label(position, text)
        self.label.parent = self
        self.rect = self.image.get_rect()
        self.position = position
        self.size = size
        self.sprite = sprite
        self.ishover = False
        self.__enabled = True
        self.command = command
        self.update_render()

    def update_render(self):
        self.update_rect()
        self.label.position = Vec2(self.rect.x+self.rect.width/2-self.label.rect.width/2,
                                   self.rect.y+self.rect.height/2-self.label.rect.height/2)

    def hide(self):
        super(Button, self).hide()
        self.label.hide()

    def show(self):
        super(Button, self).show()
        self.label.show()

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.ishover = False
        t = pygame.surfarray.array3d(self.image)
        if value and not self.__enabled:
            for i in t:
                for j in i:
                    j += 50
        elif not value and self.__enabled:
            for i in t:
                for j in i:
                    j -= 50
        try:
            pygame.surfarray.blit_array(self.image, t)
        except ValueError:
            pass
        self.__enabled = value

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, val):
        self.__sprite = val
        if val is None:
            self.image = pygame.Surface(self.size.coords)
            self.image .fill((50, 50, 50))
        else:
            image = pygame.image.load(val)
            self.image = pygame.transform.scale(image, self.size.coords)
        self.update_render()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, Vec2):
            raise TypeError("Position must be a Vec2")

        self.__size = size
        self.image = pygame.transform.scale(self.image, size.coords)
        self.update_render()

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, command):
        self.__command = command

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        system.add_widget(self.label)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.label.position = Vec2(self.rect.x+self.rect.width/2-self.label.rect.width/2,
                                   self.rect.y+self.rect.height/2-self.label.rect.height/2)

    def mousepress(self, evt):
        from pyengine import MouseButton  # Avoid import error

        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y +\
                self.rect.height and self.command and evt.button == MouseButton.LEFTCLICK.value and self.enabled:
            self.command()
            return True

    def mousemotion(self, evt):
        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y + \
                self.rect.height:
            if not self.ishover and self.enabled:
                t = pygame.surfarray.array3d(self.image)
                for i in t:
                    for j in i:
                        j += 10
                try:
                    pygame.surfarray.blit_array(self.image, t)
                except ValueError:
                    pass
                self.ishover = True
        elif self.ishover and self.enabled:
            t = pygame.surfarray.array3d(self.image)
            for i in t:
                for j in i:
                    j -= 10
            try:
                pygame.surfarray.blit_array(self.image, t)
            except ValueError:
                pass
            self.ishover = False


