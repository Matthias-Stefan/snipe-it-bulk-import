__author__ = "Matthias Stefan"
__version__ = "0.1.0"


import abc


class ITemplate(abc.ABC):
    @abc.abstractmethod
    def __init__(self, options):
        pass
