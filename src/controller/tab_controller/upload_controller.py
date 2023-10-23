__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.interface_controller import IController
from src.view.tabs import UploadTab


class UploadController(IController):
    def __init__(self):
        self._view = UploadTab(controller=self)

    def execute(self, **kwargs):
        pass

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return
