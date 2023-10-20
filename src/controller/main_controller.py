__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller.tab_controller import CheckoutController, \
    CreateAssetController, \
    SettingsController, \
    UploadController
from src.controller.interface_controller import IController
from src.view import MainView


class MainController(IController):
    def __init__(self):
        self._view = MainView(controller=self)

        self._checkout_controller: IController = CheckoutController()

        self._create_asset_controller: IController = CreateAssetController()
        self._create_asset_controller.progress_events.reset += self._view.reset_progress
        self._create_asset_controller.progress_events.advance += self._view.advance_progress

        self._settings_controller: IController = SettingsController()
        self._upload_controller: IController = UploadController()

        self._create_asset_controller.execute()

    def execute(self, **kwargs):
        return

    @property
    def view(self):
        return self._view




