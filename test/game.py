from pyengine import Window, Entity, ControlType
from pyengine.Systems import UISystem, EntitySystem, CameraSystem
from pyengine.Utils import Colors, Vec2, Font
from pyengine.Widgets import Label, Button, Entry
from pyengine.Components import PositionComponent, SpriteComponent, AnimComponent, ControlComponent


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value, debug=True)

        self.uisys = self.world.get_system(UISystem)

        self.la = Label(Vec2(100, 100), "Texte", Colors.BLACK.value)
        self.b = Button(Vec2(100, 200), "Afficher", self.show_entry)
        self.e = Entry(Vec2(100, 300), color=Colors.GREEN.value, font=Font(size=25))

        self.uisys.add_widget(self.la)
        self.uisys.add_widget(self.b)
        self.uisys.add_widget(self.e)

        self.esys = self.world.get_system(EntitySystem)

        self.en = Entity()
        self.en.add_component(PositionComponent(Vec2(400, 100)))
        self.en.add_component(SpriteComponent("../tests/files/sprite0.png"))
        self.en.add_component(AnimComponent(50, "../tests/files/sprite0.png", "../tests/files/sprite1.png"))

        self.en2 = Entity()
        self.en2.add_component(PositionComponent(Vec2(300, 100)))
        self.en2.add_component(SpriteComponent("../tests/files/sprite0.png"))
        self.en2.add_component(ControlComponent(ControlType.FOURDIRECTION))

        self.esys.add_entity(self.en)
        self.esys.add_entity(self.en2)

        self.run()

    def show_entry(self, btn, click):
        self.la.text = self.e.text
        self.world.get_system(CameraSystem).entity_follow = self.en2


Game()
