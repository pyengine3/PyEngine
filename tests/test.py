from pyengine import Window, World, Entity
from pyengine.Components import PositionComponent, SpriteComponent


game = Window(800, 600)
monde = World()
game.set_world(monde)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")
monde.add_entity(entity)

game.run()
