__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals
from src.model import IModel, ModelProperties
from src.view.file_browser import FileBrowser

import os

from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from pathlib import Path


class CreateAssetTab(MDFloatLayout, MDTabsBase):
    """Represents a composition of MDFloatLayout and MDTabsBase.
     This view allows users to specify Snipe-IT model, set the quantity (the number of pre-filled Excel rows based on
     the model), select a Snipe-IT status label, and create a CSV file using the src.view.file_browser.FileBrowser.
     When auto-upload is enabled, the application will wait until Excel is closed before proceeding with an automatic
     upload.

    :param controller: The controller instance.
    :type controller: src.controller.tab_controller.create_asset_controller.CreateAssetController
    :param model: The model instance used for data management.
    :type model: src.model.interface_model.IModel
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
        """Opens the file browser.

        :rtype: None
        """
        file_browser = FileBrowser(self.filename_callback)
        file_browser.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a filepath.

        :param filepath: The selected filepath.
        :type filepath: pathlib.Path
        :rtype: None
        """
        self.set_filepath(str(filepath))
        self.ids.tf_file.text = str(filepath)

    def set_sit_models(self, sit_models: dict):
        """Sets the available SIT models in the view.

        :param sit_models: A dictionary of available Snipe-IT models.
        :type sit_models: dict
        :rtype: None
        """
        self.selected_sit_models = [key for key in sit_models.keys()]
        self.ids.sp_model.text = self.selected_sit_models[0]
        self.set_sit_model(self.selected_sit_models[0])

    def set_sit_model(self, value: str):
        """Sets the selected Snipe-IT model to the controller.

        :param value: The selected Snipe-IT model.
        :type value: str
        :rtype: None
        """
        self.controller.sit_model = value

    def set_quantity(self, value: int):
        """Sets the quantity value to the controller.

        :param value: The quantity value.
        :type value: int
        :rtype: None
        """
        self.controller.quantity = value

    def set_status_labels(self, status_labels: dict):
        """Sets the available status labels in the view.

        :param status_labels: A dictionary of available status labels.
        :type status_labels: dict
        :rtype: None
        """
        self.selected_status_labels = [key for key in status_labels.keys()]
        self.ids.sp_status_label.text = self.selected_status_labels[0]
        self.set_status_label(self.selected_status_labels[0])

    def set_status_label(self, value: str):
        """Sets the selected status label to the controller.

        :param value: The selected status label.
        :type value: str
        :rtype: None
        """
        self.controller.status_label = value

    def set_filepath(self, value: str):
        """Sets the filepath in the controller.

        :param value: The filepath to set
        :type value: str
        :rtype: str
        """
        self.controller.filepath = value

    def set_autostart(self, value: bool):
        """Sets the autostart setting to the controller.

        :param value: The autostart setting.
        :type value: bool
        :rtype: None
        """
        self.controller.autostart = value

    def set_auto_upload(self, value: bool):
        """Sets the auto-upload setting to the controller.

        :param value: The auto-upload setting.
        :type value: bool
        :rtype: None
        """
        self.controller.auto_upload = value

    @property
    def filter_sit_model(self):
        """Filters the dropdown menu for Snipe-IT models.

        :type: str
        """
        return self._filter_sit_model

    @filter_sit_model.setter
    def filter_sit_model(self, value: str):
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
    def filter_status_label(self, value: str):
        self.ids.sp_status_label.is_open = True
        self._filter_status_label = value
        if len(str(value)) > 0:
            selected_status_labels = [elem for elem in self.controller.status_labels.keys() if
                                      elem.find(self._filter_status_label) != -1]
            self.selected_status_labels = selected_status_labels
        else:
            self.selected_status_labels = self.status_labels

    def on_model_changed_callback(self, model_property: ModelProperties, value: any):
        """Callback function to handle changes in the model's properties.

        :param model_property: Enum for specifying the receiving property.
        :type model_property: src.model.interface_model.ModelProperties
        :param value: The new value of the property.
        :type value: any
        :rtype: None
        """
        if model_property == ModelProperties.FILEPATH:
            self.ids.tf_file.text = value


Builder.load_file(os.path.join(Globals.get_create_asset_tab_package(), "create_asset_tab.kv"))
