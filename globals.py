__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import os


class Globals:
    _project_dir = os.path.dirname(os.path.abspath(__file__))
    _logs_dir = os.path.join(_project_dir, "logs")
    _source_package = os.path.join(_project_dir, "src")
    _model_package = os.path.join(_source_package, "model")
    _settings_package = os.path.join(_model_package, "settings")

    _view_package = os.path.join(_source_package, "view")
    _tabs_package = os.path.join(_view_package, "tabs")
    _checkout_tab_package = os.path.join(_tabs_package, "checkout_tab")
    _create_asset_tab_package = os.path.join(_tabs_package, "create_asset_tab")
    _settings_tab_package = os.path.join(_tabs_package, "settings_tab")
    _upload_tab_package = os.path.join(_tabs_package, "upload_tab")

    _file_browser_package = os.path.join(_view_package, "file_browser")
    _progress_package = os.path.join(_view_package, "progress")

    @staticmethod
    def get_project_dir():
        return Globals._project_dir

    @staticmethod
    def get_logs_dir():
        return Globals._logs_dir

    @staticmethod
    def get_source_package():
        return Globals._source_package

    @staticmethod
    def get_model_package():
        return Globals._model_package

    @staticmethod
    def get_settings_package():
        return Globals._settings_package

    @staticmethod
    def get_view_package():
        return Globals._view_package

    @staticmethod
    def get_tabs_package():
        return Globals._tabs_package

    @staticmethod
    def get_checkout_tab_package():
        return Globals._checkout_tab_package

    @staticmethod
    def get_create_asset_tab_package():
        return Globals._create_asset_tab_package

    @staticmethod
    def get_settings_tab_package():
        return Globals._settings_tab_package

    @staticmethod
    def get_upload_tab_package():
        return Globals._upload_tab_package

    @staticmethod
    def get_file_browser_package():
        return Globals._file_browser_package

    @staticmethod
    def get_progress_package():
        return Globals._progress_package
