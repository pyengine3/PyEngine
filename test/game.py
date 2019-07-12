from pyengine import Window, Entity, ControlType
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Utils import Colors, Vec2
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, ControlComponent
from pyengine.Prefabs import Tilemap
from pyengine.Widgets import Checkbox, ProgressBar, Button, Entry, Label


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value)

        self.uisys = self.world.get_system(UISystem)

        self.check = Checkbox(Vec2(500, 300), "TEST")
        self.check.label.color = Colors.BLACK.value
        self.progress = ProgressBar(Vec2(400, 200), Vec2(300, 20), ("tilemap/sprite0.png", "tilemap/sprite1.png"))
        self.button = Button(Vec2(500, 100), "Add", self.btn)
        self.e = Entry(Vec2(400, 400))
        self.la = Label(Vec2(400, 450), "Contenu de l'entry", Colors.BLACK.value)

        self.uisys.add_widget(self.check)
        self.uisys.add_widget(self.progress)
        self.uisys.add_widget(self.button)
        self.uisys.add_widget(self.e)
        self.uisys.add_widget(self.la)

        self.esys = self.world.get_system(EntitySystem)

        self.tilemap = Tilemap(Vec2(), "tilemap/TESTMAP.json", 0.7)

        self.player = Entity()
        self.player.add_component(PositionComponent(Vec2(10, 10)))
        self.player.add_component(SpriteComponent("images/idle.png")).scale = 0.2
        self.player.add_component(PhysicsComponent())
        self.player.add_component(ControlComponent(ControlType.CLASSICJUMP))

        self.esys.add_entity(self.tilemap)
        self.esys.add_entity(self.player)

        self.run()

    def btn(self):
        self.progress.value += 5
        self.tilemap.scale = 1.2
        self.la.text = self.e.text


Game()
