__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import UploadController
from src.model import Upload
from src.view.tabs import UploadTab

from kivymd.uix.button import MDRoundFlatIconButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from unittest import TestCase
from unittest.mock import MagicMock


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.controller_mock = MagicMock(spec=UploadController)
            self.model = Upload()
            self.view = UploadTab(self.controller_mock, self.model)
    return TestApp()


class TestUploadTab(TestCase):
    def test_initialization(self):
        test_app = basic_app()
        self.assertEqual(type(test_app.view.controller), type(test_app.controller_mock))
        self.assertEqual(type(test_app.view.model), type(test_app.model))
        self.assertTrue(isinstance(test_app.view.ids.lb_file, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_file, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.bt_open, MDRoundFlatIconButton))
        self.assertTrue(isinstance(test_app.view.ids.bt_upload, MDRaisedButton))

    def test_on_template_create(self):
        test_app = basic_app()
        test_app.view.on_upload()
        self.assertEqual(test_app.controller_mock.method_calls[0][0], UploadController.execute.__name__)

    def test_set_filepath(self):
        test_app = basic_app()
        test_filepath = r'C:\Users\file.csv'
        test_app.view.set_filepath(test_filepath)
        self.assertEqual(test_filepath, test_app.controller_mock.filepath)

    def test_on_model_changed_callback(self):
        test_app = basic_app()
        test_app.model.filepath = r'C:\Users\file.csv'
        self.assertEqual(test_app.view.ids.tf_file.text, r'C:\Users\file.csv')

