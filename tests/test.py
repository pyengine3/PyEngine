from pyengine import Window, GameState, Entity, ControlType, Controls, StateCallbacks
from pyengine.Systems import *
from pyengine.Components import *
from pyengine.Components.ControlComponent import const


def quitter(obj, pos):
    if state.get_system(EntitySystem).has_entity(bloc):
        state.get_system(EntitySystem).remove_entity(bloc)


game = Window(800, 600, (200, 145, 208), True)
game.set_title("Controles TEST")
state = GameState("BASE")
game.add_state(state)

entity = Entity()
entity.add_component(PositionComponent([100, 100]))
entity.add_component(SpriteComponent("images/sprite0.png"))
entity.add_component(PhysicsComponent())
control = entity.add_component(ControlComponent(ControlType.CLASSICJUMP))
control.set_control(Controls.UPJUMP, const.K_SPACE)

state.set_callback(StateCallbacks.OUTOFWINDOW, quitter)

bloc = Entity()
bloc.add_component(PositionComponent([100, 200]))
bloc.add_component(SpriteComponent("images/sprite1.png", 1, 45))
bloc.add_component(PhysicsComponent(False))


system = state.get_system(EntitySystem)
system.add_entity(entity)
system.add_entity(bloc)

game.run()
