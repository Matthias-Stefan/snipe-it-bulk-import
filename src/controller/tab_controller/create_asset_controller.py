__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.interface_controller import IController


class CreateAssetController(IController):
    def __init__(self):
        pass

    def execute(self, **kwargs):
        self.progress_events.reset()
        # ...
        self.progress_events.advance(5, "Hitler")

    @property
    def view(self):
        pass

