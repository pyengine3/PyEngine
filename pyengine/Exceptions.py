class NoWorldError(Exception):
    def __init__(self, text):
        super(NoWorldError, self).__init__(text)


class WrongComponentError(Exception):
    def __init__(self, text):
        super(WrongComponentError, self).__init__(text)


class NoComponentError(Exception):
    def __init__(self, text):
        super(NoComponentError, self).__init__(text)


class NoSystemError(Exception):
    def __init__(self, text):
        super(NoSystemError, self).__init__(text)


class ComponentIntializedError(Exception):
    def __init__(self, text):
        super(ComponentIntializedError, self).__init__(text)


class CompatibilityError(Exception):
    def __init__(self, text):
        super(CompatibilityError, self).__init__(text)

