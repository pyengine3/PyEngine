class NoObjectError(Exception):
    def __init__(self, text):
        super(NoObjectError, self).__init__(text)


class CompatibilityError(Exception):
    def __init__(self, text):
        super(CompatibilityError, self).__init__(text)

