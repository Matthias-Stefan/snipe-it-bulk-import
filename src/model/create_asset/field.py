__author__ = "Matthias Stefan"
__version__ = "0.1.0"


class Field:
    def __init__(self, name, value, meta):
        self.name = name
        self.value = value
        self.meta = meta

    def __eq__(self, other):
        return self.meta == type(other)
