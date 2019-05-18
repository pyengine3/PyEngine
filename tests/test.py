from pyengine import Window, GameState
from pyengine.Systems import *
from pyengine.Widgets import *


def click(obj, button):
    if image.is_show():
        image.hide()
    else:
        image.show()


game = Window(800, 600, (200, 145, 208), True)
game.set_title("ShowHide TEST")
state = GameState("BASE")
game.add_state(state)

button = Button([100, 100], "Clique", click)

image = Image([300, 300], "images/sprite0.png")


system = state.get_system(UISystem)
system.add_widget(button)
system.add_widget(image)

game.run()
