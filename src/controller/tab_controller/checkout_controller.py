__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.interface_controller import IController


class CheckoutController(IController):
    def execute(self, **kwargs):
        pass

    @property
    def view(self):
        pass


