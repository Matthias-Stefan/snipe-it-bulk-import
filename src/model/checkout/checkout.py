__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.model import IModel, ModelProperties


class Checkout(IModel):
    def __init__(self):
        self._filepath = ""
        self._autostart = False
        self._auto_upload = False

    @property
    def filepath(self):
        """Filepath of the CSV to be uploaded.

        :type: pathlib.Path
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if isinstance(value, str) and value != self._filepath:
            self._filepath = value
            self.model_events.on_changed(ModelProperties.FILEPATH, self._filepath)

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
