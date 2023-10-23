__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.controller import MainController
from src.model import Settings


import kivy
kivy.require('2.2.1')

from kivymd.app import MDApp


class Main(MDApp):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.icon = r"res/icon.png"
        self.title = "Snipe-IT Bulk Import"

        self.controller = MainController()
        self.settings = Settings()

    def build(self):
        return self.controller.view


if __name__ == '__main__':
    Main().run()

