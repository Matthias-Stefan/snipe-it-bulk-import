__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from globals import Globals
from src.model import IModel, ModelProperties
from src.view.file_browser import FileBrowser

import os

from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class UploadTab(MDFloatLayout, MDTabsBase):
    """Upload previously created template CSV files here.

    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    def __init__(self, controller, model: IModel, **kwargs):
        super(UploadTab, self).__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Upload"
        self.icon = "upload"

    def on_upload(self):
        """Initiates the upload process.

        :rtype: None
        """
        self.controller.execute()

    def open_filebrowser(self):
        """Opens the file chooser dialog.

        :rtype: None
        """
        file_dialog = FileBrowser(self.filename_callback)
        file_dialog.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a filepath.

        :param filepath:
        :type filepath: pathlib.Path
        :rtype: None
        """
        self.set_filepath(str(filepath))
        self.ids.tf_file.text = str(filepath)

    def set_filepath(self, value):
        self.controller.filepath = value

    def on_model_changed_callback(self, model_property: ModelProperties, value):
        if model_property == ModelProperties.OUTPUT_DIR:
            self.ids.tf_file.text = value


Builder.load_file(os.path.join(Globals.get_upload_tab_package(), "upload_tab.kv"))
