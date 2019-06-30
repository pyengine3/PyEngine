__all__ = ["Packet"]


class Packet:
    def __init__(self, type_: str = None, author: int = None, message: str = None):
        self.type_ = type_
        self.author = author
        self.message = message

    def to_send(self):
        return str.encode(str(self.type_)+"|"+str(self.author)+"|"+str(self.message))

    def from_recieve(self, recieve: bytearray):
        m = recieve.decode()
        if len(m.split("|", 2)) == 3:
            self.type_, self.author, self.message = m.split("|", 2)
            if self.author != "None":
                self.author = int(self.author)
            else:
                self.author = None
        return self
