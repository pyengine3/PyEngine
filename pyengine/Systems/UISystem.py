import pygame
from pyengine.Widgets.Widget import Widget

__all__ = ["UISystem"]


class UISystem:
    def __init__(self, state):
        self.state = state
        self.widgets = pygame.sprite.Group()
        self.focus = None

    def get_widget(self, identity):
        for i in self.widgets:
            if i.identity == identity:
                return i

    def add_widget(self, widget):
        if not isinstance(widget, Widget):
            raise TypeError("Argument is not type of "+str(Widget)+" but "+str(type(widget))+".")
        widget.set_id(len(self.widgets))
        self.widgets.add(widget)
        widget.set_system(self)
        return widget

    def mousepress(self, evt):
        focustemp = None
        for i in self.widgets.sprites():
            try:
                if i.mousepress(evt):
                    while i.parent is not None:
                        i = i.parent
                    focustemp = i
                    i.focusin()
                else:
                    if self.focus == i:
                        self.focus.focusout()
            except AttributeError:
                pass
        self.focus = focustemp

    def keypress(self, evt):
        for i in self.widgets.sprites():
            try:
                if self.focus == i:
                    i.keypress(evt)
            except AttributeError:
                pass

    def keyup(self, evt):
        for i in self.widgets.sprites():
            try:
                if self.focus == i:
                    i.keyup(evt)
            except AttributeError:
                pass

    def update(self):
        for i in self.widgets.sprites():
            try:
                if self.focus == i:
                    i.update()
            except AttributeError:
                pass

    def show(self, screen):
        self.widgets.draw(screen)
