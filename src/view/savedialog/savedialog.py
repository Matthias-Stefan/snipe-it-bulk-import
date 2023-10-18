"""savedialog.py


"""

__author__ = "Matthias Stefan"
__version__ = "0.0.1"

import os

from collections.abc import Callable
from kivy.properties import ObservableList
from kivy.uix.popup import Popup
from pathlib import Path


class SaveDialog(Popup):
    def __init__(self, callback: Callable[[Path], None], **kwargs):
        super(SaveDialog, self).__init__(**kwargs)
        self._path = ""
        self._filename = ""
        self._callback = callback

    def cancel(self):
        self.dismiss()

    def save(self):
        path = Path(self._path, self._filename)
        if os.path.exists(path.parent.absolute()):
            self._callback(path)
            self.dismiss()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self.ids.ti_path.text = self._path

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if isinstance(value, ObservableList):
            if len(value) > 0:
                self._filename = Path(value[0]).name
        elif isinstance(value, str):
            self._filename = value
        self.ids.ti_filename.text = self._filename