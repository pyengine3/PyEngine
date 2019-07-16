from pyengine.Network import *
import unittest


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.nw = NetworkManager()
        try:
            self.nw.create_client("localhost", 22112, self.callback)
        except ConnectionRefusedError:
            pass

    def test_send(self):
        if self.nw.client is None:
            self.skipTest("Client doesn't exist (Server musn't be launched)")
        else:
            self.nw.client.send(Packet("TOALL", 0, "Ceci est un test"))

    def callback(self, type_, author, message):
        if type_ == "TOALL":
            self.assertEqual(type_, "TOALL")
            self.assertEqual(message, "Ceci est un test")
            self.nw.stop_client()
            self.nw.stop_server()
