__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.model import IModel, ModelProperties


class CreateAsset(IModel):
    def __init__(self):
        self._model = ""
        self._quantity = 0
        self._status_label = ""
        self._filepath = ""
        self._autostart = False
        self._auto_upload = False

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, str) and value != self._model:
            self._model = value
            self.model_events.on_changed(ModelProperties.MODEL, self._model)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value != self._quantity:
            self._quantity = value
            self.model_events.on_changed(ModelProperties.QUANTITY, self._quantity)

    @property
    def status_label(self):
        return self._status_label

    @status_label.setter
    def status_label(self, value):
        if isinstance(value, str) and value != self._status_label:
            self._status_label = value
            self.model_events.on_changed(ModelProperties.STATUS_LABEL, self._status_label)

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if isinstance(value, str) and value != self._filepath:
            self._filepath = value
            self.model_events.on_changed(ModelProperties.FILEPATH, self._filepath)

    @property
    def autostart(self):
        return self._autostart

    @autostart.setter
    def autostart(self, value):
        if isinstance(value, bool) and value != self._autostart:
            self._autostart = value
            self.model_events.on_changed(ModelProperties.AUTOSTART, self._autostart)

    @property
    def auto_upload(self):
        return self._auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        if isinstance(value, bool) and value != self._auto_upload:
            self._auto_upload = value
            self.model_events.on_changed(ModelProperties.AUTO_UPLOAD, self._auto_upload)
