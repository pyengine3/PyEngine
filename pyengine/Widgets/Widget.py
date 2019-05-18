import pygame

__all__ = ["Widget"]


class Widget(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Widget, self).__init__()
        self.id = -1
        self.position = position
        self.system = None
        self.parent = None
        self.isshow = True

        self.rect = None  # Respect PEP8
        self.image = None  # Respect PEP8

    def set_id(self, identity):
        self.id = identity

    def focusin(self):
        pass

    def focusout(self):
        pass

    def set_system(self, system):
        self.system = system

    def get_id(self):
        return self.id

    def get_system(self):
        return self.system

    def is_show(self):
        return self.isshow

    def show(self):
        self.isshow = True

    def hide(self):
        self.isshow = False

    def set_position(self, position):
        self.position = position
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def get_position(self):
        return self.position

    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def mousepress(self, evt):
        if self.rect.x <= evt.pos[0] <= self.rect.x + self.rect.width and self.rect.y <= evt.pos[1] <= self.rect.y +\
                self.rect.height:
            return True
