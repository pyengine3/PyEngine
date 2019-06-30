from pyengine import Entity, ControlType
from pyengine.Components import PositionComponent, PhysicsComponent, SpriteComponent, ControlComponent
from pyengine.Utils import Vec2
from pyengine.Network import Packet


class Character(Entity):
    def __init__(self, pos):
        super(Character, self).__init__()
        self.add_component(PositionComponent(pos))
        sprite = self.add_component(SpriteComponent("images/sprite0.png"))
        sprite.size = Vec2(20, 20)
        self.add_component(PhysicsComponent(False))

    def move_to(self, pos):
        self.get_component(PositionComponent).position = pos


class Player(Character):
    def __init__(self, pos, nw):
        super(Player, self).__init__(pos)
        self.add_component(ControlComponent(ControlType.FOURDIRECTION))
        self.get_component(SpriteComponent).sprite = "images/sprite1.png"
        self.get_component(SpriteComponent).size = Vec2(20, 20)
        self.nw = nw

    def update(self):
        super(Player, self).update()
        poscomp = self.get_component(PositionComponent)
        if self.nw.client:
            self.nw.client.send(Packet("pos", None, str(poscomp.position)))
