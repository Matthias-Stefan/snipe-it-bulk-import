__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import SettingsController
from src.model import Settings
from src.view.tabs import SettingsTab

from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from unittest import TestCase
from unittest.mock import MagicMock


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.controller_mock = MagicMock(spec=SettingsController)
            self.model = Settings()
            self.view = SettingsTab(self.controller_mock, self.model)
    return TestApp()


class TestSettingsTab(TestCase):
    def test_initialization(self):
        test_app = basic_app()
        self.assertEqual(type(test_app.view.controller), type(test_app.controller_mock))
        self.assertEqual(type(test_app.view.model), type(test_app.model))
        self.assertTrue(isinstance(test_app.view.ids.lb_url, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_url, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_token, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_token, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_excel_path, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_excel_path, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_output_folder, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_output_folder, MDTextField))

    def test_set_url(self):
        test_app = basic_app()
        test_url = "10.43.2.90"
        test_app.view.set_url(test_url)
        self.assertEqual(test_url, test_app.controller_mock.url)

    def test_set_token(self):
        test_app = basic_app()
        test_token = "TEST123"
        test_app.view.set_token(test_token)
        self.assertEqual(test_token, test_app.controller_mock.token)

    def test_set_excel_path(self):
        test_app = basic_app()
        test_excel_path = r'C:\Users\file.csv'
        test_app.view.set_excel_path(test_excel_path)
        self.assertEqual(test_excel_path, test_app.controller_mock.excel_path)

    def test_set_output_folder(self):
        test_app = basic_app()
        test_output_folder = r'C:\Users'
        test_app.view.set_output_folder(test_output_folder)
        self.assertEqual(test_output_folder, test_app.controller_mock.output_folder)
