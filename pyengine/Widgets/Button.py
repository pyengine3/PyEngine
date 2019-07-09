import pygame
from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label
from pyengine.Utils import Vec2
from typing import Union, Callable, Tuple

__all__ = ["Button"]


class Button(Widget):
    def __init__(self, position: Vec2, text: str, command: Union[None, Callable[[int], None]] = None,
                 size: Vec2 = Vec2(100, 40), sprite: Union[None, str] = None):
        super(Button, self).__init__(position)

        if sprite is None:
            self.image = pygame.Surface(size.coords)
            self.image.fill((50, 50, 50))
        else:
            image = pygame.image.load(sprite)
            self.image = pygame.transform.scale(image, size.coords)

        self.rect = self.image.get_rect()
        self.label = Label(position, text)
        self.label.parent = self
        self.position = position
        self.size = size
        self.sprite = sprite
        self.ishover = False
        self.command = command
        self.update_render()

    def update_render(self):
        self.update_rect()
        self.label.position = Vec2(self.rect.x+self.rect.width/2-self.label.rect.width/2,
                                   self.rect.y+self.rect.height/2-self.label.rect.height/2)

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
        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y +\
                self.rect.height and self.command:
            self.command(self, evt.button)
            return True

    def mousemotion(self, evt):
        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y + \
                self.rect.height:
            if not self.ishover:
                t = pygame.surfarray.array3d(self.image)
                for i in t:
                    for j in i:
                        j += 10
                pygame.surfarray.blit_array(self.image, t)
                self.ishover = True
        elif self.ishover:
            t = pygame.surfarray.array3d(self.image)
            for i in t:
                for j in i:
                    j -= 10
            pygame.surfarray.blit_array(self.image, t)
            self.ishover = False


