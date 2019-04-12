from pyengine import Window, World, Entity
from pyengine.Components import PositionComponent, SpriteComponent


game = Window(800, 600)
monde = World()
game.set_world(monde)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")

subentity = Entity()
subentity.add_components(PositionComponent, [100, 100], [10, 10])
subentity.add_components(SpriteComponent, "images/sprite0.png")

entity.attach_entity(subentity)

entity.get_component(PositionComponent).set_position([200, 200])

monde.add_entity(entity)
monde.add_entity(subentity)

game.run()
