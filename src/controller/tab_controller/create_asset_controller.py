__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import IController
from src.manager import SnipeManager
from src.model import CreateAsset
from src.template import ITemplate, CreateAssetTemplate
from src.view.tabs import CreateAssetTab

import subprocess
import threading


class CreateAssetController(IController):
    def __init__(self, parent=None):
        super(CreateAssetController, self).__init__(parent)
        self.sit_models: dict = {}
        self.status_labels: dict = {}

        self._model = CreateAsset()
        self._view = CreateAssetTab(controller=self, model=self._model)

    def post_init(self):
        snipe_manager = SnipeManager()
        self.progress_reset()
        self.progress_advance(0, "Start fetching models")
        data_index = 0
        for data, total in snipe_manager.request_all_sit_models():
            progress_threshold = total / 10
            for sit_model in data:
                self.sit_models[f"{sit_model['name']} <{sit_model['id']}>"] = sit_model
                if data_index > progress_threshold:
                    self.progress_advance(1, "Fetching models")
                data_index += 1
        self._view.set_sit_models(self.sit_models)
        self.progress_advance(100, "Fetched models successfully")

        self.progress_reset(1)
        self.progress_advance(0, "Start fetching status labels")
        data_index = 0
        for data, total in snipe_manager.request_all_status_labels():
            progress_threshold = total / 10
            for status_label in data:
                self.status_labels[f"{status_label['name']} <{status_label['id']}>"] = status_label
                if data_index > progress_threshold:
                    self.progress_advance(1, "Fetching status labels")
                data_index += 1
        self._view.set_status_labels(self.status_labels)
        self.progress_advance(100, "Fetched status labels successfully")

        from src.controller import MainController
        if isinstance(self.parent, MainController):
            output_dir = self.parent.get_settings_controller().output_dir
            if output_dir is not None and output_dir != "":
                self.model.filepath = output_dir

    def execute(self, **kwargs):
        def _execute():
            self.progress_reset()
            self.progress_advance(0, "Start creating csv")
            self.progress_advance(10, "Prepare Template", timeout=1)
            create_asset_template: ITemplate = CreateAssetTemplate(
                sit_model=self.sit_models[self.sit_model],
                quantity=self.quantity,
                status_label=self.status_labels[self.status_label],
                filepath=self.filepath
            )
            file = create_asset_template.create()
            self.progress_advance(20, "Open Excel", timeout=1)
            if self.autostart:
                from src.controller import MainController
                if isinstance(self.parent, MainController):
                    excel_path = self.parent.get_settings_controller().excel_path
                    if self.auto_upload:
                        self.progress_advance(30, "Wait for Excel to close", timeout=1)
                        subprocess.call([excel_path, file])
                        upload_controller = self.parent.get_upload_controller()
                        upload_controller.filepath = str(file)
                        upload_controller.execute()
                    else:
                        subprocess.Popen([excel_path, file])
            self.progress_advance(100, "Task finished", timeout=1)

        thread: threading.Thread = threading.Thread(target=_execute)
        thread.daemon = True
        thread.start()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    @property
    def sit_model(self):
        """Retrieve the current model.

        :type: str
        """
        return self.model.model

    @sit_model.setter
    def sit_model(self, value):
        self.model.model = value

    @property
    def quantity(self):
        """The quantity for asset creation.

        :type: int
        """
        return self.model.quantity

    @quantity.setter
    def quantity(self, value):
        self.model.quantity = int(value)

    @property
    def status_label(self):
        """Retrieve the status label.

        :type: str
        """
        return self.model.status_label

    @status_label.setter
    def status_label(self, value):
        self.model.status_label = value

    @property
    def filepath(self):
        """The path or filename of the new CSV to be created.

        :type: pathlib.Path
        """
        return self.model.filepath

    @filepath.setter
    def filepath(self, value):
        self.model.filepath = value

    @property
    def autostart(self):
        """Determine if Excel should be automatically invoked.

        :type: bool
        """
        return self.model.autostart

    @autostart.setter
    def autostart(self, value):
        self.model.autostart = value

    @property
    def auto_upload(self):
        """Determine if CSV should be automatically uploaded.

        :type: bool
        """
        return self.model.auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        self.model.auto_upload = value
