__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller.tab_controller import CheckoutController, \
    CreateAssetController, \
    SettingsController, \
    UploadController
from src.controller import IController
from src.manager.logger import Logger
from src.view import MainView

from typing import cast


class MainController(IController):
    """Initialize an instance of the MainController class.

    This class serves as the main controller for the application and manages sub-controllers for various tabs.

    :rtype: None
    """
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

    @Logger.log_function
    def post_init(self):
        """Perform any post-initialization tasks for the controllers.

        This method links progress events from sub-controllers to the main view and calls post_init for each sub-controller.

        :rtype: None
        """
        for controller in self._children:
            controller.progress_events.reset += self._main_view.reset_progress
            controller.progress_events.advance += self._main_view.advance_progress
            controller.post_init()

    def execute(self, **kwargs):
        """Execute the main controller's tasks.

        This method does not perform any specific task and returns immediately.

        :param kwargs: Additional keyword arguments for execution.
        :type kwargs: dict
        :rtype: None
        """
        return

    @property
    def view(self):
        """Get the associated view for this controller.

        :rtype: src.view.main_view.MainView
        """
        return self._main_view

    @property
    def model(self):
        """Get the associated model for this controller.

        :rtype: None
        """
        return

    def get_settings_controller(self) -> SettingsController:
        """Get the SettingsController sub-controller.

        :rtype: src.controller.tab_controller.settings_controller.SettingsController
        """
        return cast(SettingsController, self._children[0])

    def get_create_asset_controller(self) -> CreateAssetController:
        """Get the CreateAssetController sub-controller.

        :rtype: src.controller.tab_controller.create_asset_controller.CreateAssetController
        """
        return cast(CreateAssetController, self._children[1])

    def get_checkout_controller(self) -> CheckoutController:
        """Get the CheckoutController sub-controller.

        :rtype: src.controller.tab_controller.checkout_controller.CheckoutController
        """
        return cast(CheckoutController, self._children[2])

    def get_upload_controller(self) -> UploadController:
        """Get the UploadController sub-controller.

        :rtype: src.controller.tab_controller.upload_controller.UploadController
        """
        return cast(UploadController, self._children[3])
