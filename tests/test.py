from pyengine import Window, World, GameState
from pyengine.Systems import *
from pyengine.Widgets import *


game = Window(800, 600, True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = World()
state.set_world(monde)

label = Label([100, 100], "TEST", (255, 255, 255), ["arial", 25, True, True])
image = Image([100, 100], "images/sprite0.png", [200, 100])

uisystem = monde.get_system(UISystem)
uisystem.add_widget(image)
uisystem.add_widget(label)

image.set_position([110, 100])

game.run()
