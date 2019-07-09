from pyengine.Prefabs import *
from pyengine.Utils import Vec2
import unittest


class TilemapTests(unittest.TestCase):
    def test_tilemap(self):
        self.tilemap = Tilemap(Vec2(), "files/tilemap/TESTMAP.json")

        self.assertEqual(self.tilemap.folder, "files/tilemap/")
        self.assertEqual(len(self.tilemap.tiles), 21)