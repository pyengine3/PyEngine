from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *

from random import randint


def click(obj, b):
    if image.get_image() == "images/sprite0.png":
        image.set_image("images/sprite1.png")
    else:
        image.set_image("images/sprite0.png")
    image.set_size([randint(100, 300), randint(100, 300)])


game = Window(800, 600, True)
game.set_title("UI TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

button = Button([100, 100], "Appuie", click)
image = Image([200, 200], "images/sprite0.png")


system = monde.get_system(UISystem)
system.add_widget(button)
system.add_widget(image)

game.run()
