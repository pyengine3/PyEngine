import unittest
from pyengine import World, Window
from pyengine.Systems import *


class WorldTests(unittest.TestCase):
    def setUp(self):
        self.w = Window(2, 2)
        self.world = World(self.w)

    def test_create(self):
        with self.assertRaises(TypeError):
            w = World(1)

    def test_window(self):
        self.assertEqual(self.world.window, self.w)

    def test_systems(self):
        self.assertEqual(self.world.get_system(EntitySystem), self.world.systems["Entity"])
        self.assertEqual(self.world.get_system(MusicSystem), self.world.systems["Music"])
        self.assertEqual(self.world.get_system(UISystem), self.world.systems["UI"])
        self.assertEqual(self.world.get_system(SoundSystem), self.world.systems["Sound"])
        self.assertEqual(self.world.get_system(CameraSystem), self.world.systems["Camera"])

    def test_phys(self):
        self.assertEqual(self.world.space.gravity, [0, -900])
        self.world.space.gravity = [0, 900]
        self.assertEqual(self.world.space.gravity, [0, 900])


