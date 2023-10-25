__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.utility import ProgressEvents

import abc

from functools import partial
from kivy.clock import Clock


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

    def progress_reset(self, timeout=0):
        Clock.schedule_once(self.progress_events.reset, timeout=timeout)

    def progress_advance(self, amount: int, info: str, state: bool = True, timeout=0):
        Clock.schedule_once(partial(self.progress_events.advance, amount, info, state), timeout=timeout)

