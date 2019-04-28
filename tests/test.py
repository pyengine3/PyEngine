from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *

from random import randint


def click(obj, b):
    obj.set_position([randint(0, 800-100), randint(0, 600-100)])


game = Window(800, 600, True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

button = Button([100, 100], "Appuie", click, [100, 100])
button2 = Button([150, 150], "Appuie 2", click, [100, 100], "images/sprite0.png")

system = monde.get_system(UISystem)
system.add_widget(button)
system.add_widget(button2)

game.run()
