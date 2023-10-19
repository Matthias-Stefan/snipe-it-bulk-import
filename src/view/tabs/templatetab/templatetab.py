__author__ = "Matthias Stefan"
__version__ = "0.0.1"

from src.view.savedialog import SaveDialog

import os

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty
from pathlib import Path


class TemplateTab(MDFloatLayout, MDTabsBase):
    """This section is for specifying details for creating the Assetcreate CSV. In the template, options are
    available for automatic Excel opening. In the case of autoupload, the app waits until Excel is closed and
    then initiates an automatic upload.

    :inherits: kivymd.uix.tab.MDTabsBase, kivymd.uix.floatlayout.MDFloatLayout
    :param kwargs: Extra keyword arguments passed to the super constructor.
    """

    models = [f"value_t{i}" for i in range(5)]+[f"test{i}" for i in range(5)]
    selected_models = ListProperty(models)

    status_labels = ["Undeployable", "Deployable", "Archived", "Pending"]
    selected_status_labels = ListProperty(status_labels)

    def __init__(self, **kwargs):
        super(TemplateTab, self).__init__(**kwargs)
        self.title = "Template"
        self.icon = "file-table"

        self._model = ""
        self._quantity = 0
        self._status_label = ""
        self._filepath = None
        self._autostart = False
        self._auto_upload = False

        self._filter_model = ""
        self._filter_status_label = ""

    def on_template_create(self):
        """Initiates the creation process.

        :rtype: None
        """
        pass

    def open_filechooser(self):
        """Opens the file chooser dialog.

        :rtype: None
        """
        save_dialog = SaveDialog(self.filename_callback)
        save_dialog.open()

    def filename_callback(self, filepath: Path):
        """Callback to receive a file path.

        :param filepath:
        :type filepath: pathlib.Path
        :rtype: None
        """
        self._filepath = filepath
        self.ids.tf_file.text = str(self._filepath)

    @property
    def model(self):
        """Retrieve the current model.

        :type: str
        """
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def filter_model(self):
        """Filter the dropdown menu.

        :type: str
        """
        return self._filter_model

    @filter_model.setter
    def filter_model(self, value):
        self.ids.sp_model.is_open = True
        self._filter_model = value
        if len(str(value)) > 0:
            selected_models = [elem for elem in self.models if elem.find(self._filter_model) != -1]
            self.selected_models = selected_models
        else:
            self.selected_models = self.models

    @property
    def quantity(self):
        """The quantity for asset creation.

        :type: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value.isdigit():
            self._quantity = int(value)

    @property
    def status_label(self):
        """Retrieve the status label.

        :type: str
        """
        return self._status_label

    @status_label.setter
    def status_label(self, value):
        self._status_label = value

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
            selected_status_labels = [elem for elem in self.status_labels if elem.find(self._filter_status_label) != -1]
            self.selected_status_labels = selected_status_labels
        else:
            self.selected_status_labels = self.status_labels

    @property
    def filepath(self):
        """The path or filename of the new CSV to be created.

        :type: pathlib.Path
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        path = Path(value)
        if os.path.exists(path.parent.absolute()):
            self._filepath = path

    @property
    def autostart(self):
        """Determine if Excel should be automatically invoked.

        :type: bool
        """
        return self._autostart

    @autostart.setter
    def autostart(self, value):
        self._autostart = value

    @property
    def auto_upload(self):
        """Determine if CSV should be automatically uploaded.

        :type: bool
        """
        return self._auto_upload

    @auto_upload.setter
    def auto_upload(self, value):
        self._auto_upload = value