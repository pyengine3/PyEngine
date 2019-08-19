import pygame

from pyengine import World
from pyengine.Utils.Logger import loggers
from pyengine.Utils.Color import Colors
from pyengine.Utils.Font import Font
from pyengine.Widgets.Entry import Entry
from pyengine.Widgets.Button import Button
from pyengine.Widgets.AnimatedImage import AnimatedImage
from pyengine.Widgets.Widget import Widget

__all__ = ["UISystem"]


class UISystem:
    def __init__(self, world: World):
        self.world = world
        self.widgets = pygame.sprite.Group()
        self.focus = None
        self.debugfont = Font("arial", 15, color=Colors.BLUE.value)

    def get_widget(self, identity: int) -> Widget:
        liste = [i for i in self.widgets if i.identity == identity]
        if len(liste):
            return liste[0]
        loggers.get_logger("PyEngine").warning("Try to get widget with id "+str(identity)+" but it doesn't exist")

    def add_widget(self, widget: Widget) -> Widget:
        if not isinstance(widget, Widget):
            raise TypeError("Argument is not type of "+str(Widget)+" but "+str(type(widget))+".")
        if len(self.widgets):
            widget.identity = self.widgets.sprites()[-1].identity + 1
        else:
            widget.identity = 0
        self.widgets.add(widget)
        widget.system = self
        return widget

    def has_widget(self, widget: Widget) -> bool:
        return widget in self.widgets

    def remove_widget(self, widget: Widget) -> None:
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise ValueError("Widget has not in UISystem")

    def mousepress(self, evt):
        focustemp = None
        for i in self.widgets.sprites():
            if i.mousepress(evt):
                while i.parent is not None:
                    i = i.parent
                focustemp = i
                i.focusin()
            else:
                if self.focus == i:
                    self.focus.focusout()
        self.focus = focustemp

    def mousemotion(self, evt):
        [i.mousemotion(evt) for i in self.widgets if isinstance(i, Button)]

    def keyup(self, evt):
        [i.keyup(evt) for i in self.widgets if self.focus == i and isinstance(i, Entry)]

    def keypress(self, evt):
        [i.keypress(evt) for i in self.widgets if self.focus == i and isinstance(i, Entry)]

    def update(self):
        [i.update() for i in self.widgets if self.focus == i and isinstance(i, Entry)]
        [i.update() for i in self.widgets if isinstance(i, AnimatedImage)]

    def show(self, screen):
        [screen.blit(i.image, i.rect) for i in self.widgets if i.isshow and i.image is not None]

    def show_debug(self, screen):
        for i in self.widgets:
            if i.isshow and i.image is not None:
                render = self.debugfont.render("ID : "+str(i.identity))
                screen.blit(render, (i.rect.x + i.rect.width / 2 - render.get_width()/2, i.rect.y - 20))
