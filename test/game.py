from pyengine import Window
from pyengine.Systems import UISystem
from pyengine.Utils import Colors, Vec2
from pyengine.Widgets import Button, Entry, Label, Console, Selector


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value)

        self.uisys = self.world.get_system(UISystem)

        self.button = Button(Vec2(500, 100), "Add", self.btn)
        self.e = Entry(Vec2(400, 400))
        self.la = Label(Vec2(400, 450), "Contenu de \nl'entry", Colors.BLACK.value)
        self.console = Console(self, width=self.width)
        self.select = Selector(Vec2(0, 100), ["Ceci", "Est", "Un", "Test"])

        self.uisys.add_widget(self.button)
        self.uisys.add_widget(self.e)
        self.uisys.add_widget(self.la)
        self.uisys.add_widget(self.console)
        self.uisys.add_widget(self.select)

        self.run()

    def btn(self):
        self.la.text = self.e.text
        print(self.select.get())
        self.select.strings = ["CECI EST TROP LONG", "OU PAS !"]


Game()
