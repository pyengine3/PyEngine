from pyengine import Window, GameState, Entity
from pyengine.Systems import *
from pyengine.Widgets import *
from pyengine.Components import *


game = Window(800, 600, True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

entity = Entity()
entity.add_component(PositionComponent([100, 100]))
entity.add_component(SpriteComponent("images/sprite0.png"))
life = entity.add_component(LifeBarComponent(100, ["images/lifebar-back.png", "images/lifebar-front.png"]))

entitysystem = monde.get_system(EntitySystem)
entitysystem.add_entity(entity)

game.run()
