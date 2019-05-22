from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *


game = Window(800, 600, (200, 145, 208), True)
game.set_title("ShowHide TEST")
state = GameState("BASE")
game.add_state(state)

entry = Entry([100, 100], 200, "images/sprite0.png")


system = state.get_system(UISystem)
system.add_widget(entry)

game.run()
