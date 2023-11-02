__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.model import IModel, ModelProperties


class Settings(IModel):
    """Initialize an instance of the Settings class.

    This class represents the settings for the application, allowing the specification of URL, token, output directory,
    Excel path, and logs directory.

    :rtype: None
    """
    def __init__(self):
        self._url = ""
        self._token = ""
        self._output_dir = ""
        self._excel_path = ""
        self._logs_dir = ""

    @property
    def url(self):
        """URL for API requests.

        :type: str
        """
        return self._url

    @url.setter
    def url(self, value):
        if isinstance(value, str) and value != self._url:
            self._url = value
            self.model_events.on_changed(ModelProperties.URL, self._url)

    @property
    def token(self):
        """API token for authentication.

        :type: str
        """
        return self._token

    @token.setter
    def token(self, value):
        if isinstance(value, str) and value != self._token:
            self._token = value
            self.model_events.on_changed(ModelProperties.TOKEN, self._token)

    @property
    def output_dir(self):
        """The default output directory for CSV files.

        :type: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value):
        if isinstance(value, str) and value != self._output_dir:
            self._output_dir = value
            self.model_events.on_changed(ModelProperties.OUTPUT_DIR, self._output_dir)

    @property
    def excel_path(self):
        """The default Excel file path for automatic opening.

        :type: str
        """
        return self._excel_path

    @excel_path.setter
    def excel_path(self, value):
        if isinstance(value, str) and value != self._excel_path:
            self._excel_path = value
            self.model_events.on_changed(ModelProperties.EXCEL_PATH, self._excel_path)
