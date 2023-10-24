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
        self._settings_controller: IController = SettingsController(self)
        self._create_asset_controller: IController = CreateAssetController(self)
        self._checkout_controller: IController = CheckoutController(self)
        self._upload_controller: IController = UploadController(self)

        self._main_view = MainView(self._create_asset_controller.view,
                                   self._checkout_controller.view,
                                   self._upload_controller.view,
                                   self._settings_controller.view,
                                   controller=self)

        self._settings_controller.progress_events.reset += self._main_view.reset_progress
        self._settings_controller.progress_events.advance += self._main_view.advance_progress

        self._create_asset_controller.progress_events.reset += self._main_view.reset_progress
        self._create_asset_controller.progress_events.advance += self._main_view.advance_progress

        self._checkout_controller.progress_events.reset += self._main_view.reset_progress
        self._checkout_controller.progress_events.advance += self._main_view.advance_progress

        self._upload_controller.progress_events.reset += self._main_view.reset_progress
        self._upload_controller.progress_events.advance += self._main_view.advance_progress



    def execute(self, **kwargs):
        return

    @property
    def view(self):
        return self._main_view

    @property
    def model(self):
        return

    def get_settings_controller(self) -> SettingsController:
        return cast(SettingsController, self._settings_controller)

