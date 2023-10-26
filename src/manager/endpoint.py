__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from typing import Callable


class Endpoint:
    def __init__(self):
        self.value: str = ""
        self.callback: Callable = None
        self.payload: dict = {}

    def get_params(self):
        return self.value, self.payload
