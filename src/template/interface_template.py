__author__ = "Matthias Stefan"
__version__ = "0.1.0"


import abc
import pathlib


class ITemplate(abc.ABC):
    @abc.abstractmethod
    def create(self) -> pathlib.Path:
        pass
