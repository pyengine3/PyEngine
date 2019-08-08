from pyengine import Window, ControlType, MouseButton
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
        super(Game, self).__init__(1200, 750, debug=True)

        self.world.mousepress = self.mousepress
        self.esys = self.world.get_system(EntitySystem)

        j = BasicEntity(Vec2(300, 600))
        j.get_component(SpriteComponent).size = Vec2(600, 20)
        j.add_component(ControlComponent(ControlType.FOURDIRECTION))
        j.add_component(PhysicsComponent(False, callback=self.collision))

        obj = BasicEntity(Vec2(100, 100))
        obj.add_component(PhysicsComponent(elasticity=1.5))

        self.esys.add_entity(j)
        self.esys.add_entity(obj)
        self.run()

    def collision(self, entity, others, space, data):
        pass

    def mousepress(self, evt):
        self.world.systems["Entity"].mousepress(evt)
        self.world.systems["UI"].mousepress(evt)

        if evt.button == MouseButton.LEFTCLICK.value:
            obj = BasicEntity(Vec2(evt.pos))
            obj.add_component(PhysicsComponent(elasticity=1.5))
            self.esys.add_entity(obj)

Game()
