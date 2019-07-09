import threading
import socket
from pyengine.Network.Packet import Packet


class ClientThread(threading.Thread):
    def __init__(self, server, clientsocket, nb):
        super(ClientThread, self).__init__()
        self.server = server
        self.clientsocket = clientsocket
        self.nb = nb
        self.connected = True

    def run(self):
        print("NEW CLIENT :", str(self.nb))
        while self.connected:
            try:
                r = self.clientsocket.recv(2048)
                r = Packet().from_recieve(r)
                r.author = self.nb
                self.server.recieve(r)
            except ConnectionAbortedError:
                self.connected = False
            except ConnectionResetError:
                self.connected = False
        self.server.clientquit(self.nb)


class Server(threading.Thread):
    def __init__(self, port):
        super(Server, self).__init__()
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpsock.bind(("localhost", port))
        self.nbclient = 0
        self.liste = {}

    def stop(self):
        for i in self.liste.values():
            i.connected = False
        self.tcpsock.close()

    def recieve(self, packet):
        if packet.message is not None and len(packet.message):
            self.sendall(packet)

    def clientquit(self, nb):
        print("END CLIENT :", str(nb))
        self.sendall(Packet("END", nb, ""))
        del self.liste[nb]

    def run(self):
        while True:
            self.tcpsock.listen(10)
            (clientsocket, (ip, port)) = self.tcpsock.accept()
            newthread = ClientThread(self, clientsocket, self.nbclient)
            self.liste[self.nbclient] = newthread
            self.sendall(Packet("NEW", self.nbclient, ""))
            self.nbclient += 1
            newthread.start()

    def sendto(self, nb, packet):
        try:
            self.liste[nb].clientsocket.send(packet.to_send())
        except KeyError:
            pass

    def sendall(self, packet):
        temp = self.liste.copy()
        for i in temp.values():
            if packet.author is None:
                i.clientsocket.send(packet.to_send())
            elif i != self.liste[packet.author] or packet.type_ == "TOALL":
                i.clientsocket.send(packet.to_send())
