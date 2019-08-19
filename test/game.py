import math

from pyengine import Window, MouseButton
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent
from pyengine.Entities import Entity
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Widgets import Image
from pyengine.Utils import Vec2


class BasicEntity(Entity):
    def __init__(self, pos):
        super(BasicEntity, self).__init__()

        self.add_component(PositionComponent(pos))
        self.add_component(SpriteComponent("images/sprite0.png", 2))


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(1300, 650, debug=True)

        self.world.mousepress = self.mousepress
        self.esys = self.world.get_system(EntitySystem)

        bas = BasicEntity(Vec2(650, 600))
        bas.get_component(SpriteComponent).size = Vec2(800, 20)
        bas.add_component(PhysicsComponent(False, elasticity=.9))

        gauche = BasicEntity(Vec2(100, 400))
        gauche.get_component(SpriteComponent).size = Vec2(500, 20)
        gauche.get_component(SpriteComponent).rotation = -60
        gauche.add_component(PhysicsComponent(False, elasticity=.9))

        droit = BasicEntity(Vec2(1200, 400))
        droit.get_component(SpriteComponent).size = Vec2(500, 20)
        droit.get_component(SpriteComponent).rotation = 60
        droit.add_component(PhysicsComponent(False, elasticity=.9))

        spinner = BasicEntity(Vec2(650, 450))
        spinner.get_component(SpriteComponent).size = Vec2(300, 20)
        phys = spinner.add_component(PhysicsComponent(False, elasticity=.9))
        phys.body.angular_velocity = math.radians(120)

        spinner2 = BasicEntity(Vec2(1050, 300))
        spinner2.get_component(SpriteComponent).size = Vec2(300, 20)
        phys2 = spinner2.add_component(PhysicsComponent(False, elasticity=.9))
        phys2.body.angular_velocity = math.radians(120)

        spinner3 = BasicEntity(Vec2(250, 300))
        spinner3.get_component(SpriteComponent).size = Vec2(300, 20)
        phys3 = spinner3.add_component(PhysicsComponent(False, elasticity=.9))
        phys3.body.angular_velocity = math.radians(120)

        obj = BasicEntity(Vec2(150, 100))
        obj.add_component(PhysicsComponent(elasticity=.9, can_rot=False))

        self.esys.add_entity(bas)
        self.esys.add_entity(gauche)
        self.esys.add_entity(droit)
        self.esys.add_entity(spinner)
        self.esys.add_entity(spinner2)
        self.esys.add_entity(spinner3)
        self.esys.add_entity(obj)

        back = Image(Vec2(0, 0), "images/sprite1.png")
        self.world.get_system(UISystem).add_widget(back)

        self.run()

    def mousepress(self, evt):
        self.world.systems["Entity"].mousepress(evt)
        self.world.systems["UI"].mousepress(evt)

        if evt.button == MouseButton.LEFTCLICK.value:
            obj = BasicEntity(Vec2(evt.pos))
            obj.add_component(PhysicsComponent(elasticity=.9))
            self.esys.add_entity(obj)


Game()
