__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import IController
from src.view.tabs import CheckoutTab


class CheckoutController(IController):
    def __init__(self, parent=None):
        super(CheckoutController, self).__init__(parent)
        self._view = CheckoutTab(controller=self)

    def execute(self, **kwargs):
        self.progress_events.reset()
        # ...
        self.progress_events.advance()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        pass


