__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from globals import Globals
from src.controller.interface_controller import IController
from src.model.settings import Settings
from src.view.tabs import SettingsTab

import dotenv
import os
import sys

from datetime import datetime


class SettingsController(IController):
    def __init__(self):
        self._dotenv_file = os.path.join(Globals.get_settings_package(), ".env")
        try:
            if len(dotenv.find_dotenv(self._dotenv_file)) > 0:
                self._config = dotenv.dotenv_values(self._dotenv_file)
        except IOError as error:
            print(error)
            sys.exit()

        self._model = Settings()
        self._view = SettingsTab(controller=self, model=self.model)
        self._model.url = self.url
        self._model.token = self.token
        self._model.output_dir = self.output_dir
        self._model.excel_path = self.excel_path
        self._model.logs_dir = self.logs_dir

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
        if isinstance(arg, str) and os.path.exists(arg) and arg.endswith(".exe"):
            return True
        return False

    @staticmethod
    def validate_output_dir(*arg) -> bool:
        if isinstance(arg, str) and os.path.exists(os.path.dirname(arg)):
            return True
        return False

    @staticmethod
    def validate_logs_dir(*arg) -> bool:
        if isinstance(arg, str) and os.path.exists(os.path.dirname(arg)):
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
        return self._config.get("url")

    @url.setter
    def url(self, value):
        self.progress_events.reset()
        self.progress_events.advance(0, f"Start creating {SettingsController.__name__}")
        if self.validate_url(value):
            self._model.url = value
            dotenv.set_key(self._dotenv_file, "url", self._model.url)
            self.update_timestamp()
            self.progress_events.advance(100, f"Created {SettingsController.__name__} successfully")

    @property
    def token(self):
        return self._config.get("token")

    @token.setter
    def token(self, value):
        if self.validate_token(value):
            self._model.token = value
            dotenv.set_key(self._dotenv_file, "token", value)
            self.update_timestamp()

    @property
    def output_dir(self):
        return self._config.get("output_dir")

    @output_dir.setter
    def output_dir(self, value):
        if self.validate_output_dir(value):
            self._model.output_dir = value
            dotenv.set_key(self._dotenv_file, "output_dir", value)
            self.update_timestamp()

    @property
    def excel_path(self):
        return self._config.get("excel_path")

    @excel_path.setter
    def excel_path(self, value):
        if self.validate_excel_path(value):
            self._model.excel_path = value
            dotenv.set_key(self._dotenv_file, "excel_path", value)
            self.update_timestamp()

    @property
    def logs_dir(self):
        return self._config.get("logs_dir")

    @logs_dir.setter
    def logs_dir(self, value):
        if self.validate_logs_dir(value):
            self._model.logs_dir = value
            dotenv.set_key(self._dotenv_file, "logs_dir", value)
            self.update_timestamp()
