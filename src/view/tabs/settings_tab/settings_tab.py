__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals
from src.model import IModel, ModelProperties

import os

from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class SettingsTab(MDFloatLayout, MDTabsBase):
    """Represents a composition of MDFloatLayout and MDTabsBase.
    This view provides functionalities to specify Database URL, Token, default Output directory, and Excel path.

    :param controller: The controller instance.
    :type controller: src.controller.tab_controller.settings_controller.SettingsController
    :param model: The model instance used for data management.
    :type model: src.model.interface_model.IModel
    :param kwargs: Extra keyword arguments passed to the super constructor
    """
    def __init__(self, controller, model: IModel, **kwargs):
        super(SettingsTab, self).__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Settings"
        self.icon = "cog"

    def set_url(self, url: str):
        """Sets the URL input from the view to the controller.

        :param url: The input received from the view component.
        :type url: str
        :return: None
        """
        self.controller.url = url

    def set_token(self, token: str):
        """Sets the token input from the view to the controller.

        :param token: The input received from the view component.
        :type token: str
        :return: None
        """
        self.controller.token = token

    def set_excel_path(self, excel_path: str):
        """Sets the Excel path input from the view to the controller.

        :param excel_path: The input received from the view component.
        :type excel_path: str
        :return: None
        """
        self.controller.excel_path = excel_path

    def set_output_folder(self, output_folder):
        """Sets the output path input from the view to the controller.

        :param output_folder: The input received from the view component.
        :type output_folder: str
        :return: None
        """
        self.controller.output_dir = output_folder

    def on_model_changed_callback(self, model_property: ModelProperties, value: any):
        """Callback function to handle changes in the model's properties.

        :param model_property: Enum for specifying the receiving property.
        :type model_property: src.model.interface.ModelProperties
        :param value: The new value of the property.
        :type value: any
        :return: None
        """
        if model_property == ModelProperties.URL:
            self.ids.tf_url.text = value
        elif model_property == ModelProperties.TOKEN:
            self.ids.tf_token.text = value
        elif model_property == ModelProperties.OUTPUT_DIR:
            self.ids.tf_output_folder.text = value
        elif model_property == ModelProperties.EXCEL_PATH:
            self.ids.tf_excel_path.text = value


Builder.load_file(os.path.join(Globals.get_settings_tab_package(), "settings_tab.kv"))
