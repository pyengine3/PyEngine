from pyengine import Window, Entity, ControlType
from pyengine.Components import *
from pyengine.Systems import EntitySystem, UISystem, CameraSystem
from pyengine.Widgets import *


def move_cam(pos, click):
    game.world.get_system(CameraSystem).position = [10, 10]


game = Window(300, 300, debug=True)

e = Entity()
e.add_component(PositionComponent([100, 100]))
sprite = e.add_component(SpriteComponent("images/sprite0.png"))
sprite.size = [100, 20]
e2 = Entity()
e2.add_component(PositionComponent([100, 130]))
sprite = e2.add_component(SpriteComponent("images/sprite0.png"))
sprite.size = [100, 20]
e2.add_component(ControlComponent(ControlType.FOURDIRECTION))
e3 = Entity()
e3.add_component(PositionComponent([100, 160]))
sprite = e3.add_component(SpriteComponent("images/sprite0.png"))
sprite.size = [100, 20]
e3.add_component(PhysicsComponent(False))

w = Image([100, 100], "images/sprite0.png", [100, 20])
b = Button([10, 10], "Camera", move_cam)

game.world.get_system(EntitySystem).add_entity(e)
game.world.get_system(EntitySystem).add_entity(e2)
game.world.get_system(EntitySystem).remove_entity(e)
game.world.get_system(EntitySystem).add_entity(e3)

game.world.get_system(UISystem).add_widget(w)
game.world.get_system(UISystem).add_widget(b)

game.run()
