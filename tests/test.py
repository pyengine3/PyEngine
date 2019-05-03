from pyengine import Window, GameState, Entity
from pyengine.Systems import *
from pyengine.Components import *


def collision(obj, cause):
    direction = ball.get_component(MoveComponent).get_direction()
    ball.get_component(MoveComponent).set_direction([0, -direction[1]])


game = Window(800, 600, (200, 145, 208), True)
game.set_title("Move TEST")
state = GameState("BASE")
game.add_state(state)

monde = state.get_world()

bloc1 = Entity()
bloc1.add_component(PositionComponent([100, 100]))
bloc1.add_component(SpriteComponent("images/sprite0.png"))
bloc1.add_component(PhysicsComponent(False))

bloc2 = Entity()
bloc2.add_component(PositionComponent([100, 300]))
bloc2.add_component(SpriteComponent("images/sprite0.png"))
bloc2.add_component(PhysicsComponent(False))

ball = Entity()
ball.add_component(PositionComponent([100, 200]))
ball.add_component(SpriteComponent("images/sprite1.png"))
physics = ball.add_component(PhysicsComponent(False))
physics.set_callback(collision)
ball.add_component(MoveComponent([0, 1]))

system = monde.get_system(EntitySystem)
system.add_entity(bloc1)
system.add_entity(bloc2)
system.add_entity(ball)

game.run()
