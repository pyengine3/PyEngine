from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *

from random import randint


def click(obj, b):
    if image.get_image() == "images/sprite0.png":
        image.set_image("images/sprite1.png")
    else:
        image.set_image("images/sprite0.png")
    obj.set_size([randint(100, 200), randint(100, 200)])
    print(entry.get_text())


game = Window(800, 600, (200, 145, 208), True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

button = Button([100, 100], "Appuie", click)
image = Image([200, 200], "images/sprite0.png")
entry = Entry([300, 300])

system = monde.get_system(UISystem)
system.add_widget(button)
system.add_widget(image)
system.add_widget(entry)

game.run()
