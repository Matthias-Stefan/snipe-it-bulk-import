__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.utility import ProgressEvents

import abc


class IController(abc.ABC):
    @abc.abstractmethod
    def __init__(self, parent=None):
        self.parent: IController = parent
        self.progress_events = ProgressEvents()

    @abc.abstractmethod
    def post_init(self):
        pass

    @abc.abstractmethod
    def execute(self, **kwargs):
        pass

    @property
    @abc.abstractmethod
    def view(self):
        pass

    @property
    @abc.abstractmethod
    def model(self):
        pass
