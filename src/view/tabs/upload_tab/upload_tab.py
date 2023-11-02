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


class UploadTab(MDFloatLayout, MDTabsBase):
    """Represents a composition of MDFloatLayout and MDTabsBase.
    This view provides functionality to search and select a CSV file using src.view.file_browser.FileBrowser.

    :param controller: The controller instance.
    :type controller: src.controller.tab_controller.upload_controller.UploadController
    :param model: The model instance used for data management.
    :type model: src.model.interface_model.IModel
    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    def __init__(self, controller, model: IModel, **kwargs):
        super(UploadTab, self).__init__(**kwargs)
        self.controller = controller
        model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Upload"
        self.icon = "upload"

    def on_upload(self):
        """Initiates the upload process by executing the controller.

        :rtype: None
        """
        self.controller.execute()

    def open_filebrowser(self):
        """Opens the file browser to select a file.

        :rtype: None
        """
        file_browser = FileBrowser(self.filename_callback)
        file_browser.open()

    def filename_callback(self, filepath: Path):
        """Callback function to receive a filepath and update the view.

        :param filepath: The selected file's path.
        :type filepath: pathlib.Path
        :rtype: None
        """
        self.set_filepath(str(filepath))
        self.ids.tf_file.text = str(filepath)

    def set_filepath(self, value: str):
        """Sets the filepath in the controller.

        :param value: The filepath to set
        :rtype: str
        """
        self.controller.filepath = value

    def on_model_changed_callback(self, model_property: ModelProperties, value: any):
        """Callback function to handle changes in the model's properties.

        :param model_property: Enum for specifying the receiving property.
        :type model_property: src.model.interface_model.ModelProperties
        :param value: The new value of the property.
        :type value: any
        :rtype: None
        """
        if model_property == ModelProperties.FILEPATH:
            self.ids.tf_file.text = value


Builder.load_file(os.path.join(Globals.get_upload_tab_package(), "upload_tab.kv"))
