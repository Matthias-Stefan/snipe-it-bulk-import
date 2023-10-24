__author__ = "Matthias Stefan"
__version__ = "0.1.1"

from globals import Globals
from src.model import IModel, ModelProperties

import os

from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class SettingsTab(MDFloatLayout, MDTabsBase):
    """User Settings for Storing URL, Token, Excel Path, and Output Path.


    :param kwargs: Extra keyword arguments passed to the super constructor.
    """
    def __init__(self, controller, model: IModel, **kwargs):
        super(SettingsTab, self).__init__(**kwargs)
        self.controller = controller
        self.model = model
        self.model.model_events.on_changed += self.on_model_changed_callback

        self.title = "Settings"
        self.icon = "cog"

    def set_url(self, url):
        self.controller.url = url

    def set_token(self, token):
        self.controller.token = token

    def set_excel_path(self, excel_path):
        self.controller.excel_path = excel_path

    def set_output_folder(self, output_folder):
        self.controller.output_dir = output_folder

    def on_model_changed_callback(self, model_property: ModelProperties, value):
        if model_property == ModelProperties.URL:
            self.ids.tf_url.text = value
        elif model_property == ModelProperties.TOKEN:
            self.ids.tf_token.text = value
        elif model_property == ModelProperties.OUTPUT_DIR:
            self.ids.tf_output_folder.text = value
        elif model_property == ModelProperties.EXCEL_PATH:
            self.ids.tf_excel_path.text = value


Builder.load_file(os.path.join(Globals.get_settings_tab_package(), "settings_tab.kv"))
