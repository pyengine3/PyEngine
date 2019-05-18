import pygame
from pyengine.Exceptions import NoObjectError
from pyengine.Components import PositionComponent, SpriteComponent, TextComponent, ControlComponent
from pyengine.Entity import Entity

__all__ = ["EntitySystem"]


class EntitySystem:
    def __init__(self, state):
        self.state = state
        self.entities = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()

    def get_entity(self, identity):
        for i in self.entities:
            if i.identity == identity:
                return i

    def add_entity(self, entity):
        if not isinstance(entity, Entity):
            raise TypeError("Argument is not type of "+str(Entity)+" but "+str(type(entity))+".")
        if not entity.has_component(PositionComponent):
            raise NoObjectError("Entity must have PositionComponent to be add in a world.")
        if not entity.has_component(SpriteComponent) and not entity.has_component(TextComponent):
            raise NoObjectError("Entity must have SpriteComponent or TextComponent to be add in a world.")
        entity.set_id(len(self.entities))
        entity.set_system(self)
        if entity.has_component(SpriteComponent):
            self.entities.add(entity)
        else:
            self.texts.add(entity)
        return entity

    def update(self):
        for i in self.entities:
            i.update()

    def keypress(self, evt):
        for i in self.entities:
            if i.has_component(ControlComponent):
                i.get_component(ControlComponent).keypress(evt)

    def keyup(self, evt):
        for i in self.entities:
            if i.has_component(ControlComponent):
                i.get_component(ControlComponent).keyup(evt)

    def mousepress(self, evt):
        for i in self.entities:
            if i.has_component(ControlComponent):
                i.get_component(ControlComponent).mousepress(evt)

    def show(self, screen):
        self.entities.draw(screen)
        for i in self.texts:
            text = i.get_component(TextComponent)
            position = i.get_component(PositionComponent)
            screen.blit(text.render(), position.get_position())

    def show_debug(self, screen):
        for i in self.entities:
            render = self.state.window.debugfont.render("ID : "+str(i.id), 1, (255, 255, 0))
            screen.blit(render, (i.rect.x + i.rect.width / 2 - render.get_width()/2, i.rect.y - 20))
