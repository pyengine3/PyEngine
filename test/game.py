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

    def client_recieve(self, message):
        nb, message = message.split(": ", 1)
        pos = message.replace("(", "").replace(")", "").split(", ")
        if len(pos) == 2:
            try:
                pos = Vec2(int(pos[0]), int(pos[1]))
                if nb in self.entities:
                    self.entities[nb].move_to(pos)
                else:
                    self.entities[nb] = Character(pos)
                    self.esys.add_entity(self.entities[nb])
            except ValueError:
                pass


Game()
