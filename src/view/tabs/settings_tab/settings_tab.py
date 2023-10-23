__author__ = "Matthias Stefan"
__version__ = "0.1.1"

from globals import Globals

import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class SettingsTab(MDFloatLayout, MDTabsBase):
    """User Settings for Storing URL, Token, Excel Path, and Output Path.


    :param kwargs: Extra keyword arguments passed to the super constructor.
    """
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(SettingsTab, self).__init__(**kwargs)
        self.title = "Settings"
        self.icon = "cog"

        self._url = ""
        self._token = ""
        self._excel_path = ""
        self._predefine_output_folder = ""

    def on_save(self):
        """Initiates the save process.

        :rtype: None
        """
        pass

    @property
    def url(self):
        """Retrieve the current url.

        :rtype: None
        """
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        self.ids.tf_url.text = value

    @property
    def token(self):
        """Retrieve the current token.

        :rtype: None
        """
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        self.ids.tf_token.text = value

    @property
    def excel_path(self):
        """Retrieve the current excel path.

        :rtype: None
        """
        return self._excel_path

    @excel_path.setter
    def excel_path(self, value):
        self._excel_path = value
        self.ids.tf_excel_path.text = value

    @property
    def predefine_output_folder(self):
        """Retrieve the defined output folder.

        :rtype: None
        """
        return self._predefine_output_folder

    @predefine_output_folder.setter
    def predefine_output_folder(self, value):
        self._predefine_output_folder = value
        self.ids.tf_predefine_output_folder.text = value


Builder.load_file(os.path.join(Globals.get_settings_tab_package(), "settings_tab.kv"))
