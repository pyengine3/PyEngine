import threading
import socket


class ReseauClient(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.connected = True

    def run(self):
        while self.connected:
            try:
                r = self.client.s.recv(9999999).decode()
                self.client.recieve(r)
            except ConnectionResetError:
                self.connected = False
            except ConnectionAbortedError:
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

    def recieve(self, message):
        self.callback(message)

    def send(self, message):
        self.s.send(str.encode(str(message)))


