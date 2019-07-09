from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, TextComponent
from pyengine.Utils import Vec2, loggers

import json
from xml.etree import ElementTree

__all__ = ["Tilemap"]


class Tilemap(Entity):
    def __init__(self, pos, file):
        super(Tilemap, self).__init__()

        self.folder = "/".join(file.split("/")[:-1])+"/"

        self.add_component(PositionComponent(pos))
        self.add_component(TextComponent(""))

        with open(file, "r") as f:
            datas = json.load(f)

        if datas["infinite"]:
            raise ValueError("PyEngine can't use infinite map")
        if len(datas["tilesets"]) > 1:
            loggers.get_logger("PyEngine").warning("Tilemap use only 1 tileset.")
        if len(datas["layers"]) > 1:
            loggers.get_logger("PyEngine").warning("Tilemap use only 1 layer.")

        height = datas["height"]
        width = datas["width"]
        tileheight = datas["tileheight"]
        tilewidth = datas["tilewidth"]

        tileset = ElementTree.parse(self.folder+datas["tilesets"][0]["source"])
        idtiles = {}
        for tile in tileset.getroot():
            if tile.tag == 'tile':
                idtiles[tile.attrib["id"]] = tile[0].attrib["source"]

        self.tiles = []
        for x in range(width):
            for y in range(height):
                if datas["layers"][0]["data"][y*width+x] - 1 != -1:
                    offset = Vec2(x * tilewidth, y * tileheight)
                    idtile = str(datas["layers"][0]["data"][y*width+x]-1)
                    self.tiles.append(Tile(pos, offset, self.folder+idtiles[idtile]))

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
        for i in self.tiles:
            self.attach_entity(i)
            system.add_entity(i)


class Tile(Entity):
    def __init__(self, pos, offset, sprite):
        super(Tile, self).__init__()

        self.add_component(PositionComponent(pos, offset))
        self.add_component(SpriteComponent(sprite))
        self.add_component(PhysicsComponent(False))
