from pyengine import Window
from pyengine.Systems import EntitySystem
from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, MoveComponent, PhysicsComponent
from pyengine.Utils import Vec2


class BasicEntity(Entity):
    def __init__(self, pos):
        super(BasicEntity, self).__init__()

        self.add_component(PositionComponent(pos))
        self.add_component(SpriteComponent("images/sprite0.png", 2))


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(640, 640, debug=True)

        self.esys = self.world.get_system(EntitySystem)

        j = BasicEntity(Vec2(100, 200))
        j.add_component(MoveComponent(Vec2(50, 50)))
        j.add_component(PhysicsComponent(False, callback=self.collision))

        obj = BasicEntity(Vec2(100, 100))
        obj.add_component(PhysicsComponent())

        self.esys.add_entity(j)
        self.esys.add_entity(obj)
        self.run()

    def collision(self, entity, others, space, data):
        print(entity.identity)
        print([i.identity for i in others])
        print(space)
        print(data)


Game()
