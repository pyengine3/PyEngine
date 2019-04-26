from pyengine.Exceptions import ComponentIntializedError
from pyengine.Components import PositionComponent, SpriteComponent

__all__ = ["LifeBarComponent"]


class LifeBarComponent:
    name = "LifeBarComponent"

    def __init__(self):
        self.entity = None
        self.life = 0
        self.maxlife = 0
        self.sprites = None
        self.maxwidth = 0
        self.offset = None
        self.backentity = None
        self.frontentity = None
        self.created_sprites = False
        self.initialized = False

    def initialize(self, entity, maxlife=100, sprites=None, offset=None):
        if offset is None:
            offset = [0, 0]

        if self.initialized:
            raise ComponentIntializedError("LifeBarComponent already initialized")
        self.initialized = True
        self.entity = entity
        self.maxlife = maxlife
        self.life = maxlife
        self.sprites = sprites
        self.offset = offset

    def create_life_sprites(self):
        if self.sprites is not None and not self.created_sprites:
            self.created_sprites = True

            from pyengine.Entity import Entity  # Avoid import cycling

            self.backentity = Entity()
            self.backentity.add_components(PositionComponent,
                                           self.entity.get_component(PositionComponent).get_position(),
                                           self.offset)
            self.backentity.add_components(SpriteComponent, self.sprites[0])

            self.frontentity = Entity()
            self.frontentity.add_components(PositionComponent,
                                            self.entity.get_component(PositionComponent).get_position(),
                                            self.offset)
            self.frontentity.add_components(SpriteComponent, self.sprites[1])

            self.entity.attach_entity(self.backentity)
            self.entity.system.add_entity(self.backentity)
            self.entity.attach_entity(self.frontentity)
            self.entity.system.add_entity(self.frontentity)

            self.maxwidth = self.frontentity.image.get_size()[0]

    def update_life(self, life):
        if life < 0:
            self.life = 0
        else:
            self.life = life
        if self.created_sprites:
            width = int(self.maxwidth * self.life / self.maxlife)
            height = self.frontentity.image.get_size()[1]
            sprite = self.frontentity.get_component(SpriteComponent)
            sprite.set_size((width, height))
