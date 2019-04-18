from pyengine import Window, World, Entity, ControlType
from pyengine.Components import *
from pyengine.Systems import *


def collision(id1, id2):
    print("Collision between", id1, "and", id2)


game = Window(800, 600, True)
monde = World()
game.set_world(monde)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")
entity.add_components(ControlComponent, ControlType.CLICKFOLLOW)
phys = entity.add_components(PhysicsComponent, False)
phys.set_callback(collision)

subentity = Entity()
subentity.add_components(PositionComponent, [100, 100], [10, -10])
subentity.add_components(TextComponent, "TEST")

entity.attach_entity(subentity)

bloc = Entity()
bloc.add_components(PositionComponent, [300, 300])
bloc.add_components(SpriteComponent, "images/sprite1.png")
bloc.add_components(PhysicsComponent, False)
bloc2 = Entity()
bloc2.add_components(PositionComponent, [350, 350])
bloc2.add_components(SpriteComponent, "images/sprite1.png", 10)
bloc2.add_components(PhysicsComponent, False)

entitySystem = monde.get_system(EntitySystem)
entitySystem.add_entity(bloc)
entitySystem.add_entity(bloc2)
entitySystem.add_entity(entity)
entitySystem.add_entity(subentity)

bloc.get_component(SpriteComponent).set_rotation(45)

musicSystem = monde.get_system(MusicSystem)
musicSystem.set_loop(True)
musicSystem.add("musique/Heikousen.mp3")
musicSystem.add("musique/Richard.mp3")
musicSystem.play()

game.run()
