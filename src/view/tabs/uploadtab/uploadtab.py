__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.view.filedialog import FileDialog

import os

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty
from pathlib import Path


class UploadTab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super(UploadTab, self).__init__(**kwargs)
        self.title = "Upload"
        self.icon = "upload"
        self._filepath = None

    def on_upload(self):
        """Initiates the upload process.

        :rtype: None
        """
        x = 5
        return

    def open_filechooser(self):
        """Opens the file chooser dialog.

        :rtype: None
        """
        file_dialog = FileDialog(self.filename_callback)
        file_dialog.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a file path.

        :param filepath:
        :type filepath: pathlib.Path
        :rtype: None
        """
        self._filepath = filepath
        self.ids.tf_file.text = str(self._filepath)

    @property
    def filepath(self):
        """The path or filename of the new CSV to be created.

        :type: pathlib.Path
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        path = Path(value)
        if os.path.exists(path.parent.absolute()):
            self._filepath = path


