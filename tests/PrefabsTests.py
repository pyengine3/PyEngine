from pyengine.Prefabs import *
from pyengine.Utils import Vec2
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
