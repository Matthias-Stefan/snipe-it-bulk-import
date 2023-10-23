__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.interface_controller import IController
from src.model.settings import Settings
from src.view.tabs import SettingsTab


class SettingsController(IController):
    def __init__(self):
        self._model = Settings()
        self._view = SettingsTab(controller=self, model=self._model)

    def execute(self, **kwargs):
        self.progress_events.reset()
        # ...
        self.progress_events.advance()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model
