__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.model import IModel, ModelProperties


class Settings(IModel):
    def __init__(self):
        self._url = ""
        self._token = ""
        self._output_dir = ""
        self._excel_path = ""
        self._logs_dir = ""

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if isinstance(value, str) and value != self._url:
            self._url = value
            self.model_events.on_changed(ModelProperties.URL, self._url)

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        if isinstance(value, str) and value != self._token:
            self._token = value
            self.model_events.on_changed(ModelProperties.TOKEN, self._token)

    @property
    def output_dir(self):
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value):
        if isinstance(value, str) and value != self._output_dir:
            self._output_dir = value
            self.model_events.on_changed(ModelProperties.OUTPUT_DIR, self._output_dir)

    @property
    def excel_path(self):
        return self._excel_path

    @excel_path.setter
    def excel_path(self, value):
        if isinstance(value, str) and value != self._excel_path:
            self._excel_path = value
            self.model_events.on_changed(ModelProperties.EXCEL_PATH, self._excel_path)

    @property
    def logs_dir(self):
        return self._logs_dir

    @logs_dir.setter
    def logs_dir(self, value):
        if isinstance(value, str) and value != self._logs_dir:
            self._logs_dir = value
