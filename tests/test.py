from pyengine import Window, Entity
from pyengine.Components import *
from pyengine.Systems import EntitySystem, UISystem, CameraSystem
from pyengine.Widgets import *


def move_cam(pos, click):
    world.get_system(CameraSystem).set_position([10, 10])


game = Window(300, 300, debug=True)
world = game.get_world()

e = Entity()
e.add_component(PositionComponent([100, 100]))
sprite = e.add_component(SpriteComponent("images/sprite0.png"))
sprite.set_size([100, 20])
e2 = Entity()
e2.add_component(PositionComponent([100, 130]))
sprite = e2.add_component(SpriteComponent("images/sprite0.png"))
sprite.set_size([100, 20])
e3 = Entity()
e3.add_component(PositionComponent([100, 160]))
sprite = e3.add_component(SpriteComponent("images/sprite0.png"))
sprite.set_size([100, 20])

w = Image([100, 100], "images/sprite0.png", [100, 20])
b = Button([10, 10], "Camera", move_cam)

world.get_system(EntitySystem).add_entity(e)
world.get_system(EntitySystem).add_entity(e2)
world.get_system(EntitySystem).remove_entity(e)
world.get_system(EntitySystem).add_entity(e3)

world.get_system(UISystem).add_widget(w)
world.get_system(UISystem).add_widget(b)

game.run()
