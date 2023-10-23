__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from globals import Globals
from src.model import IModel

import dotenv
import os
import sys

from datetime import datetime


class Settings(IModel):
    def __init__(self):
        self._dotenv_file = os.path.join(Globals.get_settings_package(), ".env")
        try:
            if len(dotenv.find_dotenv(self._dotenv_file)) > 0:
                self._config = dotenv.dotenv_values(self._dotenv_file)
                self._validate_directory_paths()
        except IOError as error:
            print(error)
            sys.exit()

    def _validate_directory_paths(self):
        if not os.path.exists(self.output_dir):
            default_path = os.path.join(Globals.get_project_dir(), "output")
            if not os.path.exists(default_path):
                os.mkdir(default_path)
                self.output_dir = default_path
        if not os.path.exists(self.excel_path):
            self.excel_path = ''
        if not os.path.exists(self.logs_dir):
            default_path = os.path.join(Globals.get_project_dir(), "logs")
            if not os.path.exists(default_path):
                os.mkdir(default_path)
                self.logs_dir = default_path

    def update_timestamp(self):
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        dotenv.set_key(self._dotenv_file, "timestamp", timestamp)

    @property
    def url(self):
        return self._config.get("url")

    @url.setter
    def url(self, value):
        dotenv.set_key(self._dotenv_file, "url", value)
        self.update_timestamp()

    @property
    def token(self):
        return self._config.get("token")

    @token.setter
    def token(self, value):
        dotenv.set_key(self._dotenv_file, "token", value)
        self.update_timestamp()

    @property
    def output_dir(self):
        return self._config.get("output_dir")

    @output_dir.setter
    def output_dir(self, value):
        dotenv.set_key(self._dotenv_file, "output_dir", value)
        self.update_timestamp()

    @property
    def excel_path(self):
        return self._config.get("excel_path")

    @excel_path.setter
    def excel_path(self, value):
        dotenv.set_key(self._dotenv_file, "excel_path", value)
        self.update_timestamp()

    @property
    def logs_dir(self):
        return self._config.get("logs_dir")

    @logs_dir.setter
    def logs_dir(self, value):
        dotenv.set_key(self._dotenv_file, "logs_dir", value)
        self.update_timestamp()
        self.model_events.on_changed()
