__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.model import IModel, ModelProperties


class CreateAsset(IModel):
    """Initialize an instance of the CreateAsset class.

    This class represents the parameters for creating an asset in Snipe-IT, including the model, quantity,
    status label, filepath for the CSV file, and options for autostart and auto-upload.

    :rtype: None
    """
    def __init__(self):
        self._model = ""
        self._quantity = 0
        self._status_label = ""
        self._filepath = ""
        self._autostart = False
        self._auto_upload = False

    @property
    def model(self):
        """The Snipe-IT model for asset creation.

        :type: str
        """
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, str) and value != self._model:
            self._model = value
            self.model_events.on_changed(ModelProperties.MODEL, self._model)

    @property
    def quantity(self):
        """The quantity of assets to create.

        :type: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value != self._quantity:
            self._quantity = value
            self.model_events.on_changed(ModelProperties.QUANTITY, self._quantity)

    @property
    def status_label(self):
        """The status label for the created assets.

        :type: str
        """
        return self._status_label

    @status_label.setter
    def status_label(self, value):
        if isinstance(value, str) and value != self._status_label:
            self._status_label = value
            self.model_events.on_changed(ModelProperties.STATUS_LABEL, self._status_label)

    @property
    def filepath(self):
        """Filepath for the CSV file that will be created.

        :type: str
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if isinstance(value, str) and value != self._filepath:
            self._filepath = value
            self.model_events.on_changed(ModelProperties.FILEPATH, self._filepath)

    @property
    def autostart(self):
        """The option to automatically invoke Excel for the created CSV file.

        :type: bool
        """
        return self._autostart

    @autostart.setter
    def autostart(self, value):
        if isinstance(value, bool) and value != self._autostart:
            self._autostart = value
            self.model_events.on_changed(ModelProperties.AUTOSTART, self._autostart)

    @property
    def auto_upload(self):
        """The option to automatically upload the CSV file.

        :type: bool
        """
        return self._auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        if isinstance(value, bool) and value != self._auto_upload:
            self._auto_upload = value
            self.model_events.on_changed(ModelProperties.AUTO_UPLOAD, self._auto_upload)
