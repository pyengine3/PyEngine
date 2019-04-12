class NoWorld(Exception):
    def __init__(self, text):
        super(NoWorld, self).__init__(text)


class WrongComponent(Exception):
    def __init__(self, text):
        super(WrongComponent, self).__init__(text)


class NoComponent(Exception):
    def __init__(self, text):
        super(NoComponent, self).__init__(text)


class ComponentAlreadyIntialized(Exception):
    def __init__(self, text):
        super(ComponentAlreadyIntialized, self).__init__(text)
