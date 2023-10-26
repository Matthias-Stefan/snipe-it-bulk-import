__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals

import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout


class MainView(MDFloatLayout):
    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(**kwargs)
        for arg in args:
            self.ids.tabs.add_widget(arg)

    def reset_progress(self, *args):
        self.ids.progress_info.reset()

    def advance_progress(self, amount, info, state, *args):
        self.ids.progress_info.advance(amount, info, state)


Builder.load_file(os.path.join(Globals.get_view_package(), "main_view.kv"))
Builder.load_file(os.path.join(Globals.get_progress_package(), "progress.kv"))
Builder.load_file(os.path.join(Globals.get_file_browser_package(), "file_browser.kv"))
