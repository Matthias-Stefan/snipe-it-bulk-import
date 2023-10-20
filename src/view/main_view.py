__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.view.progress import ProgressInfo
from src.view.tabs import CreateAssetTab, UploadTab, CheckoutTab, SettingsTab

import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout


class MainView(MDFloatLayout):
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.ids.tabs.add_widget(CreateAssetTab())
        self.ids.tabs.add_widget(CheckoutTab())
        self.ids.tabs.add_widget(UploadTab())
        self.ids.tabs.add_widget(SettingsTab())

    def reset_progress(self):
        self.ids.progress_info.reset()

    def advance_progress(self, amount, info):
        self.ids.progress_info.advance(amount, info)

    def add_tab(self, tab: MDFloatLayout):
        self.ids.tabs.add_widget(tab)


Builder.load_file(os.path.join(os.path.dirname(__file__), "progress/progress.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "file_browser/file_browser.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/create_asset_tab/create_asset_tab.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/checkout_tab/checkout_tab.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/upload_tab/upload_tab.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/settings_tab/settings_tab.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "main_view.kv"))
