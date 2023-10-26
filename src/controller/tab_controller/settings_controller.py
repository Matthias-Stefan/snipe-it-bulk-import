__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals
from src.controller import IController
from src.model import Settings
from src.view.tabs import SettingsTab

import dotenv
import os
import sys

from datetime import datetime
from pathlib import Path


class SettingsController(IController):
    def __init__(self, parent=None):
        super(SettingsController, self).__init__(parent)
        self._dotenv_file = os.path.join(Globals.get_settings_package(), ".env")
        try:
            if len(dotenv.find_dotenv(self._dotenv_file)) > 0:
                self._config = dotenv.dotenv_values(self._dotenv_file)
        except IOError as error:
            print(error)
            sys.exit()

        self._model = Settings()
        self._view = SettingsTab(controller=self, model=self.model)

        self._model.url = self._config.get("url")
        self._model.token = self._config.get("token")
        self._model.output_dir = self._config.get("output_dir")
        self._model.excel_path = self._config.get("excel_path")
        self._model.logs_dir = self._config.get("logs_dir")

    def post_init(self):
        return

    def execute(self, **kwargs):
        return

    @staticmethod
    def create_folder(path: Path):
        if not os.path.exists(path):
            os.mkdir(path)
            return True
        return False

    def update_timestamp(self):
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        dotenv.set_key(self._dotenv_file, "timestamp", timestamp)

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    @property
    def url(self):
        return self.model.url

    @url.setter
    def url(self, value):
        self.model.url = value
        dotenv.set_key(self._dotenv_file, "url", self.model.url)
        self.update_timestamp()

    @property
    def token(self):
        return self.model.token

    @token.setter
    def token(self, value):
        self.model.token = value
        dotenv.set_key(self._dotenv_file, "token", value)
        self.update_timestamp()

    @property
    def output_dir(self):
        return self.model.output_dir

    @output_dir.setter
    def output_dir(self, value):
        self.progress_reset()
        if isinstance(value, str) and os.path.exists(os.path.dirname(value)):
            self.model.output_dir = value
            dotenv.set_key(self._dotenv_file, "output_dir", value)
            if self.create_folder(Path(value)):
                self.update_timestamp()
                self.progress_advance(100, f"Created output directory successfully: {value}")
            else:
                self.progress_advance(100, f"Set output directory successfully: {value}")
        else:
            self.progress_advance(100, f"Failed to create output directory: {value}", False)

    @property
    def excel_path(self):
        return self.model.excel_path

    @excel_path.setter
    def excel_path(self, value):
        self.progress_reset()
        if isinstance(value, str) and os.path.exists(value) and value.lower().endswith(".exe"):
            self.model.excel_path = value
            dotenv.set_key(self._dotenv_file, "excel_path", value)
            self.update_timestamp()
            self.progress_advance(100, f"Set excel path successfully: {value}")
        else:
            self.progress_advance(100, f"Failed to set excel path: {value}", False)

    @property
    def logs_dir(self):
        return self.model.logs_dir

    @logs_dir.setter
    def logs_dir(self, value):
        if isinstance(value, str) and os.path.exists(os.path.dirname(value)):
            self.model.logs_dir = value
            dotenv.set_key(self._dotenv_file, "logs_dir", value)
            self.update_timestamp()
