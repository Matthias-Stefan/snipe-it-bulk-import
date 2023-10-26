__author__ = "Matthias Stefan"
__version__ = "1.0.0"


class Singleton:
    def __init__(self, class_):
        self._class = class_
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._class(*args, **kwargs)
        return self._instance
