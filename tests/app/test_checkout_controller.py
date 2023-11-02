__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.controller import CheckoutController, MainController
from src.template import CreateCheckoutTemplate

from unittest import TestCase
from unittest.mock import patch, mock_open


def basic_app():
    from kivymd.app import MDApp

    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super(TestApp, self).__init__(**kwargs)
            self.main_controller = MainController()
            self.controller = CheckoutController(self.main_controller)
    return TestApp()


class TestCreateCheckoutTemplate(TestCase):
    def test_create(self):
        create_instance = CreateCheckoutTemplate(
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        )
        with patch('builtins.open', new_callable=mock_open()) as mock_open_func:
            result = create_instance.create()
            mock_open_func.assert_called_with(result, 'w+', newline='', encoding='utf-8-sig')


class TestCheckoutController(TestCase):
    @patch("threading.Thread")
    def test_threading_start(self, thread_exe):
        test_app = basic_app()
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()
        thread_exe.assert_called()

    @patch("subprocess.Popen")
    def test_execute_calls_subprocess_popen(self, subprocess_popen):
        test_app = basic_app()
        test_app.controller.autostart = True
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()()
        subprocess_popen.assert_called()

    @patch("subprocess.call")
    def test_execute_calls_subprocess_call(self, subprocess_call):
        test_app = basic_app()
        test_app.controller.autostart = True
        test_app.controller.auto_upload = True
        test_app.controller.filepath = \
            r"C:\Users\MStefan\Documents\BBS1Mainz\3_Schuljahr\IHK-Abschlussprojekt\project\output\test"
        test_app.controller.execute()()
        subprocess_call.assert_called()
