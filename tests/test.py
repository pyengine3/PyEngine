from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *


game = Window(800, 600, (200, 145, 208), True)
game.set_title("Move TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

entry = Entry([100, 100])

system = monde.get_system(UISystem)
system.add_widget(entry)

game.run()
