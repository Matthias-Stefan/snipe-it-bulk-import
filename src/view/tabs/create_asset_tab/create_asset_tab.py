__author__ = "Matthias Stefan"
__version__ = "0.2.0"

from globals import Globals
from src.model import IModel, ModelProperties
from src.view.file_browser import FileBrowser

import os

from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class CreateAssetTab(MDFloatLayout, MDTabsBase):
    """Generating the Asset Creation CSV. Within the template, there are choices for enabling automatic Excel opening.
    When auto-upload is selected, the application will wait until Excel is closed and then proceed with an automatic
    upload.

    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    selected_sit_models = ListProperty()
    selected_status_labels = ListProperty()

    def __init__(self, controller, model: IModel, **kwargs):
        super(CreateAssetTab, self).__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Create Asset Template"
        self.icon = "devices"

        self._filter_sit_model = ""
        self._filter_status_label = ""

    def on_template_create(self):
        """Initiates the creation process.

        :rtype: None
        """
        self.controller.execute()

    def open_filebrowser(self):
        """Opens the file chooser dialog.

        :rtype: None
        """
        file_dialog = FileBrowser(self.filename_callback)
        file_dialog.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a filepath.

        :param filepath:
        :type filepath: pathlib.Path
        :rtype: None
        """
        self.set_filepath(filepath)
        self.ids.tf_file.text = str(filepath)

    def set_sit_models(self, sit_models: dict):
        self.selected_sit_models = [key for key in sit_models.keys()]
        self.ids.sp_model.text = self.selected_sit_models[0]
        self.set_sit_model(self.selected_sit_models[0])

    def set_sit_model(self, value):
        self.controller.sit_model = value

    def set_quantity(self, value):
        self.controller.quantity = value

    def set_status_labels(self, status_labels: dict):
        self.selected_status_labels = [key for key in status_labels.keys()]
        self.ids.sp_status_label.text = self.selected_status_labels[0]
        self.set_status_label(self.selected_status_labels[0])

    def set_status_label(self, value):
        self.controller.status_label = value

    def set_filepath(self, value):
        self.controller.filepath = value

    def set_autostart(self, value):
        self.controller.autostart = value

    def set_auto_upload(self, value):
        self.controller.auto_upload = value

    @property
    def filter_sit_model(self):
        """Filter the dropdown menu.

        :type: str
        """
        return self._filter_sit_model

    @filter_sit_model.setter
    def filter_sit_model(self, value):
        self.ids.sp_model.is_open = True
        self._filter_sit_model = value
        if len(str(value)) > 0:
            selected_sit_models = [elem for elem in self.controller.sit_models.keys() if
                                   elem.find(self._filter_sit_model) != -1]
            self.selected_sit_models = selected_sit_models
        else:
            self.selected_sit_models = [elem for elem in self.controller.sit_models.keys()]

    @property
    def filter_status_label(self):
        """Filter the dropdown menu.

        :type: str
        """
        return self._filter_status_label

    @filter_status_label.setter
    def filter_status_label(self, value):
        self.ids.sp_status_label.is_open = True
        self._filter_status_label = value
        if len(str(value)) > 0:
            selected_status_labels = [elem for elem in self.controller.status_labels.keys() if
                                      elem.find(self._filter_status_label) != -1]
            self.selected_status_labels = selected_status_labels
        else:
            self.selected_status_labels = self.status_labels

    def on_model_changed_callback(self, model_property: ModelProperties, value):
        if model_property == ModelProperties.FILEPATH:
            self.ids.tf_file.text = value


Builder.load_file(os.path.join(Globals.get_create_asset_tab_package(), "create_asset_tab.kv"))
