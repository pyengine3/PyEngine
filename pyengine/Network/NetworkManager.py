from pyengine.Network.Client import Client
from pyengine.Network.Server import Server

__all__ = ["NetworkManager"]


class NetworkManager:
    def __init__(self):
        self.client = None
        self.server = None

    def create_server(self, port):
        if self.server is None:
            self.server = Server(port)
            self.server.run()

    def stop_server(self):
        if self.server is not None:
            self.server.stop()
            self.server = None

    def stop_client(self):
        if self.client is not None:
            self.client.stop()
            self.client = None

    def create_client(self, ip, port, callback):
        if self.client is None:
            self.client = Client(ip, port, callback)
