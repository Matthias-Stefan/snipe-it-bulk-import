__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.utility import ProgressEvents

import abc

from functools import partial
from kivy.clock import Clock


class IController(abc.ABC):
    """Initialize an instance of the IController class.

    This is an abstract base class for application controllers. It defines methods for initialization, execution,
    and progress management.

    :param parent: The parent controller or component.
    :type parent: src.controller.IController
    """
    @abc.abstractmethod
    def __init__(self, parent=None):
        self.parent: IController = parent
        self.progress_events = ProgressEvents()

    @abc.abstractmethod
    def post_init(self):
        """Perform any post-initialization tasks, if necessary.

        :rtype: None
        """
        pass

    @abc.abstractmethod
    def execute(self, **kwargs):
        """Execute any specific actions, if needed.

        :param kwargs: Additional keyword arguments for execution.
        :type kwargs: dict
        :rtype: None
        """
        pass

    @property
    @abc.abstractmethod
    def view(self):
        """Get the associated view for this controller.

        :rtype: kivymd.uix.floatlayout.MDFloatLayout, kivymd.uix.tab.MDTabsBase
        """
        pass

    @property
    @abc.abstractmethod
    def model(self):
        """Get the associated model for this controller.

        :rtype: src.model.interface_model.IModel
        """
        pass

    def progress_reset(self, timeout=0):
        """Reset progress events to their initial state.

        :param timeout: Delay in seconds before resetting progress events (default is 0).
        :type timeout: float
        :rtype: None
        """
        Clock.schedule_once(self.progress_events.reset, timeout=timeout)

    def progress_advance(self, amount: int, info: str, state: bool = True, timeout=0):
        """Advance progress by a specified amount and update progress information.

        :param amount: The amount by which to advance the progress.
        :type amount: int
        :param info: Additional information about the progress.
        :type info: str
        :param state: The state of the progress (default is True).
        :type state: bool
        :param timeout: Delay in seconds before advancing progress (default is 0).
        :type timeout: float
        :rtype: None
        """
        Clock.schedule_once(partial(self.progress_events.advance, amount, info, state), timeout=timeout)

