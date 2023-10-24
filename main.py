__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import MainController
from src.manager import SnipeManager


import kivy
kivy.require('2.2.1')

from kivy.clock import Clock
from kivymd.app import MDApp


class Main(MDApp):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.icon = r"res/icon.png"
        self.title = "Snipe-IT Bulk Import"

        self.controller = MainController()
        self.snipe_manager = SnipeManager()
        self.snipe_manager.post_init(self.controller.get_settings_controller().url,
                                     self.controller.get_settings_controller().token)

    def build(self):
        return self.controller.view

    def on_start(self):
        self.controller.post_init()


if __name__ == '__main__':
    Main().run()

