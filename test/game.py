from pyengine import Window
from pyengine.Systems import UISystem
from pyengine.Utils import Colors, Vec2
from pyengine.Widgets import Label, Button, Entry


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value)

        self.uisys = self.world.get_system(UISystem)

        self.la = Label(Vec2(100, 100), "Texte", Colors.BLACK.value)
        self.b = Button(Vec2(100, 200), "Afficher", self.show_entry)
        self.e = Entry(Vec2(100, 300))

        self.uisys.add_widget(self.la)
        self.uisys.add_widget(self.b)
        self.uisys.add_widget(self.e)

        self.run()

    def show_entry(self, btn, click):
        self.la.text = self.e.text
        self.e.width = 500
        if self.e.hasimage:
            self.e.sprite = None
        else:
            self.e.sprite = "../tests/files/sprite0.png"


Game()
