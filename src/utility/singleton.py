__author__ = "Matthias Stefan"
__version__ = "1.0.0"


class Singleton:
    """A decorator class for implementing the Singleton design pattern.

    This decorator ensures that only one instance of a class is created, and subsequent calls to the decorated class
    return the same instance.

    :param class_: The class to be decorated as a Singleton.
    :type class_: class
    """
    def __init__(self, class_):
        self._class = class_
        self._instance = None

    def __call__(self, *args, **kwargs):
        """Creates or retrieves the Singleton instance of the class.

        If an instance does not exist, it creates one; otherwise, it returns the existing instance.

        :param args: Positional arguments to pass to the class constructor.
        :param kwargs: Keyword arguments to pass to the class constructor.
        :return: The Singleton instance of the class.
        """
        if self._instance is None:
            self._instance = self._class(*args, **kwargs)
        return self._instance
