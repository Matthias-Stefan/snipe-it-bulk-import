__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import CreateAssetController
from src.model import CreateAsset
from src.view.tabs import CreateAssetTab

import pathlib

from kivy.uix.spinner import Spinner
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
            self.controller_mock = MagicMock(spec=CreateAssetController)
            self.model = CreateAsset()
            self.view = CreateAssetTab(self.controller_mock, self.model)
    return TestApp()


class TestCreateAssetTab(TestCase):
    def test_initialization(self):
        test_app = basic_app()
        self.assertEqual(type(test_app.view.controller), type(test_app.controller_mock))
        self.assertEqual(type(test_app.view.model), type(test_app.model))
        self.assertTrue(isinstance(test_app.view.ids.lb_model, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.sp_model, Spinner))
        self.assertTrue(isinstance(test_app.view.ids.tf_model, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_quantity, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_quantity, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_status_label, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.sp_status_label, Spinner))
        self.assertTrue(isinstance(test_app.view.ids.tf_status_label, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.lb_file, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.tf_file, MDTextField))
        self.assertTrue(isinstance(test_app.view.ids.bt_open, MDRoundFlatIconButton))
        self.assertTrue(isinstance(test_app.view.ids.lb_autostart, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.cb_autostart, MDCheckbox))
        self.assertTrue(isinstance(test_app.view.ids.lb_auto_upload, MDLabel))
        self.assertTrue(isinstance(test_app.view.ids.cb_auto_upload, MDCheckbox))
        self.assertTrue(isinstance(test_app.view.ids.bt_create, MDRaisedButton))
        self.assertEqual(test_app.view.title, "Create Asset Template")
        self.assertEqual(test_app.view.icon, "devices")

    def test_on_template_create(self):
        test_app = basic_app()
        test_app.view.on_template_create()
        self.assertEqual(test_app.controller_mock.method_calls[0][0], CreateAssetController.execute.__name__)

    def test_filename_callback(self):
        test_app = basic_app()
        test_filepath = pathlib.Path(r'C:\Users')
        test_app.view.filename_callback(test_filepath)
        self.assertEqual(test_app.view.ids.tf_file.text, str(test_filepath))
        self.assertEqual(test_app.view.ids.tf_file.text, test_app.controller_mock.filepath)

    def test_set_sit_models(self):
        test_app = basic_app()
        sit_models = {"Model 1 <1>": "1", "Model 2 <2>": "2"}
        test_app.view.set_sit_models(sit_models)
        self.assertEqual(test_app.view.ids.sp_model.text, "Model 1 <1>")
        self.assertEqual(test_app.view.selected_sit_models[0], "Model 1 <1>")
        self.assertEqual(test_app.view.selected_sit_models[1], "Model 2 <2>")

    def test_set_sit_model(self):
        test_app = basic_app()
        test_model = "Model1"
        test_app.view.set_sit_model(test_model)
        self.assertEqual(test_model, test_app.controller_mock.sit_model)

    def test_set_quantity(self):
        test_app = basic_app()
        test_quantity = 100
        test_app.view.set_quantity(test_quantity)
        self.assertEqual(test_quantity, test_app.controller_mock.quantity)

    def test_set_status_labels(self):
        test_app = basic_app()
        test_status_labels = {"Test 1 <41>": "41", "Test 2 <42>": "42", "Test 3 <43>": "43"}
        test_app.view.set_status_labels(test_status_labels)
        self.assertEqual(test_app.view.ids.sp_status_label.text, "Test 1 <41>")
        self.assertEqual(test_app.view.selected_status_labels[0], "Test 1 <41>")
        self.assertEqual(test_app.view.selected_status_labels[1], "Test 2 <42>")
        self.assertEqual(test_app.view.selected_status_labels[2], "Test 3 <43>")

    def test_set_status_label(self):
        test_app = basic_app()
        test_status_label = "Status Label 1"
        test_app.view.set_status_label(test_status_label)
        self.assertEqual(test_status_label, test_app.controller_mock.status_label)

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

    def test_filter_sit_model(self):
        test_app = basic_app()
        test_dict = {"Model 1 <1>": "Model 1", "Model 2 <2>": "2"}
        test_app.controller_mock.sit_models = test_dict
        test_app.view.set_sit_models(test_dict)
        test_app.view.filter_sit_model = "2"
        self.assertEqual(test_app.view.selected_sit_models[0], "Model 2 <2>")
        test_app.view.filter_sit_model = "1"
        self.assertEqual(test_app.view.selected_sit_models[0], "Model 1 <1>")
        test_app.view.filter_sit_model = ""
        self.assertEqual(test_app.view.selected_sit_models[0], "Model 1 <1>")
        self.assertEqual(test_app.view.selected_sit_models[1], "Model 2 <2>")

    def test_filter_status_label(self):
        test_app = basic_app()
        test_dict = {"Status Label 1 <1>": "Status Label 1", "Status Label 2 <2>": "Status Label 2"}
        test_app.controller_mock.status_labels = test_dict
        test_app.view.set_status_labels(test_dict)
        test_app.view.filter_status_label = "2"
        self.assertEqual(test_app.view.selected_status_labels[0], "Status Label 2 <2>")
        test_app.view.filter_status_label = "1"
        self.assertEqual(test_app.view.selected_status_labels[0], "Status Label 1 <1>")
        test_app.view.filter_status_label = ""
        self.assertEqual(test_app.view.selected_status_labels[0], "Status Label 1 <1>")
        self.assertEqual(test_app.view.selected_status_labels[1], "Status Label 2 <2>")

    def test_on_model_changed_callback(self):
        test_app = basic_app()
        test_app.model.filepath = r'C:\Users\file.csv'
        self.assertEqual(test_app.view.ids.tf_file.text, r'C:\Users\file.csv')







