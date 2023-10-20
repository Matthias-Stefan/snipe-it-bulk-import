__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.view.file_browser import FileBrowser

import os

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class UploadTab(MDFloatLayout, MDTabsBase):
    """Upload previously created template CSV files here.

    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

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
        self._filepath = filepath
        self.ids.tf_file.text = str(self._filepath)

    @property
    def filepath(self):
        """Filepath of the CSV to be uploaded.

        :type: pathlib.Path
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        path = Path(value)
        if os.path.exists(path.parent.absolute()):
            self._filepath = path


