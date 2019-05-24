from pyengine import Window, GameState, Entity
from pyengine.Systems import *
from pyengine.Components import PositionComponent, TextComponent
from pyengine.Widgets import *
from pyengine.Utils import Colors


def click(pos, click):
    text = entity.get_component(TextComponent)
    text.set_color(Colors.BLUE.value.clone().lighter())
    text.set_font(text.get_font().set_size(text.get_font().get_size()+1))
    bouton.get_label().set_color(Colors.RED.value.clone().lighter())
    bouton.get_label().set_text("TEST")


game = Window(800, 600, (0, 0, 0), True)
game.set_title("ShowHide TEST")
state = GameState("BASE")
game.add_state(state)

bouton = Button([0, 0], "CLICK", click)
entity = Entity()
entity.add_component(PositionComponent([100, 100]))
entity.add_component(TextComponent("A"))

system = state.get_system(UISystem)
system.add_widget(bouton)
system2 = state.get_system(EntitySystem)
system2.add_entity(entity)

game.run()
