from pyengine import Window, WindowCallbacks, MouseButton
from pyengine.Systems import EntitySystem
from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent
from pyengine.Utils import Vec2
import math


class BasicEntity(Entity):
    def __init__(self, pos):
        super(BasicEntity, self).__init__()

        self.add_component(PositionComponent(pos))
        self.add_component(SpriteComponent("images/sprite0.png", 2))


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(1200, 750, debug=True)

        self.set_callback(WindowCallbacks.RUNWINDOW, self.launch)

        self.world.mousepress = self.mousepress
        self.esys = self.world.get_system(EntitySystem)

        bas = BasicEntity(Vec2(600, 700))
        bas.get_component(SpriteComponent).size = Vec2(800, 20)
        bas.add_component(PhysicsComponent(False, elasticity=1))

        self.gauche = BasicEntity(Vec2(50, 500))
        self.gauche.get_component(SpriteComponent).size = Vec2(500, 20)
        self.gauche.add_component(PhysicsComponent(False, elasticity=1))

        self.droit = BasicEntity(Vec2(1150, 500))
        self.droit.get_component(SpriteComponent).size = Vec2(500, 20)
        self.droit.add_component(PhysicsComponent(False, elasticity=1))

        obj = BasicEntity(Vec2(100, 100))
        obj.add_component(PhysicsComponent(elasticity=1))

        self.esys.add_entity(bas)
        self.esys.add_entity(self.gauche)
        self.esys.add_entity(self.droit)
        self.esys.add_entity(obj)
        self.run()

    def launch(self):
        self.gauche.get_component(PhysicsComponent).body.angle = math.radians(-60)
        self.droit.get_component(PhysicsComponent).body.angle = math.radians(60)

    def mousepress(self, evt):
        self.world.systems["Entity"].mousepress(evt)
        self.world.systems["UI"].mousepress(evt)

        if evt.button == MouseButton.LEFTCLICK.value:
            obj = BasicEntity(Vec2(evt.pos))
            obj.add_component(PhysicsComponent(elasticity=1))
            self.esys.add_entity(obj)


Game()
