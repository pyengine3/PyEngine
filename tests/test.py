from pyengine import Window, GameState, Entity
from pyengine.Components import *
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Widgets import *

game = Window(300, 300, debug=True)

state = GameState("JEU")
game.add_state(state)

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

state.get_system(EntitySystem).add_entity(e)
state.get_system(EntitySystem).add_entity(e2)
state.get_system(EntitySystem).remove_entity(e)
state.get_system(EntitySystem).add_entity(e3)

print(state.get_system(EntitySystem).get_entity(1).get_component(PositionComponent).get_position())
print(state.get_system(EntitySystem).get_entity(2).get_component(PositionComponent).get_position())

state.get_system(UISystem).add_widget(w)

game.run()
