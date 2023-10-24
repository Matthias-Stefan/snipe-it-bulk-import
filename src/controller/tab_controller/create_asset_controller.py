__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import IController
from src.manager import SnipeManager
from src.model.create_asset import CreateAsset
from src.view.tabs import CreateAssetTab

from functools import partial
from kivy.clock import Clock


class CreateAssetController(IController):
    def __init__(self, parent=None):
        super(CreateAssetController, self).__init__(parent)
        self.sit_models: dict = {}
        self.status_labels: dict = {}

        self._model = CreateAsset()
        self._view = CreateAssetTab(controller=self, model=self._model)

    def post_init(self):
        snipe_manager = SnipeManager()
        self.progress_events.reset()
        Clock.schedule_once(partial(self.progress_events.advance, 0, "Start fetching models"), 0)
        data_index = 0
        for data, total in snipe_manager.request_all_sit_models():
            progress_threshold = total / 10
            for sit_model in data:
                self.sit_models[f"{sit_model['name']} <{sit_model['id']}>"] = sit_model
                if data_index > progress_threshold:
                    Clock.schedule_once(partial(self.progress_events.advance, 1, "Fetching models"), 0)
                data_index += 1
        self._view.set_sit_models(self.sit_models)
        Clock.schedule_once(partial(self.progress_events.advance, 100, "Fetched models successfully"), 0)

        Clock.schedule_once(partial(self.progress_events.advance, 0, "Start fetching status labels"), 0)
        data_index = 0
        for data, total in snipe_manager.request_all_status_labels():
            progress_threshold = total / 10
            for status_label in data:
                self.status_labels[f"{status_label['name']} <{status_label['id']}>"] = status_label
                if data_index > progress_threshold:
                    Clock.schedule_once(partial(self.progress_events.advance, 1, "Fetching status labels"), 0)
                data_index += 1
        self._view.set_status_labels(self.status_labels)
        Clock.schedule_once(partial(self.progress_events.advance, 100, "Fetched status labels successfully"), 0)

        from src.controller import MainController
        if isinstance(self.parent, MainController):
            output_dir = self.parent.get_settings_controller().output_dir
            if output_dir is not None and output_dir != "":
                self.model.filepath = output_dir

    def execute(self, **kwargs):
        self.progress_events.reset()
        # ...
        self.progress_events.advance()

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
