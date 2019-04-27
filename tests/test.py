from pyengine import Window, World, Entity, ControlType, GameState
from pyengine.Components import *
from pyengine.Systems import *
from pyengine.Enums import WorldCallbacks


def fall(objet):
    print("CHANGE STATE")
    game.set_current_state("LOOSE")


game = Window(800, 600, True)
state1 = GameState("JEU")
state2 = GameState("LOOSE")
game.add_state(state1)
game.add_state(state2)

monde = World()
monde.set_callback(WorldCallbacks.FALL, fall)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")
entity.add_components(ControlComponent, ControlType.CLASSICJUMP)
phys = entity.add_components(PhysicsComponent, True)

entitySystem = monde.get_system(EntitySystem)
entitySystem.add_entity(entity)
state1.set_world(monde)

monde2 = World()

text = Entity()
text.add_components(PositionComponent, [100, 100])
text.add_components(TextComponent, "LOOSE")
entitySystem2 = monde2.get_system(EntitySystem)
entitySystem2.add_entity(text)
state2.set_world(monde2)

game.run()
