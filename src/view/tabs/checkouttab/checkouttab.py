__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.view.filebrowser import FileBrowser

import os

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class CheckoutTab(MDFloatLayout, MDTabsBase):
    """Generating the Asset Checkout CSV includes options for automatically opening the file in Excel. In the event of
    auto-upload, the application will pause until Excel is closed, at which point it will proceed with an automatic
    upload.

    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    def __init__(self, **kwargs):
        super(CheckoutTab, self).__init__(**kwargs)
        self.title = "Checkout Template"
        self.icon = "source-branch-check"
        self._filepath = None
        self._autostart = False
        self._auto_upload = False

    def on_template_create(self):
        """Initiates the creation process.

        :rtype: None
        """
        x = 5

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

    @property
    def autostart(self):
        """Determine if Excel should be automatically invoked.

        :type: bool
        """
        return self._autostart

    @autostart.setter
    def autostart(self, value):
        self._autostart = value

    @property
    def auto_upload(self):
        """Determine if CSV should be automatically uploaded.

        :type: bool
        """
        return self._auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        self._auto_upload = value

