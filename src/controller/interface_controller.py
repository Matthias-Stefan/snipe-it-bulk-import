__author__ = "Matthias Stefan"
__version__ = "0.1.0"

import abc

from events.events import Events


class ProgressEvents(Events):
    __events__ = ('advance', 'reset')


class IController(abc.ABC):
    progress_events = ProgressEvents()

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
