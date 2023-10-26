__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import os

from collections.abc import Callable
from kivy.properties import ObservableList
from kivy.uix.popup import Popup
from pathlib import Path


class FileBrowser(Popup):
    """FileBrowser serves as a file dialog, offering a FileChooserListView for folder selection and filename
    definition. When the "save" button is pressed, the FileBrowser calls the provided callback function,
    passing the selected file path to the callee.

    :param callback: A callable function that accepts a Path object and returns None.
    :type callback: collections.abc.Callable
    :param kwargs: Additional keyword arguments to be passed to the Popup constructor.
    """
    def __init__(self, callback: Callable[[Path], None], **kwargs):
        super(FileBrowser, self).__init__(**kwargs)
        self._path = ""
        self._filename = ""
        self._callback = callback

    def cancel(self):
        """Dismisses the dialog.

        :rtype: None
        """
        self.dismiss()

    def save(self):
        """Generates the file path, checks its validity, and invokes the callback function to share the selected
        filename.

        :rtype: None
        """
        path = Path(self._path, self._filename)
        if os.path.exists(path.parent.absolute()):
            self._callback(path)
            self.dismiss()

    @property
    def path(self):
        """Property for retrieving the current path value.

        :type: str
        """
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self.ids.ti_path.text = self._path

    @property
    def filename(self):
        """Property for retrieving the current filename.

        :type: str
        """
        return self._filename

    @filename.setter
    def filename(self, value):
        if isinstance(value, ObservableList):
            if len(value) > 0:
                path = Path(value[0])
                self._filename = path.name
                self._path = str(path.parent)
                self.ids.ti_path.text = str(path.parent)
        elif isinstance(value, str):
            self._filename = value
        self.ids.ti_filename.text = self._filename
