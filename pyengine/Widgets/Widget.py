import pygame

__all__ = ["Widget"]


class Widget(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Widget, self).__init__()
        self.id = -1
        self.position = position
        self.system = None

        self.rect = None  # Respect PEP8
        self.image = None  # Respect PEP8

    def set_id(self, identity):
        self.id = identity

    def set_system(self, system):
        self.system = system

    def get_id(self):
        return self.id

    def get_system(self):
        return self.system

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
