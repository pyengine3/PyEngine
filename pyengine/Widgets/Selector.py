from pyengine.Widgets.Widget import Widget
from pyengine.Widgets import Label, Button
from pyengine.Utils import Vec2, Colors, Font

__all__ = ["Selector"]


class Selector(Widget):
    def __init__(self, position: Vec2, strings: (list, tuple)):
        super(Selector, self).__init__(position)
        if not isinstance(strings, (list, tuple)) or len(strings) == 0:
            raise ValueError("Strings must be a list with minimum one str.")

        self.__strings = strings
        self.current_index = 0
        self.bprecedent = Button(position, "<", self.precedent, size=Vec2(25, 25))
        self.label = Label(Vec2(position.x+30, position.y), self.strings[0],
                           Colors.BLACK.value, Font(size=18), Colors.WHITE.value)
        self.bnext = Button(Vec2(position.x+35+self.maxsize_string(), position.y), ">", self.next, size=Vec2(25, 25))
        self.bprecedent.parent = self
        self.label.parent = self
        self.bnext.parent = self
        self.update_render()

    @property
    def strings(self):
        return self.__strings

    @strings.setter
    def strings(self, val: (list, tuple)):
        if not isinstance(val, (list, tuple)) or len(val) == 0:
            raise ValueError("Strings must be a list with minimum one str.")
        self.__strings = val
        self.current_index = 0
        self.label.text = self.strings[0]
        self.bnext.position = Vec2(self.position.x+35+self.maxsize_string(), self.position.y)

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        self.system.add_widget(self.bprecedent)
        self.system.add_widget(self.label)
        self.system.add_widget(self.bnext)

    def maxsize_string(self):
        maxi = 0
        for i in self.strings:
            size = self.label.font.rendered_size(i)[0]
            if maxi < size:
                maxi = size
        return maxi

    def precedent(self):
        if self.current_index == 0:
            self.current_index = len(self.strings)-1
        else:
            self.current_index -= 1
        self.label.text = self.strings[self.current_index]

    def next(self):
        if self.current_index == len(self.strings) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        self.label.text = self.strings[self.current_index]

    def get(self):
        return self.label.text

    def update_render(self):
        self.label.position = Vec2(self.position.x + 30 + self.maxsize_string() / 2 -
                                   self.label.font.rendered_size(self.label.text)[0] / 2, self.position.y)


        