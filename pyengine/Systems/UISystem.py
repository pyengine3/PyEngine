import pygame

__all__ = ["UISystem"]


class UISystem:
    def __init__(self, world):
        self.world = world
        self.widgets = pygame.sprite.Group()

    def get_widget(self, identity):
        for i in self.widgets:
            if i.identity == identity:
                return i

    def add_widget(self, widget):
        widget.set_id(len(self.widgets))
        widget.set_system(self)
        self.widgets.add(widget)
        return widget

    def show(self, screen):
        self.widgets.draw(screen)
