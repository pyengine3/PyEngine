import unittest
from pyengine import Window, WindowCallbacks
from pyengine.Utils import Color


class WindowTests(unittest.TestCase):
    def setUp(self):
        self.window = Window(100, 100)

    def test_update_rate(self):
        self.assertEqual(self.window.update_rate, 60)
        self.window.update_rate = 120
        self.assertEqual(self.window.update_rate, 120)

    def test_title(self):
        self.assertEqual(self.window.title, "PyEngine")
        self.window.title = "OUI"
        self.assertEqual(self.window.title, "OUI")

    def test_is_running(self):
        self.assertFalse(self.window.is_running)
        self.window.run()
        self.assertFalse(self.window.is_running)  # Code blocked while window run.

    def test_color(self):
        self.assertEqual(self.window.color, Color(0, 0, 0))
        self.window.color = Color(2, 4, 5)
        self.assertEqual(self.window.color, Color(2, 4, 5))

    def test_size(self):
        self.assertEqual(self.window.size, (100, 100))
        self.window.size = (110, 110)
        self.assertEqual(self.window.size, (110, 110))

    def test_debug(self):
        self.assertFalse(self.window.debug)
        self.window.debug = True
        self.assertTrue(self.window.debug)

    def test_callbacks(self):
        self.window.set_callback(WindowCallbacks.STOPWINDOW, self.cstop)
        self.window.set_callback(WindowCallbacks.CHANGEWORLD, self.cworld)
        self.window.set_callback(WindowCallbacks.OUTOFWINDOW, self.cout)
        self.window.call(WindowCallbacks.OUTOFWINDOW, None, None)
        self.window.call(WindowCallbacks.CHANGEWORLD)
        self.window.run()

    def cstop(self):
        self.assertFalse(self.window.is_running)

    def cworld(self):
        pass

    def cout(self, entity, pos):
        self.assertIsNone(entity)
        self.assertIsNone(pos)
