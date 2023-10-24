__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from globals import Globals
from src.controller import IController
from src.model.settings import Settings
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

    def execute(self, **kwargs):
        return

    @staticmethod
    def validate_url(*arg) -> bool:
        return True

    @staticmethod
    def validate_token(*arg) -> bool:
        return True

    @staticmethod
    def validate_excel_path(*arg) -> bool:
        if isinstance(arg[0], str) and os.path.exists(arg[0]) and arg[0].lower().endswith(".exe"):
            return True
        return False

    @staticmethod
    def validate_output_dir(*arg) -> bool:
        if isinstance(arg[0], str) and os.path.exists(os.path.dirname(arg[0])):
            return True
        return False

    @staticmethod
    def validate_logs_dir(*arg) -> bool:
        if isinstance(arg, str) and os.path.exists(os.path.dirname(arg)):
            return True
        return False

    @staticmethod
    def create_folder(path: Path):
        if not os.path.exists(path):
            os.mkdir(path)

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
        self.progress_events.reset()
        self.progress_events.advance(0, f"Start creating url")
        if self.validate_url(value):
            self.model.url = value
            dotenv.set_key(self._dotenv_file, "url", self.model.url)
            self.update_timestamp()
            self.progress_events.advance(100, f"Created url successfully")
        else:
            self.progress_events.advance(100, f"Failed to create url", False)

    @property
    def token(self):
        return self.model.token

    @token.setter
    def token(self, value):
        self.progress_events.reset()
        self.progress_events.advance(0, f"Start creating token")
        if self.validate_token(value):
            self.model.token = value
            dotenv.set_key(self._dotenv_file, "token", value)
            self.update_timestamp()
            self.progress_events.advance(100, f"Created token successfully")
        else:
            self.progress_events.advance(100, f"Failed to create token", False)

    @property
    def output_dir(self):
        return self.model.output_dir

    @output_dir.setter
    def output_dir(self, value):
        self.progress_events.reset()
        self.progress_events.advance(0, f"Start creating output directory")
        if self.validate_output_dir(value):
            self.model.output_dir = value
            dotenv.set_key(self._dotenv_file, "output_dir", value)
            self.create_folder(value)
            self.update_timestamp()
            self.progress_events.advance(100, f"Created output directory successfully")
        else:
            self.progress_events.advance(100, f"Failed to create output directory", False)

    @property
    def excel_path(self):
        return self.model.excel_path

    @excel_path.setter
    def excel_path(self, value):
        self.progress_events.reset()
        self.progress_events.advance(0, f"Start setting excel path")
        if self.validate_excel_path(value):
            self.model.excel_path = value
            dotenv.set_key(self._dotenv_file, "excel_path", value)
            self.update_timestamp()
            self.progress_events.advance(100, f"Set excel path successfully")
        else:
            self.progress_events.advance(100, f"Failed to set excel path", False)

    @property
    def logs_dir(self):
        return self.model.logs_dir

    @logs_dir.setter
    def logs_dir(self, value):
        if self.validate_logs_dir(value):
            self.model.logs_dir = value
            dotenv.set_key(self._dotenv_file, "logs_dir", value)
            self.update_timestamp()
