"""main_window.py

"""

__author__ = "Matthias Stefan"
__version__ = "0.0.1"

from src.view.tabs import TemplateTab
from src.view.progress import ProgressInfo

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
        Builder.load_file(os.path.join(os.path.dirname(__file__), "savedialog/savedialog.kv"))
        Builder.load_file(os.path.join(os.path.dirname(__file__), "tabs/templatetab/templatetab.kv"))
        return Builder.load_file(os.path.join(os.path.dirname(__file__), "main.kv"))

    def on_start(self):
        self.root.ids.tabs.add_widget(TemplateTab())
        #self.root.ids.tabs.add_widget(UploadTab())
        #self.root.ids.tabs.add_widget(CheckoutTab())
        #self.root.ids.tabs.add_widget(SetupTab())

        self.reset_progress()
        self.advance_progress(20, "TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST")
        return

    def reset_progress(self):
        self.root.ids.progress_info.reset()

    def advance_progress(self, amount, info):
        self.root.ids.progress_info.advance(amount, info)

