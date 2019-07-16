import unittest
from pyengine.Systems import *
from pyengine.Utils import Vec2
from pyengine import Entity
from pyengine.Widgets import Label
from pyengine.Exceptions import NoObjectError
from pyengine.Components import PositionComponent, TextComponent, SpriteComponent


class MusicTests(unittest.TestCase):
    def setUp(self):
        self.system = MusicSystem()

    def test_loop(self):
        self.assertEqual(self.system.loop, False)
        self.system.loop = True
        self.assertEqual(self.system.loop, True)

    def test_volume(self):
        self.assertEqual(self.system.volume, 100)
        with self.assertRaises(ValueError):
            self.system.volume = 102
        self.system.volume = 40
        self.assertEqual(self.system.volume, 40)

    def test_queue(self):
        self.assertEqual(self.system.queue, [])
        self.system.add("test")
        self.assertEqual(self.system.queue, ["test"])
        self.system.clear_queue()
        self.assertEqual(self.system.queue, [])


class SoundTests(unittest.TestCase):
    def setUp(self):
        self.system = SoundSystem()

    def test_nb_channel(self):
        self.assertEqual(self.system.number_channel, 8)
        self.system.number_channel = 10
        self.assertEqual(self.system.number_channel, 10)

    def test_volume(self):
        self.assertEqual(self.system.volume, 100)
        with self.assertRaises(ValueError):
            self.system.volume = 102
        self.system.volume = 40
        self.assertEqual(self.system.volume, 40)


class FakeWorld:
    def __init__(self):
        pass


class CameraTests(unittest.TestCase):
    def setUp(self):
        self.system = CameraSystem(FakeWorld())

    def test_entity_follow(self):
        self.assertEqual(self.system.entity_follow, None)

    def test_offset(self):
        self.assertEqual(self.system.offset, Vec2())
        self.system.offset = Vec2(1, 1)
        self.assertEqual(self.system.offset, Vec2(1, 1))


class UITests(unittest.TestCase):
    def setUp(self):
        self.system = UISystem(FakeWorld())
        self.w = Label(Vec2(), "")

    def test_management_widget(self):
        self.system.add_widget(self.w)
        self.assertEqual(self.system.get_widget(0), self.w)
        self.assertEqual(self.system.has_widget(self.w), True)
        self.system.remove_widget(self.w)
        self.assertEqual(self.system.has_widget(self.w), False)


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.system = EntitySystem(FakeWorld())
        self.e = Entity()

    def test_management_entity(self):
        with self.assertRaises(NoObjectError):
            self.system.add_entity(self.e)
        self.e.add_component(PositionComponent(Vec2()))
        with self.assertRaises(NoObjectError):
            self.system.add_entity(self.e)
        self.e.add_component(SpriteComponent("files/sprite0.png"))
        self.system.add_entity(self.e)
        self.assertIn(self.e, self.system.entities.sprites())
        self.assertEqual(self.system.get_entity(0), self.e)
        self.assertEqual(self.system.has_entity(self.e), True)
        self.system.remove_entity(self.e)
        self.assertEqual(self.system.has_entity(self.e), False)

    def test_management_text(self):
        with self.assertRaises(NoObjectError):
            self.system.add_entity(self.e)
        self.e.add_component(PositionComponent(Vec2()))
        with self.assertRaises(NoObjectError):
            self.system.add_entity(self.e)
        self.e.add_component(TextComponent(""))
        self.system.add_entity(self.e)
        self.assertIn(self.e, self.system.entities.sprites())
        self.assertEqual(self.system.get_entity(0), self.e)
        self.assertEqual(self.system.has_entity(self.e), True)
        self.system.remove_entity(self.e)
        self.assertEqual(self.system.has_entity(self.e), False)
