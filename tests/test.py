from pyengine import Window, World, Entity, ControlType
from pyengine.Components import *


game = Window(800, 600)
monde = World()
game.set_world(monde)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")
entity.add_components(ControlComponent, ControlType.FOURDIRECTION, 2)
entity.add_components(PhysicsComponent, True, 2)

subentity = Entity()
subentity.add_components(PositionComponent, [100, 100], [10, 10])
subentity.add_components(SpriteComponent, "images/sprite0.png")

entity.attach_entity(subentity)

bloc = Entity()
bloc.add_components(PositionComponent, [300, 300])
bloc.add_components(SpriteComponent, "images/sprite1.png")
bloc.add_components(PhysicsComponent, True, 5)

monde.add_entity(bloc)
monde.add_entity(entity)
monde.add_entity(subentity)

game.run()
