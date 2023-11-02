__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from main import Main

import kivy
kivy.require('2.2.1')

from kivy.tests.common import GraphicUnitTest


class TestMainApp(GraphicUnitTest):
    # TODO: use Mock!
    def test_initialization(self):
        main = Main()
        self.assertTrue(main)
        self.assertEqual(main.theme_cls.theme_style, "Dark")
        self.assertEqual(main.icon, r"res/icon.png")
        self.assertEqual(main.title, "Snipe-IT Bulk Import")
        self.assertTrue(main.controller)
        self.assertTrue(main.controller.view.ids.tabs)
        self.assertEqual(main.title, "Snipe-IT Bulk Import")
        self.assertEqual(main.controller.view.ids.tabs.tab_bar_height, 50)
        self.assertTrue(main.controller.view.ids.progress_info)
