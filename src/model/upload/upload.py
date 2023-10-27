__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import threading

from src.model import IModel, ModelProperties


class Upload(IModel):
    """Initialize an instance of the Upload class.

    This class represents the upload functionality and allows specifying the file path, autostart, and auto-upload
    settings.

    :rtype: None
    """
    def __init__(self):
        self._filepath = ""
        self._autostart = False
        self._auto_upload = False

    @property
    def filepath(self):
        """Filepath.

        :type: str
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if isinstance(value, str) and value != self._filepath:
            self._filepath = value
            if threading.current_thread().name == 'MainThread':
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
