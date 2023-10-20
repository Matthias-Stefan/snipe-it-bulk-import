"""main_window.py

"""

__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.view.progress import ProgressInfo
from src.view.tabs import CreateAssetTab, UploadTab, CheckoutTab, SettingsTab

import kivy
kivy.require('2.2.1')
import os

from kivy.lang import Builder
from kivymd.app import MDApp


class MainWindow(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.icon = r"res/icon.png"
        self.title = "Snipe-IT Bulk Import"

        Builder.load_file(os.path.join(os.path.dirname(__file__), "progress/progress.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "filebrowser/filebrowser.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/createassettab/createassettab.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/checkouttab/checkouttab.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/uploadtab/uploadtab.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/settingstab/settingstab.kv"))
        return Builder.load_file(os.path.join(os.path.dirname(__file__), "main.kv"))

    def on_start(self):
        self.root.ids.tabs.add_widget(CreateAssetTab())
        self.root.ids.tabs.add_widget(CheckoutTab())
        self.root.ids.tabs.add_widget(UploadTab())
        self.root.ids.tabs.add_widget(SettingsTab())

        self.reset_progress()
        self.advance_progress(20, "TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST")
        return

    def reset_progress(self):
        self.root.ids.progress_info.reset()

    def advance_progress(self, amount, info):
        self.root.ids.progress_info.advance(amount, info)

