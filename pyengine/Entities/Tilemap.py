from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, TextComponent
from pyengine.Utils import Vec2, loggers
from pyengine.Entities import Entity

import json
from xml.etree import ElementTree

__all__ = ["Tilemap"]


class Tilemap(Entity):
    def __init__(self, pos, file, scale=1):
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

        self.height = datas["height"]
        self.width = datas["width"]
        self.tileheight = datas["tileheight"]
        self.tilewidth = datas["tilewidth"]

        tileset = ElementTree.parse(self.folder+datas["tilesets"][0]["source"])
        idtiles = {}
        for tile in tileset.getroot():
            if tile.tag == 'tile':
                idtiles[tile.attrib["id"]] = tile[0].attrib["source"]

        self.tiles = [self.create_tile(datas, idtiles, pos, x, y)
                      for y in range(self.height) for x in range(self.width)]
        self.tiles = [x for x in self.tiles if x is not None]

        self.scale = scale

    def create_tile(self, datas, idtiles, pos, x, y):
        if datas["layers"][0]["data"][y*self.width+x] - 1 != -1:
            offset = Vec2(x * self.tilewidth, y * self.tileheight)
            idtile = str(datas["layers"][0]["data"][y*self.width+x]-1)
            tilesetfolder = "/".join(datas["tilesets"][0]["source"].split("/")[:-1])+"/"
            return Tile(pos, offset, self.folder + tilesetfolder + idtiles[idtile], [x, y], self.tileheight)

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val):
        for i in self.tiles:
            i.get_component(SpriteComponent).scale = val
            i.get_component(PositionComponent).offset = Vec2(
                i.pos_in_grid[0] * self.tilewidth * val,
                i.pos_in_grid[1] * self.tileheight * val + (self.tileheight - i.image.get_height())
            )
        self.__scale = val

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
    def __init__(self, pos, offset, sprite, pos_in_grid, tileheight):
        super(Tile, self).__init__()

        self.pos_in_grid = pos_in_grid
        poscomp = self.add_component(PositionComponent(pos, offset))
        self.add_component(SpriteComponent(sprite))
        poscomp.offset = Vec2(
            offset.x,
            offset.y + (tileheight - self.image.get_height())
        )
        self.add_component(PhysicsComponent(False))
