from pyengine import Window, GameState, Entity
from pyengine.Components import *
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Widgets import *

game = Window(300, 300)

state = GameState("JEU")
game.add_state(state)

e = Entity()
e.add_component(PositionComponent([100, 100]))
sprite = e.add_component(SpriteComponent("images/sprite0.png"))
sprite.set_size([100, 20])

image = Image([100, 100], "images/sprite1.png")

state.get_system(EntitySystem).add_entity(e)
state.get_system(UISystem).add_widget(image)

game.run()
