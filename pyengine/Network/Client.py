import threading
import socket
from pyengine.Network.Packet import Packet


class ReseauClient(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.connected = True

    def run(self):
        while self.connected:
            try:
                r = self.client.s.recv(9999999)
                self.client.recieve(Packet().from_recieve(r))
            except ConnectionResetError:
                self.connected = False
            except ConnectionAbortedError:
                self.connected = False
            except OSError:
                self.connected = False


class Client:
    def __init__(self, ip, port, callback=None):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

        self.t = ReseauClient(self)
        self.t.start()

        self.callback = callback

    def stop(self):
        self.t.connected = False
        self.s.close()

    def recieve(self, packet):
        if self.callback is not None:
            self.callback(packet.type_, packet.author, packet.message)

    def send(self, packet: Packet):
        self.s.send(packet.to_send())



