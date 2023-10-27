__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from globals import Globals
from src.view.progress import ProgressInfo

import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout


class MainView(MDFloatLayout):
    """Represents the main view of the application.

    :param controller: The main controller instance for managing the application.
    :type controller: src.controller.main_controller.MainController
    """
    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(**kwargs)
        for arg in args:
            self.ids.tabs.add_widget(arg)

    def reset_progress(self, *args):
        """Resets the progress information.

        :param args:
        """
        self.ids.progress_info.reset()

    def advance_progress(self, amount: int, info: str, state: bool, *args):
        """Advances the progress and updates progress information.

        :param amount: The amount by which to advance the progress.
        :type amount: int
        :param info: Additional information about the progress.
        :type info: str
        :param state: The current state of the progress.
        :type state: bool
        :param args:
        """
        self.ids.progress_info.advance(amount, info, state)


Builder.load_file(os.path.join(Globals.get_view_package(), "main_view.kv"))
Builder.load_file(os.path.join(Globals.get_progress_package(), "progress.kv"))
Builder.load_file(os.path.join(Globals.get_file_browser_package(), "file_browser.kv"))
