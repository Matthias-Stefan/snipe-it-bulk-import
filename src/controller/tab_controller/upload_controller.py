__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import IController
from src.view.tabs import UploadTab


class UploadController(IController):
    def __init__(self, parent=None):
        super(UploadController, self).__init__(parent)
        self._view = UploadTab(controller=self)

    def post_init(self):
        return

    def execute(self, **kwargs):
        pass

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return
