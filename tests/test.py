from pyengine import Window, World, Entity, ControlType
from pyengine.Components import *
from pyengine.Systems import *
from pyengine.Enums import WorldCallbacks


def collision(objet, cause):
    print("COLLISION")


def fall(objet):
    if objet.has_component(PositionComponent):
        position = objet.get_component(PositionComponent)
        position.set_position([position.x, 0])
    print("FALL :", objet.id)


game = Window(800, 600, True)
monde = World()
monde.set_callback(WorldCallbacks.FALL, fall)
game.set_world(monde)

entity = Entity()
entity.add_components(PositionComponent, [100, 100])
entity.add_components(SpriteComponent, "images/sprite0.png")
entity.add_components(ControlComponent, ControlType.DOUBLEJUMP)
entity.add_components(LifeBarComponent, 100, ["images/lifebar-back.png", "images/lifebar-front.png"], [-30, -15])
phys = entity.add_components(PhysicsComponent)
phys.set_callback(collision)

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

lifebar = entity.get_component(LifeBarComponent)
lifebar.create_life_sprites()
lifebar.update_life(50)

bloc.get_component(SpriteComponent).set_rotation(45)

game.run()
