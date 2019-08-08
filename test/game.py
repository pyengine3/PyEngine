from pyengine import Window, ControlType
from pyengine.Systems import EntitySystem
from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, ControlComponent, PhysicsComponent
from pyengine.Utils import Vec2


class BasicEntity(Entity):
    def __init__(self, pos):
        super(BasicEntity, self).__init__()

        self.add_component(PositionComponent(pos))
        self.add_component(SpriteComponent("images/sprite0.png", 2))


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(640, 640, debug=True)

        self.world.collision_callback = self.callback

        self.esys = self.world.get_system(EntitySystem)

        j = BasicEntity(Vec2(100, 200))
        j.add_component(ControlComponent(ControlType.FOURDIRECTION))
        j.add_component(PhysicsComponent(False))

        obj = BasicEntity(Vec2(100, 100))
        obj.add_component(PhysicsComponent())
        self.esys.add_entity(j)
        self.esys.add_entity(obj)
        self.run()

    def callback(self, arb, space, data):
        print("Collision")
        print(arb)
        print(space)
        print(data)
        return True


Game()
