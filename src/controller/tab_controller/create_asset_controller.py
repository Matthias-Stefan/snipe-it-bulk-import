__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.interface_controller import IController
from src.view.tabs import CreateAssetTab


class CreateAssetController(IController):
    def __init__(self):
        self._view = CreateAssetTab(controller=self)

    def execute(self, **kwargs):
        self.progress_events.reset()
        # ...
        self.progress_events.advance()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return
