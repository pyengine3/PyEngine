from pyengine import Window, ControlType
from pyengine.Systems import EntitySystem
from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, ControlComponent
from pyengine.Utils import Vec2


class BasicEntity(Entity):
    def __init__(self, pos):
        super(BasicEntity, self).__init__()

        self.add_component(PositionComponent(pos))
        self.add_component(SpriteComponent("images/sprite0.png", 20))
        self.add_component(ControlComponent(ControlType.FOURDIRECTION))


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(640, 640, debug=True)

        self.esys = self.world.get_system(EntitySystem)

        self.esys.add_entity(BasicEntity(Vec2(0, 0)))

        self.run()


Game()
