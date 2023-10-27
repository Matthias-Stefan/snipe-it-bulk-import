__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals
from src.model import IModel, ModelProperties
from src.view.file_browser import FileBrowser

import os

from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class CheckoutTab(MDFloatLayout, MDTabsBase):
    """Represents a composition of MDFloatLayout and MDTabsBase.
    Generating the Asset Checkout CSV includes options for automatically opening the file in Excel. When auto-upload is
    enabled, the application will wait until Excel is closed before proceeding with an automatic upload.

    :param controller: The controller instance.
    :type controller: src.controller.tab_controller.checkout_controller.CheckoutController
    :param model: The model instance used for data management.
    :type model: src.model.interface_model.IModel
    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    def __init__(self, controller, model: IModel, **kwargs):
        super(CheckoutTab, self).__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Checkout Template"
        self.icon = "source-branch-check"

    def on_template_create(self):
        """Initiates the creation process.

        :rtype: None
        """
        self.controller.execute()

    def open_filebrowser(self):
        """Opens the file browser.

        :rtype: None
        """
        file_browser = FileBrowser(self.filename_callback)
        file_browser.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a filepath.

        :param filepath:
        :type filepath: pathlib.Path
        :rtype: None
        """
        self.set_filepath(str(filepath))
        self.ids.tf_file.text = str(filepath)

    def set_filepath(self, value: str):
        """Sets the selected file's path in the controller.

        :param value: The file's path.
        :type value: str
        :rtype: None
        """
        self.controller.filepath = value

    def set_autostart(self, value: bool):
        """Sets the autostart option in the controller.

        :param value: The autostart option.
        :type value: bool
        :rtype: None
        """
        self.controller.autostart = value

    def set_auto_upload(self, value: bool):
        """Sets the auto-upload option in the controller.

        :param value: The auto-upload option.
        :type value: bool
        :rtype: None
        """
        self.controller.auto_upload = value

    def on_model_changed_callback(self, model_property: ModelProperties, value):
        """Listens for model property changes.

        :param model_property: Enum for specifying the receiving property
        :type model_property: src.model.interface.ModelProperties
        :param value: The value of the change
        :type value: any
        :return: None
        """
        if model_property == ModelProperties.FILEPATH:
            self.ids.tf_file.text = value


Builder.load_file(os.path.join(Globals.get_checkout_tab_package(), "checkout_tab.kv"))
