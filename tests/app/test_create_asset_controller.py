__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import CreateAssetController, MainController
from src.template import CreateAssetTemplate
from src.manager.snipe_manager import SnipeManager

from unittest import TestCase
from unittest.mock import patch, mock_open


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.main_controller = MainController()
            self.controller = CreateAssetController(self.main_controller)
    return TestApp()


class TestCreateAssetTemplate(TestCase):
    def test_create(self):
        create_instance = CreateAssetTemplate(
            {"Test Model <1>": "1"}, 1, {"Test Status Label <1>:": "1"},
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        )
        with patch('builtins.open', new_callable=mock_open()) as mock_open_func:
            result = create_instance.create()
            mock_open_func.assert_called_with(result, 'w+', newline='', encoding='utf-8-sig')


class TestCreateAssetController(TestCase):
    def test_post_init_call(self):
        test_app = basic_app()
        snipe_manager = SnipeManager()
        with patch.object(snipe_manager, 'request_all_sit_models') as request_all_sit_models_mock, \
             patch.object(snipe_manager, 'request_all_status_labels') as request_all_status_labels_mock, \
             patch.object(test_app.controller, 'progress_advance') as progress_advance_mock:
            request_all_sit_models_mock.return_value = [([{'id': '1', 'name': 'test_model_1'},
                                                          {'id': '2', 'name': 'test_model_2'}], 2)]
            request_all_status_labels_mock.return_value = [([{'id': '1', 'name': 'test_label_1'},
                                                             {'id': '2', 'name': 'test_model_2'}], 2)]
            test_app.controller.post_init()
            request_all_sit_models_mock.assert_called()
            request_all_status_labels_mock.assert_called()
            calls = [
                (0, 'Start fetching models'),
                (1, 'Fetching models'),
                (100, 'Fetched models successfully'),
                (0, 'Start fetching status labels'),
                (1, 'Fetching status labels'),
                (100, 'Fetched status labels successfully')
            ]
            for args in calls:
                progress_advance_mock.assert_any_call(*args)
            self.assertIsNotNone(test_app.controller.model.filepath)

    @patch("threading.Thread")
    def test_threading_start(self, thread_exe):
        test_app = basic_app()
        test_app.controller.sit_models = {'1': {'id': 1},
                                          '2': {'id': 2}}
        test_app.controller.sit_model = '1'
        test_app.controller.quantity = 1
        test_app.controller.status_labels = {'1': {'id': 1},
                                             '2': {'id': 2}}
        test_app.controller.status_label = '2'
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()
        thread_exe.assert_called()

    @patch("subprocess.Popen")
    def test_execute_calls_subprocess_popen(self, subprocess_popen):
        test_app = basic_app()
        test_app.controller.autostart = True
        test_app.controller.sit_models = {'1': {'id': 1},
                                          '2': {'id': 2}}
        test_app.controller.sit_model = '1'
        test_app.controller.quantity = 1
        test_app.controller.status_labels = {'1': {'id': 1},
                                             '2': {'id': 2}}
        test_app.controller.status_label = '2'
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()()
        subprocess_popen.assert_called()

    @patch("subprocess.call")
    def test_execute_calls_subprocess_call(self, subprocess_call):
        test_app = basic_app()
        test_app.controller.autostart = True
        test_app.controller.auto_upload = True
        test_app.controller.sit_models = {'1': {'id': 1},
                                          '2': {'id': 2}}
        test_app.controller.sit_model = '1'
        test_app.controller.quantity = 1
        test_app.controller.status_labels = {'1': {'id': 1},
                                             '2': {'id': 2}}
        test_app.controller.status_label = '2'
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()()
        subprocess_call.assert_called()
