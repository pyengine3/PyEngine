from pyengine.Network import *
import unittest


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.nw = NetworkManager()
        self.nw.create_client("localhost", 22112, self.callback)

    def test_send(self):
        self.nw.client.send(Packet("TOALL", 0, "Ceci est un test"))

    def callback(self, type_, author, message):
        self.assertEqual(type_, "TOALL")
        self.assertEqual(author, 0)
        self.assertEqual(message, "Ceci est un test")
        self.nw.stop_client()
        self.nw.stop_server()
