from pyengine import Window, ControlType, WindowCallbacks
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Utils import Colors, Vec2
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, TextComponent, \
    ControlComponent, LifeComponent
from pyengine.Entities import Tilemap, Entity
from pyengine.Widgets import Checkbox, ProgressBar, Button, Entry, Label, Console, MultilineLabel


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value)

        self.set_callback(WindowCallbacks.OUTOFWINDOW, self.parti)

        self.uisys = self.world.get_system(UISystem)

        self.check = Checkbox(Vec2(500, 300), "TEST")
        self.check.label.color = Colors.BLACK.value
        self.progress = ProgressBar(Vec2(400, 200), Vec2(300, 20))
        self.button = Button(Vec2(500, 100), "Add", self.btn)
        self.e = Entry(Vec2(400, 400))
        self.la = Label(Vec2(400, 450), "Contenu de \nl'entry", Colors.BLACK.value)
        self.console = Console(self, width=self.width)
        self.ml = MultilineLabel(Vec2(10, 450), "Chocolat\nVanille\nCARAMEL !", Colors.BLACK.value)

        self.uisys.add_widget(self.check)
        self.uisys.add_widget(self.progress)
        self.uisys.add_widget(self.button)
        self.uisys.add_widget(self.e)
        self.uisys.add_widget(self.la)
        self.uisys.add_widget(self.console)
        self.uisys.add_widget(self.ml)

        self.esys = self.world.get_system(EntitySystem)

        self.tilemap = Tilemap(Vec2(20, 90), "tilemap/TESTMAP.json")

        self.player = Entity()
        self.player.add_component(PositionComponent(Vec2(10, 10)))
        self.player.add_component(SpriteComponent("images/idle.png")).scale = 0.3
        self.player.add_component(ControlComponent(ControlType.FOURDIRECTION))
        self.player.add_component(PhysicsComponent(False))
        self.player.add_component(LifeComponent(100, self.die))

        self.etext = Entity()
        self.etext.add_component(PositionComponent(Vec2(10, 50)))
        self.etext.add_component(TextComponent("TEST", Colors.BLACK.value))
        self.etext2 = Entity()
        self.etext2.add_component(PositionComponent(Vec2(10, 80)))
        self.etext2.add_component(TextComponent("TEST", Colors.BLACK.value))

        self.esys.add_entity(self.tilemap)
        self.esys.add_entity(self.player)
        self.esys.add_entity(self.etext)
        self.esys.add_entity(self.etext2)

        self.run()

    def btn(self):
        self.progress.value += 5
        self.la.text = self.e.text
        self.player.get_component(LifeComponent).life = -10
        self.ml.text = "OUI !"

    def die(self):
        print("MON ENTITE EST MORTE !")

    def parti(self, obj, pos):
        print("MAIS T'ES PARTI !")


Game()
