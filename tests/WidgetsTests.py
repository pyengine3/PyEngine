import unittest
from pyengine.Widgets import *
from pyengine.Utils import Vec2, Color, Font, Colors
import pygame


class WidgetTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.widget = None

    def test_pos(self):
        if self.widget is not None:
            self.assertEqual(self.widget.position, Vec2(10, 10))
            self.widget.position = Vec2(11, 11)
            self.assertEqual(self.widget.position, Vec2(11, 11))


class LabelTests(WidgetTests):
    def setUp(self):
        super(LabelTests, self).setUp()
        self.widget = Label(Vec2(10, 10), "test")

    def test_text(self):
        self.assertEqual(self.widget.text, "test")
        self.widget.text = "OUI"
        self.assertEqual(self.widget.text, "OUI")

    def test_color(self):
        self.assertEqual(self.widget.color, Color())
        self.widget.color = Color(2, 23, 2)
        self.assertEqual(self.widget.color, Color(2, 23, 2))

    def test_font(self):
        self.assertEqual(self.widget.font, Font())
        self.widget.font = Font("arial", 13)
        self.assertEqual(self.widget.font, Font("arial", 13))

    def test_background(self):
        self.assertEqual(self.widget.background, None)
        self.widget.background = Color()
        self.assertEqual(self.widget.background, Color())


class ImageTests(WidgetTests):
    def setUp(self):
        super(ImageTests, self).setUp()
        self.widget = Image(Vec2(10, 10), "files/sprite0.png")

    def test_sprite(self):
        self.assertEqual(self.widget.sprite, "files/sprite0.png")
        self.widget.sprite = "files/sprite1.png"
        self.assertEqual(self.widget.sprite, "files/sprite1.png")

    def test_size(self):
        self.assertEqual(self.widget.size,
                         Vec2(self.widget.image.get_rect().width, self.widget.image.get_rect().height))
        self.widget.size = Vec2(10, 10)
        self.assertEqual(Vec2(self.widget.image.get_rect().width, self.widget.image.get_rect().height), Vec2(10, 10))


class ButtonTests(WidgetTests):
    def setUp(self):
        super(ButtonTests, self).setUp()
        self.widget = Button(Vec2(10, 10), "test")

    def test_text(self):
        self.assertEqual(self.widget.label.text, "test")
        self.widget.label.text = "OUI"
        self.assertEqual(self.widget.label.text, "OUI")

    def test_sprite(self):
        self.assertEqual(self.widget.sprite, None)
        self.widget.sprite = "files/sprite1.png"
        self.assertEqual(self.widget.sprite, "files/sprite1.png")

    def test_size(self):
        self.assertEqual(self.widget.size, Vec2(100, 40))
        self.widget.size = Vec2(100, 50)
        self.assertEqual(self.widget.size, Vec2(100, 50))

    def test_command(self):
        self.assertEqual(self.widget.command, None)
        self.widget.command = self.command
        self.assertEqual(self.widget.command, self.command)

    def command(self, btn, click):
        pass


class EntryTests(WidgetTests):
    def setUp(self):
        super(EntryTests, self).setUp()
        self.widget = Entry(Vec2(10, 10))

    def test_text(self):
        self.assertEqual(self.widget.text, "")
        self.widget.text = "test"
        self.assertEqual(self.widget.text, "test")

    def test_width(self):
        self.assertEqual(self.widget.width, 200)
        self.widget.width = 400
        self.assertEqual(self.widget.width, 400)

    def test_color(self):
        self.assertEqual(self.widget.label.color, Colors.BLACK.value)
        self.widget.label.color = Colors.GREEN.value
        self.assertEqual(self.widget.label.color, Colors.GREEN.value)

    def test_font(self):
        self.assertEqual(self.widget.label.font, Font())
        self.widget.label.font = Font(size=20)
        self.assertEqual(self.widget.label.font, Font(size=20))

