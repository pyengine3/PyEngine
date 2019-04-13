import pygame
from pyengine.Entity import Entity
from pyengine.Components import ControlComponent, PositionComponent, SpriteComponent, TextComponent
from pyengine.Exceptions import NoComponentError

__all__ = ["World"]


class World:
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()
        self.window = None

    def set_window(self, window):
        self.window = window

    def get_entity(self, identity):
        for i in self.entities:
            if i.identity == identity:
                return i

    def add_entity(self, entity):
        if type(entity) != Entity:
            raise TypeError("Argument is not a Entity")
        if not entity.has_component(PositionComponent):
            raise NoComponentError("Entity must have PositionComponent to be add in a world.")
        if not entity.has_component(SpriteComponent) and not entity.has_component(TextComponent):
            raise NoComponentError("Entity must have SpriteComponent or TextComponent to be add in a world.")
        entity.set_id(len(self.entities))
        entity.set_world(self)
        if entity.has_component(SpriteComponent):
            self.entities.add(entity)
        else:
            self.texts.add(entity)

    def update(self):
        for i in self.entities:
            i.update()

    def keypress(self, key):
        for i in self.entities:
            if i.has_component(ControlComponent):
                i.get_component(ControlComponent).keypress(key)

    def show(self, screen):
        self.entities.draw(screen)
        for i in self.texts:
            text = i.get_component(TextComponent)
            position = i.get_component(PositionComponent)
            screen.blit(text.render(), position.get_position())

    def show_debug(self, screen):
        for i in self.entities:
            render = self.window.debugfont.render("ID : "+str(i.id), 1, (255, 255, 0))
            screen.blit(render, (i.rect.x + i.rect.width / 2 - render.get_width()/2, i.rect.y - 20))
