from pyengine.Entities import *
from pyengine.Utils import Vec2
from pyengine.Components import *
from pyengine.Exceptions import CompatibilityError
from pyengine import ControlType
import unittest


class TilemapTests(unittest.TestCase):
    def setUp(self):
        self.tilemap = Tilemap(Vec2(), "files/tilemap/TESTMAP.json")

    def test_tilemap(self):
        self.assertEqual(self.tilemap.folder, "files/tilemap/")
        self.assertEqual(len(self.tilemap.tiles), 21)

    def test_scale(self):
        self.assertEqual(self.tilemap.scale, 1)
        self.tilemap.scale = 2
        self.assertEqual(self.tilemap.scale, 2)


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.e = Entity()
        self.components = [
            PositionComponent(Vec2(10, 10)),
            SpriteComponent("files/sprite0.png"),
            PhysicsComponent(),
            LifeComponent(100),
            MoveComponent(Vec2(1, 1)),
            ControlComponent(ControlType.FOURDIRECTION)
        ]

    def test_attached_entity(self):
        e2 = Entity()
        self.e.attach_entity(e2)
        self.assertTrue(e2 in self.e.attachedentities)

    def test_components(self):
        with self.assertRaises(TypeError):
            self.e.add_component(1)
        for i in self.components:
            self.e.add_component(i)
        with self.assertRaises(CompatibilityError):
            self.e.add_component(TextComponent(""))
        for i in self.components:
            self.assertTrue(self.e.has_component(type(i)))
        self.assertFalse(self.e.has_component(TextComponent))
        for i in self.components:
            self.assertEqual(self.e.get_component(type(i)), i)
        self.e.remove_component(PhysicsComponent)
        self.assertFalse(self.e.has_component(PhysicsComponent))
