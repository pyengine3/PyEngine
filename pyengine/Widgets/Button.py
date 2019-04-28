import pygame
from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label

__all__ = ["Button"]


class Button(Widget):
    def __init__(self, position, text, command=None, size=None, image=None):
        super(Button, self).__init__(position)

        if size is None:
            size = [100, 40]
        if image is None:
            image = pygame.Surface(size)
            image.fill((50, 50, 50))
        else:
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, size)

        self.size = size
        self.image = image
        self.command = command
        self.rect = image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.label = Label(position, text)
        self.label.set_position([position[0]+self.rect.width/2-self.label.rect.width/2,
                                 position[1]+self.rect.height/2-self.label.rect.height/2])

    def set_system(self, system):
        super(Button, self).set_system(system)
        system.add_widget(self.label)

    def set_position(self, position):
        super(Button, self).set_position(position)
        self.label.set_position([self.rect.x+self.rect.width/2-self.label.rect.width/2,
                                 self.rect.y+self.rect.height/2-self.label.rect.height/2])

    def mousepress(self, button, pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.rect.width and self.rect.y <= pos[1] <= self.rect.y +\
                self.rect.height and self.command:
            self.command(self, button)


