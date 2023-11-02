__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import CheckoutController
from src.model import Checkout
from src.view.tabs import CheckoutTab

import pathlib

from kivymd.uix.button import MDRoundFlatIconButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from unittest import TestCase
from unittest.mock import MagicMock


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.controller_mock = MagicMock(spec=CheckoutController)
            self.model = Checkout()
            self.view = CheckoutTab(self.controller_mock, self.model)
    return TestApp()


class TestCheckoutTab(TestCase):
    def test_initialization(self):
        test_app = basic_app()
        self.assertEqual(type(test_app.view.controller), type(test_app.controller_mock))
        self.assertEqual(type(test_app.view.model), type(test_app.model))
        self.assertTrue(isinstance(test_app.view.ids.lb_file, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.lb_file, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_file, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.bt_open, MDRoundFlatIconButton))
        self.assertTrue(isinstance(test_app.view.ids.lb_autostart, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.cb_autostart, MDCheckbox))
        self.assertTrue(isinstance(test_app.view.ids.lb_auto_upload, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.cb_auto_upload, MDCheckbox))
        self.assertTrue(isinstance(test_app.view.ids.bt_create, MDRaisedButton))
        self.assertEqual(test_app.view.title, "Checkout Template")
        self.assertEqual(test_app.view.icon, "source-branch-check")

    def test_on_template_create(self):
        test_app = basic_app()
        test_app.view.on_template_create()
        self.assertEqual(test_app.controller_mock.method_calls[0][0], CheckoutController.execute.__name__)

    def test_filename_callback(self):
        test_app = basic_app()
        test_filepath = pathlib.Path(r'C:\Users')
        test_app.view.filename_callback(test_filepath)
        self.assertEqual(test_app.view.ids.tf_file.text, str(test_filepath))
        self.assertEqual(test_app.view.ids.tf_file.text, test_app.controller_mock.filepath)

    def test_set_filepath(self):
        test_app = basic_app()
        test_filepath = r'C:\Users\file.csv'
        test_app.view.set_filepath(test_filepath)
        self.assertEqual(test_filepath, test_app.controller_mock.filepath)

    def test_set_autostart(self):
        test_app = basic_app()
        test_app.view.set_autostart(True)
        self.assertEqual(True, test_app.controller_mock.autostart)
        test_app.view.set_autostart(False)
        self.assertEqual(False, test_app.controller_mock.autostart)

    def test_set_auto_upload(self):
        test_app = basic_app()
        test_app.view.set_auto_upload(True)
        self.assertEqual(True, test_app.controller_mock.auto_upload)
        test_app.view.set_auto_upload(False)
        self.assertEqual(False, test_app.controller_mock.auto_upload)

    def test_on_model_changed_callback(self):
        test_app = basic_app()
        test_app.model.filepath = r'C:\Users\file.csv'
        self.assertEqual(test_app.view.ids.tf_file.text, r'C:\Users\file.csv')
