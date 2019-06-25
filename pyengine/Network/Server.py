import threading
import socket


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
                r = self.clientsocket.recv(2048).decode()
                self.server.recieve(self.nb, r)
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

    def recieve(self, nb, message):
        if len(message):
            self.sendall(message, nb)

    def clientquit(self, nb):
        print("FIN CLIENT :", str(nb))
        del self.liste[nb]

    def run(self):
        while True:
            self.tcpsock.listen(10)
            (clientsocket, (ip, port)) = self.tcpsock.accept()
            newthread = ClientThread(self, clientsocket, self.nbclient)
            self.liste[self.nbclient] = newthread
            self.nbclient += 1
            newthread.start()

    def sendto(self, nb, message):
        try:
            self.liste[nb].clientsocket.send(str.encode(message))
        except KeyError:
            pass

    def sendall(self, message, sender=None):
        temp = self.liste.copy()
        for i in temp.values():
            if sender is None:
                i.clientsocket.send(str.encode(message))
            elif i != self.liste[sender]:
                i.clientsocket.send(str.encode(str(sender)+": "+message))
