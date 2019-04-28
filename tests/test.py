from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *

from random import randint


def click(obj, b):
    label.set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
    obj.get_label().set_color((randint(0, 255), randint(0, 255), randint(0, 255)))
    obj.get_label().set_text("CECI EST BIEN TROP LONG !")
    obj.update()


game = Window(800, 600, True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

button = Button([100, 100], "Appuie", click)
label = Label([200, 200], "RAINBOW !", None, ["arial", 35])

system = monde.get_system(UISystem)
system.add_widget(button)
system.add_widget(label)

game.run()
