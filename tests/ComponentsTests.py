import unittest
from pyengine.Components import *
from pyengine import Entity, ControlType, Controls, const
from pyengine.Utils import Vec2, Color, Font
import pygame


class PositionTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.component = self.entity.add_component(PositionComponent(Vec2(10, 10)))

    def test_pos(self):
        self.assertEqual(self.component.position, Vec2(10, 10))
        self.component.position = Vec2(11, 11)
        self.assertEqual(self.component.position, Vec2(11, 11))


class LifeTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.component = self.entity.add_component(LifeComponent(100))

    def test_life(self):
        self.assertEqual(self.component.life, 100)
        self.component.life = 50
        self.assertEqual(self.component.life, 50)
        self.component.life = 500
        self.assertEqual(self.component.life, 100)
        self.component.life = -5
        self.assertEqual(self.component.life, 0)

    def test_maxlife(self):
        self.assertEqual(self.component.maxlife, 100)
        self.component.maxlife = 110
        self.assertEqual(self.component.maxlife, 110)


class ControlTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.component = ControlComponent(ControlType.FOURDIRECTION)

    def test_speed(self):
        self.assertEqual(self.component.speed, 5)
        self.component.speed = 4
        self.assertEqual(self.component.speed, 4)

    def test_controls(self):
        self.assertEqual(self.component.get_control(Controls.LEFT), const.K_LEFT)
        self.component.set_control(Controls.UPJUMP, const.K_SPACE)
        self.assertEqual(self.component.get_control(Controls.UPJUMP), const.K_SPACE)


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.p = self.entity.add_component(PositionComponent(Vec2(10, 10)))
        self.component = self.entity.add_component(MoveComponent(Vec2(10, 10)))

    def test_direction(self):
        self.assertEqual(self.component.direction, Vec2(10, 10))
        self.component.direction = Vec2(5, 5)
        self.assertEqual(self.component.direction, Vec2(5, 5))

    def test_move(self):
        self.assertEqual(self.p.position, Vec2(10, 10))
        self.component.update()
        self.assertEqual(self.p.position, Vec2(20, 20))


class FakeEntitySystem:
    def __init__(self):
        self.entities = pygame.sprite.Group()


class PhysicsTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.entity.system = FakeEntitySystem()
        self.entity.add_component(SpriteComponent("files/sprite0.png"))
        self.component = self.entity.add_component(PhysicsComponent())
        self.p = self.entity.add_component(PositionComponent(Vec2(10, 10)))

    def test_gravity_value(self):
        self.assertEqual(self.component.gravity, 5)
        self.component.gravity = 4
        self.assertEqual(self.component.gravity, 4)

    def test_gravity(self):
        self.assertEqual(self.p.position, Vec2(10, 10))
        self.component.timegravity = 0
        self.component.update_gravity()
        self.assertEqual(self.p.position, Vec2(10, 15))

    def test_callback(self):
        self.assertEqual(self.component.callback, None)
        self.component.callback = self.callback
        self.assertEqual(self.component.callback, self.callback)

    def callback(self, obj, cause):
        pass


class SpriteTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()
        self.component = self.entity.add_component(SpriteComponent("files/sprite0.png"))
        self.basesize = [self.entity.image.get_rect().width, self.entity.image.get_rect().height]

    def text_size(self):
        self.assertEqual(self.component.size, self.basesize)
        self.component.size = [1, 1]
        self.assertEqual(self.component.size, [1, 1])

    def test_scale(self):
        self.assertEqual(self.component.scale, 1)
        self.component.scale = 2
        self.assertEqual(self.component.scale, 2)
        self.assertEqual(self.component.size, [self.basesize[0]*2, self.basesize[1]*2])

    def test_rotation(self):
        self.assertEqual(self.component.rotation, 0)
        self.component.rotation = 10
        self.assertEqual(self.component.rotation, 10)
        self.component.rotation = 45
        self.assertEqual(self.component.rotation, 45)

    def test_sprite(self):
        self.assertEqual(self.component.sprite, "files/sprite0.png")
        self.component.sprite = "files/sprite1.png"
        self.assertEqual(self.component.sprite, "files/sprite1.png")


class TextTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.entity = Entity()
        self.component = self.entity.add_component(TextComponent("test"))

    def test_scale(self):
        self.assertEqual(self.component.scale, 1)
        rect = self.component.render().get_rect()
        basesize = [rect.width, rect.height]
        self.component.scale = 2
        self.assertEqual(self.component.scale, 2)
        rect = self.component.render().get_rect()
        self.assertEqual([rect.width, rect.height], [basesize[0] * 2, basesize[1] * 2])

    def test_text(self):
        self.assertEqual(self.component.text, "test")
        self.component.text = "OUI"
        self.assertEqual(self.component.text, "OUI")

    def test_color(self):
        self.assertEqual(self.component.color, Color())
        self.component.color = Color(2, 23, 2)
        self.assertEqual(self.component.color, Color(2, 23, 2))

    def test_font(self):
        self.assertEqual(self.component.font, Font())
        self.component.font = Font("arial", 13)
        self.assertEqual(self.component.font, Font("arial", 13))

    def test_background(self):
        self.assertEqual(self.component.background, None)
        self.component.background = Color()
        self.assertEqual(self.component.background, Color())
