from pyengine import Window, World, Entity
from pyengine.Systems import UISystem, EntitySystem, CameraSystem
from pyengine.Components import PositionComponent, TextComponent, SpriteComponent
from pyengine.Widgets import Label, Button
from pyengine.Utils import Colors, Font, Vec2

import pygame


class Menu:
    def __init__(self):
        self.window = Window(300, 200, Colors.WHITE.value)
        self.window.title = "Menu"

        self.gameworld = World(self.window)
        self.menuworld = World(self.window)

        self.labeljeu = Label(Vec2(10, 10), "JEU", Colors.BLACK.value, Font("arial", 18), Colors.GREEN.value)
        self.buttonzoom = Button(Vec2(150, 10), "Zoom", self.zoom)
        self.button1jeu = Button(Vec2(10, 50), "Retour", self.menu)
        self.button2jeu = Button(Vec2(150, 50), "Quitter", self.quitter)
        self.ejeu = Entity()
        self.ejeu.add_component(PositionComponent(Vec2(100, 100)))
        self.ejeu.add_component(SpriteComponent("images/sprite0.png"))

        self.uisystemjeu = self.gameworld.get_system(UISystem)
        self.gameworld.get_system(EntitySystem).add_entity(self.ejeu)
        self.uisystemjeu.add_widget(self.labeljeu)
        self.uisystemjeu.add_widget(self.buttonzoom)
        self.uisystemjeu.add_widget(self.button1jeu)
        self.uisystemjeu.add_widget(self.button2jeu)

        self.labelmenu = Entity()
        self.labelmenu.add_component(PositionComponent(Vec2(10, 10)))
        textlmenu = self.labelmenu.add_component(TextComponent("MENU", Colors.BLACK.value, Font("arial", 18, True),
                                                               Colors.GREEN.value))
        print(textlmenu.rendered_size)
        self.button1menu = Button(Vec2(10, 50), "Jouer", self.jouer)
        self.button2menu = Button(Vec2(150, 50), "Quitter", self.quitter)

        self.uisystemmenu = self.menuworld.get_system(UISystem)
        self.menuworld.get_system(EntitySystem).add_entity(self.labelmenu)
        self.uisystemmenu.add_widget(self.button1menu)
        self.uisystemmenu.add_widget(self.button2menu)
        self.uisystemmenu.add_widget(self.buttonzoom)

        self.window.world = self.menuworld
        self.window.run()

    def menu(self, widget, button):
        self.window.world = self.menuworld

    def zoom(self, widget, button):
        if self.window.world.get_system(CameraSystem).zoom == 1:
            self.window.world.get_system(CameraSystem).zoom = 2
        else:
            self.window.world.get_system(CameraSystem).zoom = 1

    # Fonction allant sur le jeu
    def jouer(self, widget, button):
        self.window.world = self.gameworld

    def quitter(self, widget, button):
        self.window.stop()


# Lance le menu
Menu()
