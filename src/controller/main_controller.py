__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.tab_controller import CheckoutController, \
    CreateAssetController, \
    SettingsController, \
    UploadController
from src.controller import IController
from src.view import MainView

from typing import cast


class MainController(IController):
    def __init__(self):
        self._children: list[IController] = [SettingsController(self),
                                             CreateAssetController(self),
                                             CheckoutController(self),
                                             UploadController(self)]

        self._main_view = MainView(self._children[0].view,
                                   self._children[1].view,
                                   self._children[2].view,
                                   self._children[3].view,
                                   controller=self)

    def post_init(self):
        for controller in self._children:
            controller.progress_events.reset += self._main_view.reset_progress
            controller.progress_events.advance += self._main_view.advance_progress
            controller.post_init()

    def execute(self, **kwargs):
        return

    @property
    def view(self):
        return self._main_view

    @property
    def model(self):
        return

    def get_settings_controller(self) -> SettingsController:
        return cast(SettingsController, self._children[0])

    def get_create_asset_controller(self) -> CreateAssetController:
        return cast(CreateAssetController, self._children[1])

