from pyengine import Window, WindowCallbacks
from pyengine.Systems import EntitySystem
from pyengine.Utils import Colors, Vec2
from pyengine.Network import NetworkManager

from player import Player, Character


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(700, 600, Colors.WHITE.value)

        self.nw = NetworkManager()
        self.nw.create_client("localhost", 1211, self.client_recieve)

        e = Player(Vec2(100, 100), self.nw)
        self.esys = self.world.get_system(EntitySystem)
        self.esys.add_entity(e)

        self.entities = {}

        self.set_callback(WindowCallbacks.STOPWINDOW, self.stop_connexion)

        self.run()

    def stop_connexion(self):
        self.nw.stop_client()

    def client_recieve(self, type_, author, message):
        if type_ == "pos":
            pos = message.replace("(", "").replace(")", "").split(", ")
            if len(pos) == 2:
                try:
                    pos = Vec2(int(pos[0]), int(pos[1]))
                    if author in self.entities:
                        self.entities[author].move_to(pos)
                    else:
                        self.entities[author] = Character(pos)
                        self.esys.add_entity(self.entities[author])
                except ValueError:
                    pass
        elif type_ == "END":
            if author in self.entities:
                self.esys.remove_entity(self.entities[author])
                del self.entities[author]


Game()
