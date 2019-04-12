from pyengine import Window, World, Entity


game = Window(800, 600)
monde = World()
game.set_world(monde)

entity = Entity()
monde.add_entity(entity)

game.run()
