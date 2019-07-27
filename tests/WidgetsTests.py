import unittest
from pyengine.Widgets import *
from pyengine.Utils import Vec2, Color, Font, Colors
from pyengine.Systems import UISystem

import pygame

# UTILITIES CLASS FOR TESTS #


class FakeWorld:
    def __init__(self):
        pass


# TESTS #


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


class MultilineLabelTests(WidgetTests):
    def setUp(self):
        super(MultilineLabelTests, self).setUp()
        self.system = UISystem(FakeWorld())
        self.widget = MultilineLabel(Vec2(10, 10), "test")
        self.system.add_widget(self.widget)

    def test_text(self):
        self.assertEqual(self.widget.text, "test")
        self.assertEqual(len(self.widget.labels), 1)
        self.assertEqual(self.widget.labels[0].text, "test")
        self.widget.text = "OUI\ntest"
        self.assertEqual(self.widget.text, "OUI\ntest")
        self.assertEqual(len(self.widget.labels), 2)
        self.assertEqual(self.widget.labels[0].text, "OUI")
        self.assertEqual(self.widget.labels[1].text, "test")

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


class AnimatedImageTests(WidgetTests):
    def setUp(self):
        super(AnimatedImageTests, self).setUp()
        self.widget = AnimatedImage(Vec2(10, 10), ["files/sprite0.png", "files/sprite1.png"], 1)

    def test_sprites(self):
        self.assertEqual(self.widget.sprites, ["files/sprite0.png", "files/sprite1.png"])
        self.widget.sprites = ["files/sprite0.png"]
        self.assertEqual(self.widget.sprites, ["files/sprite0.png"])

    def test_size(self):
        self.assertEqual(self.widget.size,
                         Vec2(self.widget.image.get_rect().width, self.widget.image.get_rect().height))
        self.widget.size = Vec2(10, 10)
        self.assertEqual(Vec2(self.widget.image.get_rect().width, self.widget.image.get_rect().height), Vec2(10, 10))

    def test_animation(self):
        self.assertEqual(self.widget.sprite, "files/sprite0.png")
        self.widget.update()
        self.assertEqual(self.widget.sprite, "files/sprite1.png")
        self.widget.update()
        self.assertEqual(self.widget.sprite, "files/sprite0.png")
        self.widget.update()
        self.assertEqual(self.widget.sprite, "files/sprite1.png")


class CheckboxTests(WidgetTests):
    def setUp(self):
        super(CheckboxTests, self).setUp()
        self.widget = Checkbox(Vec2(10, 10), "test")

    def test_text(self):
        self.assertEqual(self.widget.label.text, "test")
        self.widget.label.text = "OUI"
        self.assertEqual(self.widget.label.text, "OUI")

    def test_scale(self):
        self.assertEqual(self.widget.scale, 1)
        self.widget.scale = 2
        self.assertEqual(self.widget.scale, 2)

    def test_checked(self):
        self.assertFalse(self.widget.checked)
        self.widget.checked = True
        self.assertTrue(self.widget.checked)


class ProgressBarTests(WidgetTests):
    def setUp(self):
        super(ProgressBarTests, self).setUp()
        self.widget = ProgressBar(Vec2(10, 10))

    def test_value(self):
        self.assertEqual(self.widget.value, 0)
        self.widget.value = 2
        self.assertEqual(self.widget.value, 2)

    def test_size(self):
        self.assertEqual(self.widget.size, Vec2(150, 10))
        self.widget.size = Vec2(300, 20)
        self.assertEqual(self.widget.size, Vec2(300, 20))

    def test_sprites(self):
        self.assertIsNone(self.widget.sprites)
        self.widget.sprites = ["files/sprite0.png", "files/sprite1.png"]
        self.assertEqual(self.widget.sprites, ["files/sprite0.png", "files/sprite1.png"])


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

    def command(self):
        pass


class SelectorTests(WidgetTests):
    def setUp(self):
        super(SelectorTests, self).setUp()
        self.widget = Selector(Vec2(10, 10), ["Michel", "Mamadou"])

    def test_get(self):
        self.assertEqual(self.widget.get(), "Michel")
        self.widget.next()
        self.assertEqual(self.widget.get(), "Mamadou")
        self.widget.next()
        self.assertEqual(self.widget.get(), "Michel")
        self.widget.precedent()
        self.assertEqual(self.widget.get(), "Mamadou")
        self.widget.precedent()
        self.assertEqual(self.widget.get(), "Michel")

    def test_strings(self):
        self.assertEqual(self.widget.strings, ["Michel", "Mamadou"])
        self.assertEqual(self.widget.get(), "Michel")
        self.widget.strings = ["Ou", "Pas"]
        self.assertEqual(self.widget.strings, ["Ou", "Pas"])
        self.assertEqual(self.widget.get(), "Ou")
        with self.assertRaises(ValueError):
            self.widget.strings = []


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
        self.assertEqual(self.widget.color, Colors.BLACK.value)
        self.widget.color = Colors.GREEN.value
        self.assertEqual(self.widget.color, Colors.GREEN.value)

    def test_font(self):
        self.assertEqual(self.widget.font, Font())
        self.widget.font = Font(size=20)
        self.assertEqual(self.widget.font, Font(size=20))


class ConsoleTests(WidgetTests):
    def setUp(self):
        super(ConsoleTests, self).setUp()
        self.widget = Console(None, Vec2(10, -10))  # Console add +20 to her y pos for the response label

    def test_commands(self):
        from pyengine.Widgets.Console import print_command
        self.assertEqual(self.widget.commands["print"], print_command)
        self.widget.add_command("test", self.setUp)
        self.assertEqual(self.widget.commands["test"], self.setUp)
        self.widget.delete_command("test")
        with self.assertRaises(KeyError):
            print(self.widget.commands["test"])
        with self.assertRaises(ValueError):
            self.widget.delete_command("test")

    def test_reply(self):
        self.assertEqual(self.widget.retour.text, ">")
        self.widget.reply()
        self.assertEqual(self.widget.retour.text, "> ")
        self.widget.reply("OUI")
        self.assertEqual(self.widget.retour.text, "> OUI")
