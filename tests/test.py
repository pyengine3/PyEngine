from pyengine import Window, GameState, Entity
from pyengine.Systems import *
from pyengine.Components import *
from pyengine.Enums import ControlType, Controls
from pyengine.Components.ControlComponent import const


game = Window(800, 600, (200, 145, 208), True)
game.set_title("Controles TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

entity = Entity()
entity.add_component(PositionComponent([100, 100]))
entity.add_component(SpriteComponent("images/sprite0.png"))
entity.add_component(PhysicsComponent())
control = entity.add_component(ControlComponent(ControlType.CLASSICJUMP))
control.set_control(Controls.UPJUMP, const.K_SPACE)

bloc = Entity()
bloc.add_component(PositionComponent([100, 200]))
bloc.add_component(SpriteComponent("images/sprite1.png"))
bloc.add_component(PhysicsComponent(False))


system = monde.get_system(EntitySystem)
system.add_entity(entity)
system.add_entity(bloc)

game.run()
